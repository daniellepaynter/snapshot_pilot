snapshot_pilot
==============================
This repo contains
Experiments to test 4OHT efficiency in inducing tdTomato expression in RABV+ cells.
Method files are not version controlled.

Project Organization
------------

    ├── LICENSE
    ├── README.md         
    ├── data
    │   ├── processed      <- Contains one folder per mouse, named with mouse ID. Folder contains a selection of images of brain slices, exported to PNGs or TIFs from .lif files using LAS-X software. 
    │   └── raw            <- Contains one folder per mouse, named with the mouse ID.
    │		 └── mouseID
    │				└── Axio <- Not present for all mice. Contains epifluorescence images of slides obtained with AxioImager 
    │				└── Confocal <- Contains data obtained primarily at Leica SP8 Matrix confocal microscope.
    │						Each file represents one slide, with up to 3 slices on the slide. Within the file,
    │						individual acquisitions are named with the slice num (1, 2, or 3) and a letter (1a, 1b, etc.). 
    │						Optionally,an acquisition name may also include the approximate brain region (1a_cortex, 1b_thal). 
    │								
    │
    ├── methods            <- Notes and protocols used in the experiment. Not git-controlled.
    │
    ├── notebooks          <- Jupyter notebooks. 
    │
    │
    ├── reports            <- Figures, summaries, overviews of the experiment.
    │   └── figures        <- Generated graphics and figures representing the dataset. Generated with code found in src.
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
