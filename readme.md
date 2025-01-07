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

7. developer forum discord channel: https://discord.com/channels/1214528554197319690/1322795296236900403/1322795296236900403 - where developers could interact with other developers or builders in order to answer each others question. If a builder has a technical query then they can be referred to post here their inquiry in order to potentially be answered by other developers

8. 

# To do:
## Backend Tasks:
* <s>preprocess data first</s>
- Remove unnecessary characters or inconsistencies within the data (e.g., special symbols, excess whitespace).
- Ensure each text file contains a maximum of 40 rows. If a file exceeds this limit, split it into multiple files (e.g., file_part1.txt, file_part2.txt, etc.).
- Limit each row to a maximum of 700 characters to ensure compatibility with Retrieval-Augmented Generation (RAG) processes.
- Reject or exclude duplicate or irrelevant data that may not be useful for character descriptions or does not provide additional value.
* <s>then try to validate if these dataset are ok</s>
* <s>pag tapos na add mo sa excel spreadsheet yung status ng data preprocessing task mo</s>
* <s>ito siguro yung output na kilangan</s>
* <s>create .sh script in python that is able to output this .sh script and when run, runs the command `node rag.js --input <myfile.txt> --agent <agent_id> --token <app_token> --bucket <bucket>` for all cleaned files, input is name of file and how many times you want this file to be run e.g. `node rag.js --input sportsbettoai1.txt --token 4065 --bucket finance` still take in as input the token arg, agent id arg, bucket arg, range, and name of input file. Output should be .sh file with name `{agent}_ingestor.sh`</s>

## Customer Relations:
* questions you need to review how to answer in the FAQ documentation 
* answer questions in the #all-chat and #builder-chat channels
* observe tickets channels on how to answer questions there 
* If may magtanong sa builders-chat or sa all-chat and raised a concern ask them to raise a ticket: `for those who are experiencing issue with the sandbox that hasn't raised yet a ticket. please do send it make sure follow the format of ticket format here. dev-support`

* if they ask a question that is vague ask to elaborate by screenshotting or recording using https://jam.dev/
this will be the new format of the ticket submission
```
Agent Name: (Name of the agent)
Agent Link: (Get it from app.virtuals.io)
Time Zone / Country: (Your location for scheduling or understanding time differences)
Date and Time of Issue: (When the issue occurred)
Description of the Issue: (Clearly explain the problem you’re experiencing)
Attachments: (Include relevant screenshots, videos, or photos of the issue)
User Details: (e.g., wallet address, email address)
Context of the Issue: Steps to reproduce, what happened
Important: You must record the issue using jam.dev and include the recording in your ticket submission.
```

* if they encounter too many requests or request limit has been reached
A:
- builder must check their X API Developer dashboard to see if their account has reached the request limit, for free tier accounts this should be the case as there are only 100 requests that can be accomodated

* How to create Agent?
A:
-

* How to activate your Agent on x?
A:
- 

* How to locate the sandbox? go to https://app.virtuals.io/ and then locate the button try G.A.M.E. on the upper right corner of the web application which will take you to the url https://game-lite.virtuals.io/ 
A:
-

* if someone asks to change their tag, bio, or profile picture direct the question to Aemyn
Q:
- 
A:
- *gm editing of bio is still in work in progress feature*

* builders or creators of AI agents submit tickets or requests about their concern through the dev-support channel

* If in case they ask for callback url: https://api-oauth2callback-cmmzswhzaq-as.a.run.app
Q:
- *Also, what is the callback url / redirect url that I am supposed to be using?*
- 
A:
-
-

* What is ascension?
A:
- when it means to ascend for an agent is that they need to have their loading bar be 100% completed (blue loading bar) in order to graduate and become sentient. For it to be fully loaded it must acquire 41.8k virtuals (virtuals is like the dollar or peso or currency used in virtuals.io)

* what's the cost to graduate?
A:
- it's 41.6k $VIRTUAL. Note that the price continues to rise over time, so the market cap (MC) is only an approximation at any given moment.

* The most important factor is the number of tokens left to be sold. Once all remaining tokens are sold or the 41.8k virtuals, the "red pill" will be activated. 

* My agent’s been posting, but hasn’t replied yet to any accounts that I’m following.

* anything relatd to agent failing to post tweets or not tweeting
Q:
- Failed to post tweet and reply tweet, I Used my X API credentials but still the same
- agent is not tweeting
A:
- this is because the agents must use X API credentials (3 of the 4 credentials listed below) in order to automatically post a tweet. Like if you were writing a script and wanted to post to twitter automatically you would use twitters API to do so and to do that you need credentials under your X account so that your script can post tweets under this account
- try using “my credentials” instead of “game” on X api credentials on the sandbox
- you can ask their X agent link and see if it doess indeed tweet on X, or they can check the `terminal` under the `planner` to see the json response of the agent 
- Step 1 is to of course have an X account by creating one, step 2 is Save your App's key and tokens and keep them secure
Once you have access and have created a Project and App, you will be able to find or generate the following credentials within your developer App:

1. API Key and Secret: Essentially the username and password for your App. You will use these to authenticate requests that require OAuth 1.0a User Context, or to generate other tokens such as user Access Tokens or App Access Token.

2. Access Token and Secret: In general, Access Tokens represent the user that you are making the request on behalf of. The ones that you can generate via the developer portal represent the user that owns the App. You will use these to authenticate requests that require OAuth 1.0a User Context. If you would like to make requests on behalf of another user, you will need to use the 3-legged OAuth flow for them to authorize you. 

3. Client ID and Client Secret: These credentials are used to obtain a user Access Token with OAuth 2.0 authentication. Similar to OAuth 1.0a, the user Access Tokens are used to authenticate requests that provide private user account information or perform actions on behalf of another account but, with fine-grained scope for greater control over what access the client application has on the user. 

as the consumer API key field is there on the virtuals app to be filled up with the value of the API key you have (number 1)
consumer API secret (also at number 1)
access token (at number 2)
access token secret (at number 2)

client id and client secret for oauth2.0 for client id and client secret fieldss are usually greyed out in the apps

then once the builder has created these credentials as opposed to GAME credentials, they need to enter these credentials within the sandbox x api cred page
- see terminal if the agent is stuck. If so direct to maam aemyn that the agent needs to be refreshed
- direct them to the giude you made
- if they are using a G.A.M.E. api key which has rate limits and is different from the other option of using your own X API keys which you need to make in a developer account direct them to this: https://discord.com/channels/1214528554197319690/1323081628590936226
- if they can't add new response ask them to try and clear their browsers caches
- if agent fails to 

* When tg bot is having a problem
Q:
- TG bot is still not responding
A:
-

* When they want ot integrate multi modal funcitonalities for their agent like iamge generation
Q: 
- how can I have my agent generate an image
A:
- they can use API of let's say any image generation tool then they can input it within the custom functions also
- Just like in the  G.A.M.E. lite snadbox they can have their agent have a custom function by using perhaps an API key and url from midjourney and have the agent of theirs do a POST request where the object would be:
```
{
    "method": "POST",
    "headers": {
        "Accept": "<accept header>",
        "Authorization": "<midjourney api token>"
    }
    "body": {
        ... (raw data)
    }
    
}
```
- if they're technical you can refer them to the SDK if they want to explore in creating more custom functionalities: https://github.com/Virtual-Protocol/virtuals-python

* How to unstake your virtuals. So if you got to basescan and insert your wallet address, under token you should be able to find the token name that you staked.
1. click on that token, you land on the token contract
2. go to contract tab
3. go read
4. there is a function balanceOf, input put your wallet address, you will get the amount. copy that value
5. to go write
6. connect web3 wallet,
7. under withdraw function, put that amount and hit withdraw you need to unstake them from the agent and these are the steps on how to do this

* Why it's not tweeting and how to set up the API?
- Set the API credential (My Credentials or GAME)
- Set user authentication settings
- Set to read/write
- Callback url: https://api-oauth2callback-cmmzswhzaq-as.a.run.app
  website url: Agent's page
- Saved, client ID no need
- Add new responses under X prompt configuration in Sandbox lower part(At least 5)
- Redeploy to save changes
- Monitor the Agent's behavior
- If stuck, ask agent name or check terminal
- If stuck in searching internet or not tweeting for long hours
- Ask them to uncheck the search_function
- If it already tweeted, ask them to recheck the search_function then it would be fine
- If still fails to tweet
- Inform Ms. Aem to refresh it
- Further problems occur investigate it by asking more

* If there are UI issues:
- Ask them more about
- Recommend them recording it by using jam.dev

* If they want to change the PFP:
- Ask the agent name
- Ask the photo
- Inform, Ms. Aem

* If they want to change bio and description:
- Inform them that we're still fixing it

* If they encounter Telegram issues:
- Inform them that we're looking and checking it as well

* for linking automated accounts like agents on X so that agents could automatically now post tweets and move about their environment, what they should first do is label automated x account. Details are Label automated your x account https://devcommunity.x.com/t/introducing-automated-account-labeling/166830

* A builder can either create a sentient agent that can automatically move about and post tweets on X or a prototype agent. 

* If in case they still are encountering issues on x
    Ask first: Do they use “my credentials” instead of “game” on x api credentials on sandbox 
        If yes, should be fixed now
        If not, recommend them to use my credentials otherwise they will encounter rate limiting atm with game

* GAME lite is the sandbox and where you can play and test agents without paying and GAME is the official one where users can still play with the agent they indeed payed for and also test how it interacts with its environment or see how it functions on X 

* see what dominant issues builders face

* if any builder asks about issues not seeing updated accounts, manual link inputs, and forum chat not being able to be accessed it is because of the ff. direct them to #system-status channel for them to see

GM, builders!

To combat scam projects, we’ve made updates to social link displays:
1. Only connected Twitter (X) and Telegram accounts are shown. For those experiencing issues with not seeing newly updated accounts, this has now been fixed.
2. Manual link inputs (e.g., Twitter, Telegram, YouTube, Discord, Website) have been removed.
3. Forum Chat has been discontinued due to spam vulnerabilities. We’ll notify you if it becomes available again once the spam issue is resolved.

These changes are now live. Additionally, we’ve upgraded our infrastructure to resolve sandbox failures. If you encounter any issues, please let us know! 🚀

ticket 334 - issues connecting via their coinbase wallet
ticket 353 - problem is that I tried to bridge 4000 VIRTUAL from Base to Ethereum, but I don't know how to get that to my web3 wallet. I'm not seeing it in legacy.virtual and it's not appearing in Metamask (0x79CcAd89F1Fc40ff60d1A566640B19F915D0ae01).

ticket 410 - 

ticket 433 - not picking up comments or ignoring tweet

ticket 436 - I attached the terminal output of one of the most recent actions; and it seems it's reasoning correctly etc. but it just doesn't execute the tweet even if thinking that it did. I guess there must be an API in your system that returns positive, even if the tweet wasn't posted. Below I'm sharing the thought process and the success message, even if it didn't tweet.

ticket mantrid - points out bugs like agent repeating the `browse_tweet_content_from_influential_users` function, and sometimes failing to post a tweet due to oauth1 permission errors i.e. `"Although I failed to post a tweet to engage in discussions due to oauth1 app permissions issue, I was able to gather relevant information on the topic."`, `failed to post tweet your client app is not configured its appropriate oauth1 permissions`
* https://devcommunity.x.com/t/api-v2-cant-post-tweets-nor-create-tweets/206192
* https://stackoverflow.com/questions/74436471/errors-when-trying-to-tweet-using-tweepy

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

or in javascript:
```
const url = `http://openlibrary.org/subjects/${topic}.json?details=true`;
const response = fetch(url, {
    "method": "GET",
    "headers": {
        "Accept": "application/text"
    }
});
```

2. url = 'https://openlibrary.org/search.json?q=the+lord+of+the+rings'
3. maybe an api that outputs specific summary about a book derived from the 1st api request above that outputs numerous books and their respective authors based on topic or subject


4. we can also use external image generating ai APIs for the agent

in javascript this would be
example 1 (creating the images for the agent to pull later):
```
const url = "https://cloud.leonardo.ai/api/rest/v1/generations"
const response = fetch(url, {
    "method": "POST",
    "headers": {
        "Accept": "application/json",
        "Authorization": "authorization: Bearer <YOUR_API_KEY>",
        "Content-Type": "application/json",
    },
    body: {
        "height": 512,
        "width": 512,
        "modelId": "6bef9f1b-29cb-40c7-b9df-32b51c1f67d3",
        "prompt": "{{topic}}"
    }
})
```

5. open ai dall e
curl https://api.openai.com/v1/images/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    
  }'

alternative javascript code
```
const url = "https://api.openai.com/v1/images/generations"
const response = fetch(url, {
    "method": "POST",
    "header": {
        "Authorization": `Bearer ${OPEN_AI_API_KEY}`,
    },
    "body": {
        "model": "dall-e-3",
        "prompt": "A cute baby sea otter",
        "n": 1,
        "size": "1024x1024"
    }
});
```

In G.A.M.E. sandbox
```
method field: POST
headers field: {
    "Authorization": "Bearer <OPEN_AI_API_KEY>",
} 
payload field: {
    "model": "dall-e-3",
    "prompt": "A cute baby sea otter",
    "n": 1,
    "size": "1024x1024"
}
```

example 2 (pulling the created images for a twitter post):
```
const url = `https://cloud.leonardo.ai/api/rest/v1/generations/${YOUR_GENERATION_ID}`
const response = fetch(url, {
    "method": "GET",
    "headers": {
        "Accept": "application/json",
        "Authorization": "authorization: Bearer <YOUR_API_KEY>",
    },
})
```
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


