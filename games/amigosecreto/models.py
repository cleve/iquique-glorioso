from django.db import models
from django.conf import settings


class Game(models.Model):
    '''Game instance
    '''
    title = models.CharField(max_length=100)
    creation = models.DateTimeField('Creation time')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title


class Friend(models.Model):
    '''Every person in the game
    '''
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.full_name
