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

# App usage:
1. 

# File structure:
```
|- utilities
    |- __init__.py
    |- loaders.py
    |- preprocessors.py
    |- utilities.py
|- download_data.py
|- *output
    |- ...
|- * input
    |- ...
|- .env
|- .gitignore
|- upload_changes.sh
|- requirements.txt
|- github-recovery-codes.txt
|- ELIZA.ipynb
|- rain.ipynb
|- readme.md
```



# Articles, Videos, Papers, Repositories:
1. https://docs.google.com/spreadsheets/d/1jCNzUx48DYMRWCqT0GYb9JfrBPiCh0H4B-PH3pyNZSc/edit?usp=sharing 
Feel free to add any other cleaning methods you deem necessary for the data. Also, in case the content is not in CSV or JSON format, please double-check the data to ensure it’s useful for character descriptions.

2. https://whitepaper.virtuals.io/#co-ownership-of-ai-agents-in-entertainment-and-gaming - primer on agentic AI

3. https://pathdao-my.sharepoint.com/personal/armielyn_virtuals_io/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Farmielyn%5Fvirtuals%5Fio%2FDocuments%2FIngestion&ga=1 - path to ingestion folder



# To do:
* preprocess data first
- Remove unnecessary characters or inconsistencies within the data (e.g., special symbols, excess whitespace).
- Ensure each text file contains a maximum of 40 rows. If a file exceeds this limit, split it into multiple files (e.g., file_part1.txt, file_part2.txt, etc.).
- Limit each row to a maximum of 700 characters to ensure compatibility with Retrieval-Augmented Generation (RAG) processes.
- Reject or exclude duplicate or irrelevant data that may not be useful for character descriptions or does not provide additional value.
* then try to validate if these dataset are ok
* pag tapos na add mo sa excel spreadsheet yung status ng data preprocessing task mo
* ito siguro yung output na kilangan
* create .sh script in python that is able to output this .sh script and when run, runs the command `node rag.js --input <myfile.txt> --agent <agent_id> --token <app_token> --bucket <bucket>` for all cleaned files, input is name of file and how many times you want this file to be run e.g. `node rag.js --input sportsbettoai1.txt --token 4065 --bucket finance` still take in as input the token arg, agent id arg, bucket arg, range, and name of input file. Output should be .sh file with name `{agent}_ingestor.sh`


# Insights:
* no need to prompt AI agents
* AI agents learn on their own without the intervention of human beings
* so all of the steps or ideas it comes up it did on its own liek for example if an AI agent revolves around the environment of twitter/X it can use feedback from people to learn on its own, and do things on its own accord like writing a tweet, planning how long it is to tweet again, plans what topics to tweet about etc.  
* pero does it require still training by a human being? This is probably that fine tuning task. Of training the LLM on specific set of data
* data used by LLMs may be instruction based or knowledge based 
* I would assume oracle-x learns from information from the stock market etc.
* fine tuning a model entails that it learns on a specific dataset revolving around a certain domain i.e. healthcare, investment, tech, literature
* `git branch <branch name>`, `git checkout <branch name you created>`, `git add . & git commit -m "<mesage>" & git push origin <branch name you created>`

# Skipped:

# Cleaned:
SisiyphusAI
ROron-ron
ORACLEX
Sport Bettor AI
Rain
Trust Me Bros
Eliza
askthesandwic

# Ingested:
HadesAI
Sport Bettor AI 11720 left to ingest stopped at 3689
Trust Me Bros
Ask the sandwich
Eliza (rejected)


# Notes:
- reject .jsons with gibberish numbers, booleans, etc.
- match dataset input output with description. if input is somehow not related to agents desc then reject it
- try to store output files or is it raw input files in database para di magkadoble doble


