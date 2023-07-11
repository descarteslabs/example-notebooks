# Getting Started with Descartes Labs Python API

This is meant to serve as an introduction to the `Descartes Labs Python API` and it's core modules. Please follow the steps located in our [Documentation page](https://docs.descarteslabs.com/installation.html) to install the client or simply run:

    pip install descarteslabs

To install the latest development version on Github you can also run:

     pip install -U git+https://github.com/descarteslabs/descarteslabs-python.git

## Overview

A general outline of the tutorials located in this repo is as follows:

1. [Logging in](01%20Logging%20In.ipynb) to your local client installation for the first time
2. [Catalog](/guides/catalog/): Create, manage, search, share, and visualize data. These guides include a [General Catalog Object Overview](guides/catalog/Catalog%20Overview.ipynb) as well as:
   - [01 Searching and Rastering Catalog Products.ipynb](guides/catalog/01%20Searching%20and%20Rastering%20Catalog%20Products.ipynb)
   - [02 Creating and Managing Products.ipynb](guides/catalog/02%20Creating%20and%20Managing%20Products.ipynb)
   - [03 Introduction to Blob Storage](guides/catalog/03%20Introduction%20to%20Blob%20Storage.ipynb)
   - [04 Introduction to Vector](guides/catalog/04%20Introduction%20to%20Vector%20Data.ipynb)
3. [Dynamic Compute](guides/dynamic-compute/): An interactive geospatial computation engine
   - [01 Interactive Computing with Mosaics.ipynb](guides/dynamic-compute/01%20Interactive%20Computing%20with%20Mosaics.ipynb)
   - [02 Interactive Computing with ImageStacks.ipynb](guides/dynamic-compute/02%20Interactive%20Computing%20with%20ImageStacks.ipynb)
   - [03 GeoContexts and Array Computation.ipynb](guides/dynamic-compute/03%20GeoContexts%20and%20Array%20Computation.ipynb)
   - [04 Advanced Computing Concepts.ipynb](guides/dynamic-compute/04%20Advanced%20Computing%20Concepts.ipynb)
   - [05 Managing and Sharing in Dynamic Compute.ipynb](guides/dynamic-compute/05%20Managing%20and%20Sharing%20in%20Dynamic%20Compute.ipynb)
4. [Batch Compute](guides/batch-compute/): A scalable asynchronous compute service
   - [01 Hello World.ipynb](guides/batch-compute/01%20Hello%20World.ipynb)
   - [02 Create Imagery.ipynb](guides/batch-compute/02%20Create%20Imagery.ipynb)

### _Note_ For working with the `Dynamic Compute` and `Vector` APIs outside of a `Workbench` environment:

For the time being these two packages must be installed separate from the `Descartes Labs` client:

    pip install 'git+https://github.com/descarteslabs/descarteslabs-dynamic-compute'

    pip install descarteslabs-vector
