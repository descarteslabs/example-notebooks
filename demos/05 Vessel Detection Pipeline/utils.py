import descarteslabs as dl
from descarteslabs.catalog import (
    Image,
    Product,
    GenericBand,
    properties as p
)
from descarteslabs.vector import Table, models

auth = dl.auth.Auth.get_default_auth()
org = auth.payload['org']
user_hash = auth.namespace

def reset_product(pid):
    '''
    Accepts a product ID and deletes it and its imagery if exists
    '''
    product = Product.get(pid)

    if product:
        print(f"Product found, deleting {pid}")
        status = product.delete_related_objects()
        if status:
            status.wait_for_completion()
        product.delete()
    print("Complete")

def reset_table(tid):
    '''
    Accepts a table ID and deletes it if exists
    '''
    if not tid.startswith(org or user_id):
        tid = f"{org or user_id}:{tid}"
    try:
        table = Table.get(tid)
        if table:
            table.delete()
            print(f"Deleted {tid}")
    except:
        return tid


def create_s1_product(pid, name):
    '''
    Accepts a product ID and name
    * Deletes product if exists 
    * Creates a new surrogate sigma0v product with just the VV band
    
    See source product for more details: esa:sentinel-1:sigma0v:v1 
    '''
    print("Checking for existing Product...")
    reset_product(pid)
    product = Product(id=pid)
    product.name = name
    product.tags = ["examples"]
    product.save()
    # Note this is all hard coded in for this demo! 
    band = GenericBand(
        id=f"{product.id}:vv",
        band_index=0, 
        file_index=0, 
        data_range=[1, 4095],
        data_type="UInt16",
        display_range=[858,2926],
        resolution={"unit":"meters", "value":10}
    )
    band.save()
    
    print("Saved band")
    img = Image(product=product, name="image1")
    img.acquired = "2025-02-04"
    upload = img.upload("data/s1_sample_1.tif", overwrite=True)
    upload.wait_for_completion()
    print("Added first image")
    
    return product.id

## Note this model is hard coded in! 
class S1VesselModel(models.MultiPolygonBaseModel):
    '''
    Basic vessel detections model with just DATE, SOURCE_IMG_ID, and geometry
    '''
    DATE: str
    SOURCE_IMG_ID: str
    
def create_s1_table(tid):
    '''
    Accepts a table ID, deletes if exists, and creates a new empty table
    based off VesselModel
    '''
    reset_table(tid)
    vessels_table = Table.create(
        tid, 
        name="S1 Vessel Detections Demo",
        model=S1VesselModel
    )
    return vessels_table.id

## Note this model is hard coded in! 
class S2VesselModel(models.MultiPolygonBaseModel):
    '''
    Basic vessel detections model with just DATE, SOURCE_IMG_ID, and geometry
    '''
    date: str
    confidence: str
    
def create_s2_table(tid):
    '''
    Accepts a table ID, deletes if exists, and creates a new empty table
    based off VesselModel
    '''
    reset_table(tid)
    vessels_table = Table.create(
        tid, 
        name="S2 Geoai Vessel Detections Demo",
        model=S2VesselModel
    )
    return vessels_table.id
