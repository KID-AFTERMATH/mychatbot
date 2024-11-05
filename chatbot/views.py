from django.shortcuts import render

# Create your views here.

from .models import Conversation
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('LotteryBot')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

def chat_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        bot_response = chatbot.get_response(user_input)
        Conversation.objects.create(user_input=user_input, bot_response=str(bot_response))
        return render(request, 'chatbot/chat.html', {'bot_response': bot_response, 'user_input': user_input})
    return render(request, 'chatbot/chat.html')
