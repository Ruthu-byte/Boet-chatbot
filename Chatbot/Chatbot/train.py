from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot
import chatterbot
from chatterbot import response_selection

chatbot = ChatBot("Boet", preprocessors=['chatterbot.preprocessors.clean_whitespace'], logic_adapters=[
    {'import_path': 'chatterbot.logic.BestMatch',
     'statements_comparison_function': "chatterbot.comparisons.levenshtein_distance",
     'response_selection_method': chatterbot.response_selection.get_first_response
     }]
                  )

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english.AI3")
