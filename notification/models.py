from django.db import models

# Create your models here.
class Notification(models.Model):

    MODEL_NODE = '1'
    ANOTHER_NODE = '2'
    META_MODEL_CHOICES = (
        (MODEL_NODE, 'Model Node'),
        (ANOTHER_NODE, 'Another Node')
    )

    message = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    meta_model = models.CharField(choices=META_MODEL_CHOICES, max_length=100)
    meta_instance = models.CharField(max_length=100)
    meta_human_readable = models.CharField(max_length=100)
