from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField('auth.User')
    name = models.CharField(max_length=100, blank=True)
#    image = models.ImageField(max_length=100, blank=True)
    birthday = models.DateField(null=True)
    location = models.CharField(max_length=100, blank=True)
    bio = models.CharField(max_length=140, blank=True)
    private = models.BooleanField()
    #follower = models.ManyToManyField('UserProfile', related_name="followings_relation")
    #followed = models.ManyToManyField('UserProfile', related_name="followings_relation")

    def __unicode__(self):
        return self.name

class Tweet(models.Model):
    owner = models.ForeignKey('UserProfile')
    status = models.CharField(max_length=140)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']
"""
    def __unicode__(self):
        return '%s.- %s %d ' % (self.id, self.status, self.date)
"""
    
