from django.db import models

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=50)
	password = models.CharField(max_length=25)
	b_day = models.DateField()
	loc = models.CharField(max_length=50)
	bio = models.TextField()


	def __unicode__(self):
		return '%s.- %s' % (self.id, self.name,)

	class Meta:
		ordering = ['-name']

class Tweet(models.Model):
	status = models.CharField(max_length=140)
	user = models.ForeignKey('User', related_name='tweets')
	created_at = models.DateTimeField(auto_now_add=True)