from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE,default="",)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']
