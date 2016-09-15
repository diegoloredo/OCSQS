import boto
from django.conf import settings
from boto.sqs.message import Message


class AmazonSQS(object):

    QUEUE = 'queue'

    def __init__(self):
        self.connection = boto.connect_sqs(
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)

    def create_queue(self, queue_name):
        return self.connection.create_queue(queue_name)

    def send_notification(self, message, queue):
        m = Message()
        m.set_body(json_)
        return queue.write(m)

    def get_queue(self):
        return self.connection.get_queue(self.QUEUE)

    def get_queues(self):
        return self.connection.get_all_queues()

    def get_notifications(self):
        queue = self.get_queue()
        if not queue:
            queue = self.create_queue(self.QUEUE)
        return queue.get_messages()