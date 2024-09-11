from django.db import models
from django.contrib.auth.models import User 
import uuid

# Create your models here.
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Client(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField()
    phone_number = models.TextField()

class Thread(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    messages = models.ManyToManyField(Message, related_name='threads')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='threads', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.client:
            return f"Thread for {self.client.first_name} {self.client.last_name}"
        return "unitiated thread"
