snapshot_pilot
==============================
### Repository used for the "snapshot pilot" experiment, as part of the TTT project.
This repo contains 3 folders: notebooks (currently not used), reports (contains 'figures' folder, and may contain other overviews/reports/summaries in the future), and src (contains code used to produce figures).
There is also an Excel file, "SS_data_collector.xlsx," which contains the key data from the experiment, including cell counts done by me. The code uses this spreadsheet as input.

### Reproducing figures:
1. Download the repository to a local directory.
2. Open Anaconda prompt and cd to snapshot_pilot\src\visualization
3. Run these commands: \
`conda activate snapshot_env` \
`python snapshot_visualization_script.py`
4. You will be prompted to input today's date; this will be used as part of the file names when saving out figures.
5. Figures will be saved in \snapshot_pilot\reports\figures.

Project Organization: Local (not all files listed below are version controlled or included on GitHub)
------------

    ├── LICENSE
    ├── README.md         
    ├── data               <- Not git-controlled.
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
