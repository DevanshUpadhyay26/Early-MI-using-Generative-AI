from django.db import models

# Create your models here.

class ChatHistory(models.Model):
    user_input = models.TextField()
    generated_output = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class ChatSummary(models.Model):
    history = models.TextField()

class MedicalRecord(models.Model):
    record = models.TextField()
