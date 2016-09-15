import json
from django.http import HttpResponse
from django.shortcuts import render

from notification.aws import AmazonSQS
from notification.models import Notification


def get_notification(request):
    sqs = AmazonSQS()
    messages = sqs.get_messages()
    messages = messages if messages else []
    for message in messages:
        message_dict = message.get_body()
        message_dict = json.loads(message_dict)
        notification = Notification()
        notification.message = message_dict.get('message')
        notification.type = message_dict.get('type')
        notification.owner = message_dict.get('owner')
        notification.meta_model = Notification.MODEL_NODE
        notification.meta_instance = message_dict.get('meta_instance')
        notification.meta_human_readable = message_dict.get('meta_human_readable')
        notification.save()
    if messages:
        total_messages = len(messages)
        response_msg = '%s notification(s) received' % total_messages
        return HttpResponse(response_msg)
    else:
        return HttpResponse('no notification received')