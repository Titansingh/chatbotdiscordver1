import discord
import requests
import json
import random
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import UbuntuCorpusTrainer

prabh = 745379486077288499
yash = 694596381150806056



badwords = ['chala ja bsdk',
            'Aand mand ka tola abh tune message kiya toh tu bhen ka loda',
            'Chaar Chawani ghode pe, yash mere lode pe',
            'yash  hamara neta hai, sabh ko apni gaand deta hai',
            'Oye bhsdk ke teri kah ke le lunga, aur Tera message teri hi gaand m de dunga']

my_bot = ChatBot(
    name='Titan',
    logic_adapters=['chatterbot.logic.MathematicalEvaluation', 'chatterbot.logic.BestMatch'])


#ubuntu_corpus_trainer = UbuntuCorpusTrainer(my_bot)
corpus_trainer = ChatterBotCorpusTrainer(my_bot)

#ubuntu_corpus_trainer.train()
corpus_trainer.train(
    "chatterbot.corpus.english",
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations"
)

 


client = discord.Client()


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)


def get_meme():
    response1 = requests.get("https://meme-api.herokuapp.com/gimme")
    json_data = json.loads(response1.text)
    quote1 = json_data['url']
    return(quote1)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author.id == client.user.id:
        return

    msg = message.content
    if message.author.id == (yash or prabh):
        await message.channel.send(random.choice(badwords))
    
    else:
        

        if msg.startswith('$hello'):
            await message.channel.send('Hello!')

        if msg.startswith('!'):
            recieved_msg = message.content
            print(recieved_msg)
            
            await message.channel.send(my_bot.get_response(recieved_msg[1:]))
            

        if msg.startswith('$inspire'):
            quote = get_quote()
            await message.channel.send(quote)
            print('quote send')
        if msg.startswith('$meme'):
            quote1 = get_meme()
            await message.channel.send(quote1)
            print('meme send')

client.run('')