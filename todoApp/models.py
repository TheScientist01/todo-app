from django.db import models

class Task(models.Model):
    title=models.CharField(max_length=255, blank=True)
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)
    is_complete=models.BooleanField(default=False)

    def __str__(self):
        return self.title