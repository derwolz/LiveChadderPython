from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from .models import Thread, Message
from django.contrib.auth.models import User
import json
import uuid
from django.shortcuts import render

@method_decorator(csrf_exempt, name='dispatch')
class ChatAPI(View):
    def get(self, request):
        session_id = request.COOKIES.get('chat_session_id')
        if not session_id:
            thread = Thread.objects.create()
            session_id = str(thread.uid)
        else:
            try:
                thread = Thread.objects.get(uid=uuid.UUID(session_id))
            except Thread.DoesNotExist:
                thread = Thread.objects.create()
                session_id = str(thread.uid)
   
        messages = [
            {"id": msg.id,"sender":str(msg.sender), "content": msg.content, "timestamp": msg.timestamp.isoformat()}
            for msg in thread.messages.order_by('timestamp')
        ]

        response = JsonResponse({"messages": messages, "thread_id": str(thread.uid)})
        response.set_cookie('chat_session_id', session_id, max_age=86400)
        return response

    def post(self, request):
        data = json.loads(request.body)
        session_id = request.COOKIES.get('chat_session_id')
        print(data)
        try:
            thread = Thread.objects.get(uid=uuid.UUID(session_id))
        except Thread.DoesNotExist:
            thread = Thread.objects.create()
        user = None
        try:
            user = User.objects.get(username=data['sender'])
        except User.DoesNotExist:
            return JsonResponse({"status": "error", "message": "User not found"}, status=404)
        message = Message.objects.create(
            sender=user,
            content=data.get('message')
        )
        thread.messages.add(message)
        
        response = JsonResponse({
            "status": "success",
            "message": {
                "id": message.id,
                "content": message.content,
                "timestamp": message.timestamp.isoformat(),
                "sender": str(message.sender),
            }
        })
        response.set_cookie('chat_session_id', str(thread.uid), max_age=86400)
        return response
    
def chat_view(request):

    return render(request, 'LiveChat/base.html')