# -*- coding: UTF-8 -*-
import json
from django.core.management.base import BaseCommand
from notification.aws import AmazonSQS


class Command(BaseCommand):
    args = ''
    help = ''

    def handle(self, *args, **options):
        sqs = AmazonSQS()
        message = {
            'message': 'New Message',
            'type': '1',
            'owner': 'Diego',
            'meta_instance': 'InstanceOne',
            'meta_human_readable': 'MetaDataHumanReadeable'
        }
        queue = sqs.get_queue()
        if not queue:
            queue = sqs.create_queue()
        sqs.send_message(json.dumps(message), queue)