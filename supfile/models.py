from django.db import models

# Create your models here.
class MyRoom():
    def __init__(self, userroom, room):
        self.userroom = userroom
        self.room = room

class UserAuthor():
    def __init__(self, list, roletypeid, roletypename):
        self.userlist = list
        self.roletypeid = roletypeid
        self.roletypename = roletypename
