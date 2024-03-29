from django.db import models
from django.contrib.auth.models import User


class Posts(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=25)
    director = models.CharField(max_length=50)
    actors = models.CharField(max_length=100)
    release_at = models.DateField()
    content = models.TextField()
    image = models.ImageField(
        upload_to='images/',
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
