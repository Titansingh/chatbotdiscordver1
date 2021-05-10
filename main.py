import discord
import requests
import json
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer


my_bot = ChatBot(
    name='PyBot',
    read_only=True,
    logic_adapters=['chatterbot.logic.MathematicalEvaluation', 'chatterbot.logic.BestMatch'])

small_talk = [
    'hi there!',
    'hi!',
    'how do you do?',
    'how are you?',
    'i\'m cool.',
    'fine, you?',
    'always cool.',
    'i\'m ok',
    'glad to hear that.',
    'i\'m fine',
    'glad to hear that.',
    'i feel awesome',
    'excellent, glad to hear that.',
    'not so good',
    'sorry to hear that.',
    'what\'s your name?',
    'i\'m pybot. ask me a math question, please.'
]


math_talk_1 = [
    'pythagorean theorem',
    'a squared plus b squared equals c squared.'
]
math_talk_2 = [
    'law of cosines',
    'c**2 = a**2 + b**2 - 2 * a * b * cos(gamma)'
]


list_trainer = ListTrainer(my_bot)

#for item in (small_talk, math_talk_1, math_talk_2):
#    list_trainer.train(item)

corpus_trainer = ChatterBotCorpusTrainer(my_bot)
corpus_trainer.train('chatterbot.corpus.english')

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
