from django.db import models

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    division = models.CharField(max_length=100)
    wins = models.IntegerField()
    losses = models.IntegerField()

    def __str__(self):
        return self.name


class Player(models.Model):
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name='players')
    name = models.CharField(max_length=100, default='no name')
    age = models.IntegerField(null=True)
    position = models.CharField(max_length=100, default='no position')
    passes_attempted = models.IntegerField(null=True)
    passes_completed = models.IntegerField(null=True)
    tackles = models.IntegerField(null=True)
    goals = models.IntegerField(null=True)
    injured = models.CharField(max_length=100, default='not injured')

    def __str__(self):
        return self.name
