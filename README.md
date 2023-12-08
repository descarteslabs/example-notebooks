# Getting Started with Descartes Labs Python API

This repository is meant to serve as an introduction to the Descartes Labs Python API and its modules. Please follow the steps located in our [Documentation page](https://docs.descarteslabs.com/installation.html) to install the client or simply run:

    pip install descarteslabs

## Overview

### Guides

Quickstart examples designed as a general overview for each of the core services within the Descartes Labs Platform:

1. [Logging in](01%20Logging%20In.ipynb) to your local client installation for the first time
2. [Catalog](https://docs.descarteslabs.com/descarteslabs/catalog/readme.html): Create, manage, search, share, and visualize data:
   - [01 Searching and Rastering Catalog Products.ipynb](guides/catalog/01%20Searching%20and%20Rastering%20Catalog%20Products.ipynb)
   - [02 Creating and Managing Products.ipynb](guides/catalog/02%20Creating%20and%20Managing%20Products.ipynb)
   - [03 Advanced Catalog Product Operations.ipynb](guides/catalog/03%20Advanced%20Catalog%20Product%20Operations.ipynb)
   - [04 Introduction to Blob Storage](guides/catalog/04%20Introduction%20to%20Blob%20Storage.ipynb)
   - [05 Searching and Retrieving Vector Tables](guides/catalog/05%20Searching%20and%20Retrieving%20Vector%20Tables.ipynb)
   - [06 Creating and Managing Vector Tables](guides/catalog/06%20Creating%20and%20Managing%20Vector%20Tables.ipynb)
3. [Dynamic Compute](https://docs.descarteslabs.com/api/dynamic-compute.html): An interactive geospatial computation engine
   - [01 Interactive Computing with Mosaics.ipynb](guides/dynamic-compute/01%20Interactive%20Computing%20with%20Mosaics.ipynb)
   - [02 Interactive Computing with ImageStacks.ipynb](guides/dynamic-compute/02%20Interactive%20Computing%20with%20ImageStacks.ipynb)
   - [03 GeoContexts and Array Computation.ipynb](guides/dynamic-compute/03%20GeoContexts%20and%20Array%20Computation.ipynb)
   - [04 Advanced Computing Concepts.ipynb](guides/dynamic-compute/04%20Advanced%20Computing%20Concepts.ipynb)
   - [05 Managing and Sharing in Dynamic Compute.ipynb](guides/dynamic-compute/05%20Managing%20and%20Sharing%20in%20Dynamic%20Compute.ipynb)
4. [Batch Compute](https://docs.descarteslabs.com/descarteslabs/compute/readme.html): A scalable asynchronous compute service
   - [01 Hello World.ipynb](guides/batch-compute/01%20Hello%20World.ipynb)
   - [02 Create Imagery.ipynb](guides/batch-compute/02%20Create%20Imagery.ipynb)
   - [03 Extracting Timeseries Data.ipynb](guides/batch-compute/03%20Extracting%20Timeseries%20Data.ipynb)

### Demos

End-to-end example analytics designed around more specific use cases, often utilizing multiple Descartes Labs Platform APIs in tandem:

1. Unsupervised Classification - Scaling a KMeans Model:
   - [01a Training an Unsupervised Classifier.ipynb](demos/01%20Unsupervised%20Classification/01a%20Training%20an%20Unsupervised%20Classifier.ipynb)
   - [01b Deploying an Unsupervised Classifier.ipynb](demos/01%20Unsupervised%20Classification/01b%20Deploying%20an%20Unsupervised%20Classifier.ipynb)
   - [01c Interactive Deployment with Dynamic Compute.ipynb](demos/01%20Unsupervised%20Classification/01c%20Interactive%20Deployment%20with%20Dynamic%20Compute.ipynb)

#### _Note for working with the Dynamic Compute and Vector APIs outside of a Workbench environment:_

For the time being these two packages must be installed separate from the Descartes Labs client:

    pip install descarteslabs-dynamic-compute


    pip install descarteslabs-vector

If you have any questions please reach out to support@descarteslabs.com
