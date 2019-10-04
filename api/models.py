from django.db import models
from django.contrib.auth.models import User

class todofeed(models.Model):
    """This is the model for the todo list"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    # title = models.CharField(max_length=50)
    # body = models.TextField()
    # created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item
