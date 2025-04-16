from bson import ObjectId
from djongo import models

class User(models.Model):
    _id = models.ObjectIdField(default=ObjectId, primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

class Team(models.Model):
    _id = models.ObjectIdField(default=ObjectId, primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    members = models.JSONField()

class Activity(models.Model):
    _id = models.ObjectIdField(default=ObjectId, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=255)
    duration = models.DurationField()

class Leaderboard(models.Model):
    _id = models.ObjectIdField(default=ObjectId, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()

class Workout(models.Model):
    _id = models.ObjectIdField(default=ObjectId, primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
