from django.db import models

# Create your models here.
class Conversation(models.Model):
    user_input = models.TextField()
    bot_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_input} -> {self.bot_response}"

    
