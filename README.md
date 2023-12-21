# Getting Started with Descartes Labs Python API

This repository is designed to serve as an introduction to the Descartes Labs Python API and its modules.

## Installation

Please follow the steps located in our [Documentation page](https://docs.descarteslabs.com/installation.html) to install the client or simply run:

    pip install descarteslabs

**_Note for working with the Dynamic Compute and Vector APIs outside of a Workbench environment_**

For the time being these two packages must be installed separate from the Descartes Labs client:

    pip install descarteslabs-dynamic-compute

    pip install descarteslabs-vector

## Overview

A general outline of the sample notebooks located in this repo is as follows:

### Guides

Quickstart examples outlined as a general overview for each of the core services within the Descartes Labs Platform.

1. [Logging in](guides/01%20Logging%20In.ipynb) to your local client installation for the first time
2. [Catalog](https://docs.descarteslabs.com/descarteslabs/catalog/readme.html): Create, manage, search, share, and visualize data
   - [01 Searching and Rastering Catalog Products.ipynb](guides/catalog/01%20Searching%20and%20Rastering%20Catalog%20Products.ipynb)
   - [02 Creating and Managing Products.ipynb](guides/catalog/02%20Creating%20and%20Managing%20Products.ipynb)
   - [03 Advanced Catalog Product Operations.ipynb](guides/catalog/03%20Advanced%20Catalog%20Product%20Operations.ipynb)
   - [04 Introduction to Blob Storage.ipynb](guides/catalog/04%20Introduction%20to%20Blob%20Storage.ipynb)
   - [05 Searching and Retrieving Vector Tables.ipynb](guides/catalog/05%20Searching%20and%20Retrieving%20Vector%20Tables.ipynb)
   - [06 Creating and Managing Vector Tables.ipynb](guides/catalog/06%20Creating%20and%20Managing%20Vector%20Tables.ipynb)
3. [Dynamic Compute](https://docs.descarteslabs.com/api/dynamic-compute.html): An interactive geospatial computation engine
   - [01 Interactive Computing with Mosaics.ipynb](guides/dynamic-compute/01%20Interactive%20Computing%20with%20Mosaics.ipynb)
   - [02 Interactive Computing with ImageStacks.ipynb](guides/dynamic-compute/02%20Interactive%20Computing%20with%20ImageStacks.ipynb)
   - [03 GeoContexts and Array Computation.ipynb](guides/dynamic-compute/03%20GeoContexts%20and%20Array%20Computation.ipynb)
   - [04 Advanced Computing Concepts.ipynb](guides/dynamic-compute/04%20Advanced%20Computing%20Concepts.ipynb)
   - [05 Managing and Sharing in Dynamic Compute.ipynb](guides/dynamic-compute/05%20Managing%20and%20Sharing%20in%20Dynamic%20Compute.ipynb)
4. [Batch Compute](https://docs.descarteslabs.com/descarteslabs/compute/readme.html): A highly scalable asynchronous compute service
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

## Support

If you have any questions please reach out to [support@descarteslabs.com](support@descarteslabs.com) or visit [support.descarteslabs.com](https://support.descarteslabs.com).
