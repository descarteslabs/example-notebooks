# Testing Vector

`Vector` is now a public Descartes Labs client and can be tested internally within the organization. To set up a testing environment you can follow these general steps:

1. Install [Conda](https://docs.conda.io/en/latest/miniconda.html)
2. Create a [new environment](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf) >= Python 3.8
   - We recommend installing jupyter and git alongside your python version, e.g. `conda create --name vector_env python=3.8 jupyter git`
3. Install the Vector library via `pip install 'git+https://github.com/descarteslabs/descarteslabs-vector'`.
   - If you have previously installed the client and would like the latest client, run `pip uninstall vector` prior to installing.
4. Authenticate your `Descartes Labs` client by running `descarteslabs auth login`
5. Activate your new Conda environment `conda activate my_env`
6. Start your Jupyter Lab server `jupyter lab`
7. Enjoy!!
