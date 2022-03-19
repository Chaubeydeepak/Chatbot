from chatterbot.chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot("My Bot")

data = [
    'hello',
    'hi there !',
    'what is your name ?',
    'My name is Bot.',
    'How are you ?',
    'i am doing good',
    'thank you',
    'In which language you talk',
    'I mostly talk in english'
]

trainer = ListTrainer(bot)

#now training the bot with help of trainer

trainer.train(data)

answer=bot.get_response("what is your name ?")
print(answer)