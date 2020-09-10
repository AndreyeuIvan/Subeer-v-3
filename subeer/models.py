from django.db import models
from django.utils.timezone import now


# Create your models here.
class Serial(models.Model):
	'''all information regarding Serials, connected with episodes, categories'''
	Rating_CHOICES = (
    (1, 'Poor'),
    (2, 'Average'),
    (3, 'Good'),
    (4, 'Very Good'),
    (5, 'Excellent')
	)

	is_favorite = models.IntegerField(choices=Rating_CHOICES, default=1)
	title = models.CharField(max_length=100)
	description = models.TextField('Description')
	slug = models.SlugField(max_length=250, blank=True)
	url = models.URLField(max_length=133)
	created = models.DateTimeField(default=now())
	updated = models.DateTimeField(default=now())
	poster = models.ImageField("Постер", upload_to="static/img/serial", blank=True)
	#Season = BigIntegerField(default=1)
	#rating= write your own
	#publish =
	#tag = 
	#author = 

	def __str__(self):
		return self.title


class Like(models.Model):
	serial = models.ForeignKey(
		Serial, on_delete=models.CASCADE,
	)


class Episode(models.Model):
	'''Store title of episode, url to download, season, authors(regarding studio of translation)'''
	#poster = models.ImageField("Постер", upload_to="static/img/episode")
	title = models.CharField(max_length=100)
	serial_id = models.ForeignKey(
		Serial, verbose_name="Serial_id", on_delete=models.SET_NULL, null=True
	)
	url = models.URLField(max_length=133, blank=True)
	created = models.DateTimeField(default=now())
	updated = models.DateTimeField(default=now())
	#season =
	#author_of_release =

	def __str__(self):
		return self.title


class Category(models.Model):
	pass


class Opinion(models.Model):
	Login = models.CharField(max_length=100, blank=True)
	Description = models.TextField(blank=True)
	date_opinion = models.DateTimeField(auto_now=True)



class Comment(models.Model):
	pass