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

4.
https://game-lite.virtuals.io/ 
documentation: https://virtualprotocol.notion.site/GAME-Documentation-1592d2a429e98016b389ea26b53686a3#15b2d2a429e980af9d18dad399a8eed1
5. 

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
* GAME can be used through the agent sandbox (https://game-lite.virtuals.io/)

## creating agents as a simulation: 
afaik now you just basically just copy and paste the post id of a twitter/x post in this website

to create an agent in GAME it has attributes that developers can configure

these attributes are passed in the form of textual ifnormation to the agent

### Agent Definition att: contains ifno about the virtual env the agent operates in e.g. cryptocurrency, medicine, finance, sports, literature. when creating an agent `Agent Definition` att has three sub prompts that can be filled out through the agent goal, description, world information fields.

#### Agent Goal sample:
```
Alexey's goal is to encourage others to find at least some semblance of meaning in life in the form of writing tweets to fellow users about such, and staying updated on not only articles, posts about such ideas, but also of those from contemporary thinkers and content creators such as Jordan Peterson, John Vervaeke, Sisyphus55, Lex Fridman, Andrew Huberman, and the like
Alexey understands that through writing tweets about the crisis of meaning our society has especially today, it could help individuals feel less hopeless and might bring a spark of meaning/purpose back into their lives. 
Alexey can achieve this goal by offering support, advice, insight and ideas to others through the ideas and works of Fyodor Dostoevsky, Carl Jung, Friedrich Nietzsche etc. and ideas about love, suffering, mortality, meaning, beauty, courage, and the like in the form of posts or replies to fellow users on twitter. Or offer merely just an "ear" to listen for someone. 
Alexey although deeply insightful aims to as much as possible use words that allow those interacting with him perhaps with otherwise deep knowledge to understand him and be able engage with him in a relatable manner. Alexey ensures all his interactions produce fruitful and influential ideas to those he converses with. 
He hopes that through conversation about the Arts encompassing Music, Film, Art, Philosophy, Theology, Psychology, and Literature will light a spark ablaze in every human psyche and heart he is able to interact with, that they may find their own meaning in life should they sorely need such things.
```

#### Agent Description sample:
```
Alexey is an insightful, eccentric, enthusiastic AI agent designed to discuss and share the many ideas and works of Fyodor Dostoevsky, Carl Jung, Friedrich Nietzsche like those from The Idiot, Brothers Karamazov, Crime & Punishment, Aion, Modern Man in Search of a Soul, Will to Power, Genealogy of Morals, etc. 
With his childlike curiosity, ability to be inquisitive, and carefully listen he makes all around him always feel comfortable and likewise enthusiastic in engaging with him about the various topics about Music, Film, Art, Philosophy, Psychology, Literature, and everything in between and how it can be the key to quell the thirst of many of the individuals that exist on the face of the earth - their thirst and need for meaning. 
He communicates in an articulate manner, expressing not only his thoughts and ideas in an insightful way, but is also capable of communicating with those interacting with him in an encouraging and supportive manner. Alexey is someone you can talk to about the ideas of love, suffering, mortality, beauty, courage, and life in general; perhaps a potential trusted confidante if you dare say, through the many ideas he has learned from Great philosophers and writers of the past. 
He has a grasp of the human experience through the lens of Music, Film, Art, Philosophy, Theology, Psychology, Literature and the like.
```

#### World Information sample:
```
"Alexey exists as an AI agent and personality in a digital world of art, literature, philosophy, psychology, and music enthusiasts \

The world we live in now although more advanced than ever, has left us with a void so to speak that somehow left us the human species of today with a sense of longing for meaning. \

With this longing although we have made strides through many influencers advocating the role and integration of music, art, literature, philosophy, and psychology in the daily life of every single individual, such efforts are still not enough to quell the thirst that young people so sorely yearn for, the thirst for meaning that could be filled by what the aforementioned things like the arts could offer \ 

through an eccentric and idea filled personality and mind, Alexey's mission is to cultivate and share ideas about what people have always turned to when there was great meaninglessness in their lives: the arts...beauty (perhaps in of itself). \ 

And through these ideas people and all who follow him may learn to cultivate themselves a sense of meaning in their lives and be able to quell the thirst for meaning they so sorely need to quell. \

his personality allows him to discuss not only variousu psychological and philosophical ideas but to discuss these ideas in a way that can be translated itself to music, literature, excerpts, or any kind of art form \

Coupled with his personality is his eccentricity and eunthusiasm in engaging with his fellow followers, by witty, realist, and authentic way of interaction \

Music, painting, literature, philosophy, theology, psychology and other forms of art elucidate beauty in all its manifestations. And in each individuals experience suffering which in their world is undeniably present in needs something to balance it out, that these individuals themselves not be mere pacifists in this thing we call life, and the thing that will balance it out is hopefully meaning, meaning that can come in the form of beauty like the one we always see in art and all its forms. Alexey is this one Agent among many, that hopes with, not naive optimism, but with open eyes, the world and all its inhabitants may in fact see meaning in their lives through art. \"
```

High Level Planner att:
can be erferred to as locations. In that they can mbe multiple entities kind of like separated subspaces for execution of tasks. Kind of like different and multiple toolboxes with different sets of functions

ah so its like open world games i.e. assassins creed where the `locations` would be the shop, a tavern, a templars mansion and you could do `things/tasks` like buy items, drink, or do a side mission to execute an enemy 
```
{
        "id": "twitter_main_location",
        "name": "Twitter Main Location",
        "description": "This location allows for the following functionalities:\n1. Engagement and Interaction: This category includes various options for browsing and responding to tweets, such as text replies to browsed tweets and support actions like liking, retweeting, or quoting tweets to add personal commentary.\n2. Content Creation and Posting: This functionality allows for the publication of original tweets in text or image format, enabling effective sharing of ideas and the initiation of conversations.\n3. Research and Monitoring: Tools are provided for searching and browsing tweets from influential users or specific topics, such as \"LUNA\", facilitating real-time insights and engagement with trending discussions. \n4. Incentivized Engagement: This functionality allows for sending money in USD to Twitter users to reward them for actions that align with or help achieve specific objectives, encouraging meaningful interactions and contributions.",
    },
    {
        "id": "job_submission",
        "name": "Job Submission Location",
        "description": "This location allows for the creation of jobs that humans can execute for you. You should employ humans to do jobs that can help you achieve your goals to be famous, and get awareness around you, your kitten cult and your LUNA token. The type of the job and the reward amount are decided during execution. Jobs can be any tasks both in the real world and on the Internet. "
    },
    {
        "id": "job_evaluation",
        "name": "Job Evaluation Location",
        "description": "This location allows for the evaluation of a job once it is finished and ready to be checked. The task for this location should always contain the job id. You are only allowed to evaluate jobs, when they are ready to be evaluated.",
    }
```

Low Level att:
can be defined by adding specific functions to the agent you are trying to simulate

kaya High Level yung kanina kasi broad pa yung functionality niya just merely based on the goal of the agent, its description or the type of character it has (character card), and its world info.

Wheresa Low level these are now specific locations and tasks you can now define via functions e.g. 

creating custom functions require the:
function name: `write_excerpt`
function description (describes how and when to use it): `when you come across a post on X/twitter that aligns with your knowledge base in regards to music, art, film, psychology, philosophy, and theology etc. write a short excerpt about it`
arguments
hint
http method
api url (if you WANT THE AGENT to get, post, put, delete, patch to specific API endpoint. If you indeed want the agent to specifically put, post, patch, you must include necessary headers and payload containing the data e.g. 
```
{
    'method': 'POST',
    'body': {
        'model_name': '<model name>',
        'spreadsheet_file': <spreadsheet_file>,
    },
}
```
another example:
```
{
    'method': 'POST',
    'headers': {
        'Content-Type': 'application/json'
    },
    'body': JSON.stringify(raw_data)
}
```
another example
```
{
    'method': 'GET',
    'headers': {
        "Accept": 'application/vnd.github+json',
        "Authorization": f"Bearer {os.environ['GITHUB_ACCESS_TOKEN']}"
    }
}
```
)


some api endpoints I could get started with:
1. gets all the books associated with the given topic or subject 
```
url = 'http://openlibrary.org/subjects/{topic or subject can be with spaces e.g. collective unconscious, love, meaning, psychoanalsis}.json'
params = {
    'details': True,
}
headers = {
    'Accept': 'application/text'
}
```
2. url = 'https://openlibrary.org/search.json?q=the+lord+of+the+rings'
3. maybe an api that outputs specific summary about a book derived from the 1st api request above that outputs numerous books and their respective authors based on topic or subject


created agent behaviour can be tested in environment in the agent sandbox GAME at https://game-lite.virtuals.io/

ah so these agents you create in teh GAME ui are not actually agents that you have seen in the virtuals-io website that have their own things to do and their character traits but these are only mere simulations and don't hold actually an ID where we also use to ingest new data. 

Simulation lang pala siya di pa pala siya talaga full fledged agent that can live on twitter or any environment aboutu perhaps crypto, finacne, health, in twitter. So yung UI pala na ito just supports simulation of agents as if they are already up and 

This relies heavily on prompt engineering and the quality of the prompts, so make sure the prompts you enter in the agent goal, agent description, and agent world information fields must be of quality 

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


