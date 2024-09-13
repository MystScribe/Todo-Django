from django.db import models

class TodoModel(models.Model):
    title = models.CharField(max_length=150)
    textarea = models.TextField()
    todolist = models.CharField(max_length=150)
    Done = models.BooleanField()
    created = models.DateTimeField()



    def __str__(self):
        return f'{self.title}'
