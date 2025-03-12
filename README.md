# Getting Started with Descartes Labs Python API

This repository is designed to serve as an introduction to the Descartes Labs Python API and its modules.

## Installation

Please follow the steps located in our [Documentation page](https://docs.descarteslabs.com/installation.html) to install the client or simply run:

    pip install descarteslabs

**_Note for working with the Dynamic Compute API outside of a Workbench environment_**

For the time being this package must be installed separate from the core Descartes Labs client:

    !pip install descarteslabs-dynamic-compute

## Overview

A general outline of the tutorial notebooks located in this repo is as follows:

### Guides

Quickstart examples outlined as a general overview for each of the core services within the Descartes Labs Platform.

1. [Logging in](guides/01%20Logging%20In.ipynb) to your local client installation for the first time
2. [Catalog](https://docs.descarteslabs.com/descarteslabs/catalog/readme.html) - Create, manage, search, share, and visualize data:
   - [01 Searching and Rastering Catalog Products.ipynb](guides/catalog/01%20Searching%20and%20Rastering%20Catalog%20Products.ipynb)
   - [02 Creating and Managing Products.ipynb](guides/catalog/02%20Creating%20and%20Managing%20Products.ipynb)
   - [03 Advanced Catalog Product Operations.ipynb](guides/catalog/03%20Advanced%20Catalog%20Product%20Operations.ipynb)
   - [04 Introduction to Blob Storage.ipynb](guides/catalog/04%20Introduction%20to%20Blob%20Storage.ipynb)
   - [05 Searching and Retrieving Vector Tables.ipynb](guides/catalog/05%20Searching%20and%20Retrieving%20Vector%20Tables.ipynb)
   - [06 Creating and Managing Vector Tables.ipynb](guides/catalog/06%20Creating%20and%20Managing%20Vector%20Tables.ipynb)
   - [07 Introduction to Events.ipynb](guides/catalog/07%20Introduction%20to%20Events.ipynb)
3. [Dynamic Compute](https://docs.descarteslabs.com/api/dynamic-compute.html) - An interactive geospatial data processing engine:
   - [01 Interactive Computing with Mosaics.ipynb](guides/dynamic-compute/01%20Interactive%20Computing%20with%20Mosaics.ipynb)
   - [02 Interactive Computing with ImageStacks.ipynb](guides/dynamic-compute/02%20Interactive%20Computing%20with%20ImageStacks.ipynb)
   - [03 GeoContexts and Array Computation.ipynb](guides/dynamic-compute/03%20GeoContexts%20and%20Array%20Computation.ipynb)
   - [04 Advanced Computing Concepts.ipynb](guides/dynamic-compute/04%20Advanced%20Computing%20Concepts.ipynb)
   - [05 Managing and Sharing in Dynamic Compute.ipynb](guides/dynamic-compute/05%20Managing%20and%20Sharing%20in%20Dynamic%20Compute.ipynb)
4. [Batch Compute](https://docs.descarteslabs.com/descarteslabs/compute/readme.html) - A highly scalable asynchronous compute service:
   - [01 Hello World.ipynb](guides/batch-compute/01%20Hello%20World.ipynb)
   - [02 Create Imagery.ipynb](guides/batch-compute/02%20Create%20Imagery.ipynb)
   - [03 Extracting Timeseries Data.ipynb](guides/batch-compute/03%20Extracting%20Timeseries%20Data.ipynb)

### Demos

End-to-end example analytic pipelines oriented towards specific applications in remote sensing.

1. Unsupervised Machine Learning - Scale a kmeans clustering algorithm:
   - [01a Training an Unsupervised Classifier.ipynb](demos/01%20Unsupervised%20Classification/01a%20Training%20an%20Unsupervised%20Classifier.ipynb)
   - [01b Deploying an Unsupervised Classifier.ipynb](demos/01%20Unsupervised%20Classification/01b%20Deploying%20an%20Unsupervised%20Classifier.ipynb)
   - [01c Interactive Deployment with Dynamic Compute.ipynb](demos/01%20Unsupervised%20Classification/01c%20Interactive%20Deployment%20with%20Dynamic%20Compute.ipynb)
2. Supervised Machine Learning - Predict land cover by training and deploying a random forest classifier:

   - [02a Generate Training Data.ipynb](demos/02%20Supervised%20Classification/02a%20Generate%20Training%20Data.ipynb)
   - [02b Training a Supervised Classifier.ipynb](demos/02%20Supervised%20Classification/02b%20Training%20a%20Supervised%20Classifier.ipynb)
   - [02c Deploying a Supervised Classifier.ipynb](demos/02%20Supervised%20Classification/02c%20Deploying%20a%20Supervised%20Classifier.ipynb)
   - [02d Interactive Deployment with Dynamic Compute.ipynb](demos/02%20Supervised%20Classification/02d%20Interactive%20Deployment%20with%20Dynamic%20Compute.ipynb)

3. Image Segmentation - Train and deploy a simple computer vision model to detect well pads in West Texas:

   - [03a Generate Training Data.ipynb](demos/03%20Image%20Segmentation/03a%20Generate%20Training%20Data.ipynb)
   - [03b Training a Segmentation Model.ipynb](demos/03%20Image%20Segmentation/03b%20Training%20a%20Segmentation%20Model.ipynb)
   - [03c Deploying a Segmentation Model.ipynb](demos/03%20Image%20Segmentation/03c%20Deploying%20a%20Segmentation%20Model.ipynb)
   - [03d Interactive Deployment with Dynamic Compute.ipynb](demos/03%20Image%20Segmentation/03d%20Interactive%20Deployment%20with%20Dynamic%20Compute.ipynb)

4. Hurricane Case Study - Analyze the impacts of Hurricane Ida on roughly 7500 offshore oil rigs in the Gulf of Mexico:
   - [04 Hurricane Ida Offshore Rigs.ipynb](demos/04%20Hurricane%20Ida%20Case%20Study/04%20Hurricane%20Ida%20Offshore%20Rigs.ipynb)
   
5. Vessel Detection Pipeline - Deploy a sample vessel detection pipeline which responds to new image upload events:
    - [01 Kaohsiung Port New Image Events.ipynb](demos/05%20Vessel%20Detection%20Pipelines/01%20Kaohsiung%20Port%20New%20Image%20Events.ipynb)
    - [02 Alang Shipbreaking Yard Daily Monitoring.ipynb](demos/05%20Vessel%20Detection%20Pipelines/02%20Alang%20Shipbreaking%20Yard%20Daily%20Monitoring.ipynb)

6. Dynamic Compute Demos - Various case studies implementing scientific methodologies on open data through Dynamic Compute:
    - [01 Se2WaQ Neuchatel Lake](demos/Dynamic%20Compute%20Demos/01%20Se2WaQ%20Neuchatel%20Lake.ipynb)
    - [02 Sentinel-1 Vessel Detection Shanghai](demos/Dynamic%20Compute%20Demos/02%20Sentinel-1%20Vessel%20Detection%20Shanghai.ipynb)
    
## Support

If you have any questions please reach out to [dl.support@earthdaily.com](dl.support@earthdaily.com).
