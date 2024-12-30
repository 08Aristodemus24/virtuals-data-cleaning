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
main application to simulate an AI agent and their behavior: https://game-lite.virtuals.io/ 
documentation: https://virtualprotocol.notion.site/GAME-Documentation-1592d2a429e98016b389ea26b53686a3#15b2d2a429e980af9d18dad399a8eed1

5. public FAQ: https://virtualprotocol.notion.site/Public-GAME-Frequently-Asked-Questions-FAQ-s-1662d2a429e9807e804dfc2b09fcf620#1662d2a429e980839f33f7045626c828

6. public FAQ of GAME: https://www.notion.so/virtualprotocol/Public-GAME-Frequently-Asked-Questions-FAQ-s-1662d2a429e9807e804dfc2b09fcf620
*THIS IS GOLDMINE*

# To do:
## Backend Tasks:
* <s>preprocess data first</s>
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
* `git checkout master`, `git merge <branch name you created e.g. michael>`
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


## what does it mean for a web app to have no onchain like dexscreener?
In the context of a web application like Dexscreener, "no on-chain" means that the application **primarily relies on off-chain data** and computations rather than directly interacting with a blockchain for every operation.

Here's a breakdown:

On-Chain:
Data Storage: Data is stored directly on the blockchain, making it immutable and transparent **think of it as something everyone can see but they can't access or do things to it but they can indeed see it kasi there is always the risk that if they did have access to it they may use it in a malicious manner**.
Transactions: Transactions are recorded and verified on the blockchain.
Decentralization: Operations are typically decentralized, meaning no single entity controls the data or processes.   

Off-Chain:
Data Storage: Data is **stored on traditional servers or databases (where large companies own them e.g. aws, microsoft, google)**.
Computations: Calculations and **data processing occur on centralized servers (owned by large companies again)**.
Centralization: Some level of centralization is involved in managing the application and its data.

How Dexscreener Works (Primarily Off-Chain):

Dextscreener aggregates data from various sources, including:

Blockchain Explorers: It pulls data about token prices, trading volume, and market capitalization from blockchain explorers.
**Decentralized Exchanges (DEXs)** APIs: It uses APIs provided by DEXs to access real-time trading data.
This data is then processed and displayed on the Dexscreener website. While the underlying data originates from blockchains, Dexscreener doesn't perform every calculation or data retrieval directly on the blockchain.

Advantages of an Off-Chain Approach (like Dexscreener):

Speed: Off-chain computations are generally much faster than on-chain operations.   
Scalability: Handling large amounts of data and user traffic is more efficient off-chain.   
Cost-Effectiveness: Off-chain operations are typically cheaper than on-chain transactions, which incur gas fees.   
Disadvantages of an Off-Chain Approach:

Centralization: There's a degree of centralization, as Dexscreener controls the servers and data processing.
Trust: Users rely on Dexscreener to provide accurate and reliable data.
In Summary:

Dexscreener, by being primarily off-chain, prioritizes speed, scalability, and cost-effectiveness. It acts as an aggregator and presenter of blockchain data rather than a fully decentralized on-chain application. This allows it to provide a user-friendly experience for tracking and analyzing crypto assets.

## what are off chain data anyway? Explain it to me a relatively good programmer with knowledge in developing simple APIs intgrated to ML models.

Let's break down "off-chain data" in a way that's relatable to a programmer familiar with APIs and ML models.

Analogy: Think of a restaurant

On-chain: This is like the **restaurant's kitchen**. All the **core operations** happen here: **cooking the food (executing smart contracts)**, **storing ingredients (blockchain data)**, and serving the dishes (transactions). Everything is **transparent** and verifiable, but it **can be slow and expensive** (like gas fees on a blockchain).

Off-chain: This is like the **restaurant's dining area**, the **menu**, the **reservation system**, and the **customer database**. These **are separate systems that interact with the kitchen** (on-chain) but **handle a lot of the work independently (outside of the kitchen)**.

In the context of blockchain and web3:

**On-chain data (the food ingredients) resides directly on the blockchain (the kitchen)**. **Every transaction (serving dishes)**, **smart contract execution (cooking food)**, and **piece of information (ingredients)** is recorded and stored on the distributed ledger. It's immutable, transparent, and verifiable by anyone with access to the blockchain.

**Off-chain data lives outside the blockchain (the kitchen)**, typically **in traditional databases**, **servers**, or other storage systems. It's managed and controlled by specific entities, which can be centralized or decentralized. **Isipin mo yung on chain data is stored in a decentralized system where no corporation, organization, has control over it and anyone and everyone has control over it unlike relational dbs, servers, which are managed by corporations, organizations, think google, amazon, microsoft etc.**

Relating to APIs and ML models:

Imagine you're building a price prediction model for a cryptocurrency.

On-chain data: This would be the raw transaction data on the blockchain: block timestamps, transaction hashes, amounts transferred, etc. Accessing this data directly for every prediction would be extremely inefficient and expensive.

Off-chain data: This could be:
Historical price data: Stored in a time-series **database (owned by amazon)**.
Market sentiment data: Collected from social media or **news sources (owned by new york times, time, new york post, washington post)** and stored in a database.
Technical indicators: Calculated off-chain using historical price data.
How your API and ML model interact with off-chain data:

Data Collection: You would use APIs (e.g., from exchanges or data providers) to collect historical price data, market sentiment, and other relevant **information (that may be owned by different organizations and corporations)**. This data is **stored in your off-chain database**.
Feature Engineering: Your ML model would use this off-chain data to calculate features like moving averages, volatility, or sentiment scores.
Model Training: You train your ML model using this off-chain data.
Prediction: When a user requests a price prediction, your API would:
Fetch the latest relevant off-chain data.
Use the trained ML model to generate a prediction.
Return the prediction to the user.

In Dexscreener's case: They use off-chain data (from DEX APIs and blockchain explorers) to provide real-time price charts and market analysis. They don't execute trades or store order books on-chain.

Using off-chain data is a common and practical approach for many web3 applications, allowing for better performance and user experience while still leveraging the underlying blockchain for core functionalities.

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


