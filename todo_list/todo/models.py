from django.db import models

# Create your models here.
class Todo(models.Model):
    class Meta:
        db_table = 'todos'
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)