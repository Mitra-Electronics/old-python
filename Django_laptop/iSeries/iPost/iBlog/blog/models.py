from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

choices = [('Technology', 'Technology'), ('Sports', 'Sports'), ('Entertainment', 'Entertainment'), ('Coding', 'Codings')]

class category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

class post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    category = models.CharField(max_length=255, choices=choices)
    date_of_creation = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('article', args=(str(self.id)))
