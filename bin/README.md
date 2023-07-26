# Installation commands for Conda Environment

```
conda env create --name nma-compneuro --file=environment.yml
conda activate nma-compneuro
conda install -c conda-forge umap-learn -y
conda install -c numba numba
python -m pip install suite2p
conda install -c conda-forge ruptures -y
conda install -c conda-forge umap-learn -y
```