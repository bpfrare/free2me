from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Resource(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Relationship(models.Model):
    user = models.ForeignKey(User)
    resource = models.ForeignKey(Resource)

    def __unicode__(self):
        return self.resource.name + "-" + self.user.name

class Using(models.Model):
    relationship = models.ForeignKey(Relationship)
    time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.relationship.resource.name + "-" + self.relationship.user.name

class Waiting(models.Model):
    relationship = models.ForeignKey(Relationship)
    time = models.DateTimeField(auto_now_add=True,)

    def __unicode__(self):
        return self.relationship.resource.name + "-" + self.relationship.user.name

