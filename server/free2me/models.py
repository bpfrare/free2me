from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Resource(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Using(models.Model):
    user = models.ForeignKey(Users)
    resource = models.ForeignKey(Resource)

class Waiting(models.Model):
    user = models.ForeignKey(Users)
    resource = models.ForeignKey(Resource)
    time = models.DateTimeField(auto_now_add=True,)

    def __unicode__(self):
        return self.time

class Relationship(models.Model):
    user = models.ForeignKey(Users)
    resource = models.ForeignKey(Resource)


