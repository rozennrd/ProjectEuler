# Installer Jupyter Book
Ce livre utilise jupyter book.

Il convient d'installer un environnement virtuel spécifique:

```bash
mamba create --name JBook -c conda-forge python=3.9 jupytext jupyter-book
conda activate JBook
conda config --env --add channels conda-forge
mamba install jupyterlab ipywidgets ipykernel
mamba install nodejs
mamba install myst-nb jupyterlab-myst
```

# Utilisation
Les cours seront écrits avec des notebooks.

Pour que le rendu du notebook soit proche de l'export HTML 
il convient d'utiliser les notebooks avec l'extension jupyterlab-myst et 
jupytext

Démarrer jupyter lab
```bash
jupyter lab
```

Pour faciliter les diffs sous git, il faut utiliser nbdiff et appairer les
notebooks avec un équivalent Myst-Markdown grâce à jupytext

Sous Jupyter Lab :  
https://jupytext.readthedocs.io/en/latest/paired-notebooks.html

* CTRL+SHIFT+C
* Rechercher *pair*
* Sélectionner *pair with myst...*


Dans un SHELL:
```bash
jupytext --set-formats ipynb,md --sync notebook.ipynb
```

