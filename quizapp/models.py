from django.db import models

# Create your models here.
# Database layer

class Question(models.Model):
    content = models.CharField(blank=False, max_length=200, help_text="Enter the question")

    def __str__(self):
        return self.content

class Answer(models.Model):
    content = models.CharField(max_length=100)
    correct = models.BooleanField(default=False, blank=False)

    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.content