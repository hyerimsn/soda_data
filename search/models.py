from django.db import models

# Create your models here.
class Log(models.Model):
    person = models.CharField(max_length=5, null=True)
    status = models.CharField(max_length=20, null=True)
    ment = models.TextField(null=True)
    date = models.TextField(null=True)

    def __str__(self):
        return self.person

class News(models.Model):
    title = models.CharField(max_length=150)
    reporter = models.CharField(max_length=50)
    media = models.CharField(max_length=6)
    body = models.TextField()
    link = models.TextField()
    date = models.CharField(max_length=10)

    def __str__(self):
        return self.title