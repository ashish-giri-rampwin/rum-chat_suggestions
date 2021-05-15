from chatterbot import ChatBot,filters
from chatterbot.trainers import ListTrainer
from data import greetings


# Create a new instance of a ChatBot
bot = ChatBot(
    'Example Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    filters=[filters.get_recent_repeated_responses],
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.5
        }
    ]
)

trainer = ListTrainer(bot)
# Train the chat bot with a few respo
for i in greetings:
    trainer.train(i)

# Get a response for some unexpected input
response = bot.get_response('good morning')
print(response)
response = bot.get_response('hello')
print(response)
response = bot.get_response('hello')
print(response)
response = bot.get_response('hello')
print(response)
response = bot.get_response('hello')
print(response)
response = bot.get_response('hello')
print(response)
response = bot.get_response('hello')
print(response)
response = bot.get_response('hello')
print(response)
response = bot.get_response('hello')
print(response)