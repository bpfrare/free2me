from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=200)

class Resource(models.Model):
    name = models.CharField(max_length=200)

class Using(models.Model):
    user = models.ForeignKey(Users)
    resource = models.ForeignKey(Resource)

class Waiting(models.Model):
    user = models.ForeignKey(Users)
    resource = models.ForeignKey(Resource)
    time = models.DateTimeField(auto_now_add=True,)


class Relationship(models.Model):
    user = models.ForeignKey(Users)
    resource = models.ForeignKey(Resource)
    
    
