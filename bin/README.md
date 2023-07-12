# Installation commands for Conda Environment
conda env create --name nma-compneuro --file=environment.yml
conda activate nma-compneuro
conda install -c conda-forge umap-learn -y
conda install -c numba numba
