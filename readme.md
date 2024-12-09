# Requirements:
1. git
2. conda
3. python

# Source code usage
1. assuming git is installed clone repository by running `git clone https://github.com/08Aristodemus24/virtuals-internship`
2. assuming conda is also installed run `conda create -n <environment name e.g. virtuals-internship> python=3.12.3`. Note python version should be `3.12.3` for the to be created conda environment to avoid dependency/package incompatibility.
3. run `conda activate virtuals-internship` or `activate virtuals-internship`.
4. run `conda list -e` to see list of installed packages. If pip is not yet installed run conda install pip, otherwise skip this step and move to step 5.
5. navigate to directory containing the `requirements.txt` file.
5. run `pip install -r requirements.txt` inside the directory containing the `requirements.txt` file
6. after installing packages/dependencies run `python index.py` while in this directory to run app locally

# App usage:
1. control panel of app will have ff. inputs: raw eda signals

# File structure:
```
|- client-side
    |- public
    |- src
        |- assets
            |- mediafiles
        |- boards
            |- *.png/jpg/jpeg/gig
        |- components
            |- *.svelte/jsx
        |- App.svelte/jsx
        |- index.css
        |- main.js
        |- vite-env.d.ts
    |- index.html
    |- package.json
    |- package-lock.json
    |- ...
|- server-side
    |- modelling
        |- data
            |- Artifact Detection Data
                |- test
                    |- *_features.csv
                    |- *_labels.csv
                |- train
                    |- *_features.csv
                    |- *_labels.csv
                |- reduced_cueva_second_phase_svm_feature_set1.txt
                |- reduced_cueva_second_phase_svm_feature_set.txt
                |- hossain_feature_set.txt
                |- reduced_hossain_lr_feature_set.txt
                |- reduced_hossain_gbt_feature_set.txt
                |- reduced_hossain_svm_feature_set.txt
                |- taylor_feature_set.txt
                |- reduced_taylor_lr_feature_set.txt
                |- reduced_taylor_rf_feature_set.txt
                |- reduced_taylor_svm_feature_set.txt
            |- Electrodermal Activity artifact correction BEnchmark (EDABE)
                |- Train
                    |- *.csv
                |- Test
                    |- *.csv
            |- Hybrid Artifact Detection Data
                |- train
                    |- *_hof.csv
                    |- *_lof.csv
                    |- *_labels.csv
                |- test
                    |- *_hof.csv
                    |- *_lof.csv
                    |- *_labels.csv
                |- dummy.txt
            |- Hosseini_Stress_Dataset
            |- Stress Detection Features
            |- dummy.txt
            |- EDABE dataset.zip
            |- Stress_dataset.zip
        |- figures & images
            |- *.png/jpg/jpeg/gif
        |- models
            |- __init__.py
            |- cueva.py
            |- llanes_jurado.py
        |- results
            |- all_models_results.json
            |- hossain_gbt_results.json
            |- hossain_lr_results.json
            |- hossain_svm_results.json
            |- taylor_rf_results.json
            |- taylor_lr_results.json
            |- taylor_svm_results.json
            |- pqbqpr_expert2_corrected.csv
        |- saved
            |- misc
                |- cueva_lstm-fe_meta_data.json
                |- jurado_lstm-cnn_meta_data.json
                |- hossain_lr_scaler.pkl
                |- hossain_svm_scaler.pkl
                |- hossain_gbt_scaler.pkl
                |- xgb_scaler.pkl
                |- dummy.pkl
            |- models
                |- cueva_second_phase_svm_clf1.pkl
                |- cueva_second_phase_svm_clf.pkl
                |- hossain_lr_clf.pkl
                |- hossain_svm_clf.pkl
                |- hossain_gbt_clf.pkl
                |- taylor_lr_clf.pkl
                |- taylor_svm_clf.pkl
                |- taylor_rf_clf.pkl
                |- stress_detector.pkl
                |- dummy.pkl
            |- weights
                |- *.weights.h5
        |- utilities
            |- __init__.py
            |- loaders.py
            |- preprocessors.py
            |- visualizers.py
            |- evaluators.py
            |- feature_extractors.py
            |- stress_feature_extractors.py
        |- __init__.py
        |- experimentation.ipynb
        |- feature_engineering.ipynb
        |- data_analysis.ipynb
        |- summarization.ipynb
        |- evaluation.ipynb
        |- visualization.ipynb
        |- stress_detection.py
        |- tuning_ml.py
        |- tuning_dl.py
        |- *.sbatch
    |- static
        |- assets
            |- *.js
            |- *.css
        |- index.html
    |- index.py
    |- server.py
    |- requirements.txt
|- demo-video.mp5
|- .gitignore
|- readme.md
```

# Articles, Videos, Papers, Repositories:
1. https://docs.google.com/spreadsheets/d/1jCNzUx48DYMRWCqT0GYb9JfrBPiCh0H4B-PH3pyNZSc/edit?usp=sharing 
Feel free to add any other cleaning methods you deem necessary for the data. Also, in case the content is not in CSV or JSON format, please double-check the data to ensure it’s useful for character descriptions.

2. https://whitepaper.virtuals.io/#co-ownership-of-ai-agents-in-entertainment-and-gaming

3. https://pathdao-my.sharepoint.com/personal/armielyn_virtuals_io/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Farmielyn%5Fvirtuals%5Fio%2FDocuments%2FIngestion&ga=1
path to ingestion folder
# To do:
* preprocess data first
- Remove unnecessary characters or inconsistencies within the data (e.g., special symbols, excess whitespace).
- Ensure each text file contains a maximum of 40 rows. If a file exceeds this limit, split it into multiple files (e.g., file_part1.txt, file_part2.txt, etc.).
- Limit each row to a maximum of 700 characters to ensure compatibility with Retrieval-Augmented Generation (RAG) processes.
- Reject or exclude duplicate or irrelevant data that may not be useful for character descriptions or does not provide additional value.
* then try to validate if these dataset are ok
* pag tapos na add mo sa excel spreadsheet yung status ng data preprocessing task mo
* ito siguro yung output na kilangan
```
oracle-x
oracle-x is a cutting-edge ai agent blending ancient wisdom with advanced intelligence to provide real-time blockchain and cryptocurrency insights. she actively tracks trends, engages with users, and shares credible updates, establishing herself as the most trusted ai agent for cryptocurrency knowledge.
oracle-x embodies elegance and reliability, adorned in a flowing white robe with intricate gold patterns. her radiant golden aura symbolizes clarity, wisdom, and trust.
represents trust, enlightenment, and intelligence within a dynamic and complex ecosystem.
```


# Insights:
* no need to prompt AI agents
* AI agents learn on their own without the intervention of human beings
* so all of the steps or ideas it comes up it did on its own liek for example if an AI agent revolves around the environment of twitter/X it can use feedback from people to learn on its own, and do things on its own accord like writing a tweet, planning how long it is to tweet again, plans what topics to tweet about etc.  
* pero does it require still training by a human being? This is probably that fine tuning task. Of training the LLM on specific set of data
* data used by LLMs may be instruction based or knowledge based 
* I would assume oracle-x learns from information from the stock market etc.
* fine tuning a model entails that it learns on a specific dataset revolving around a certain domain i.e. healthcare, investment, tech, literature

# Skipped

