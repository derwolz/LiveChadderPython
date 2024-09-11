from django.contrib import admin

# Register your models here.
from .models import Message, Thread, Client

admin.site.register(Message)
admin.site.register(Thread)
admin.site.register(Client)