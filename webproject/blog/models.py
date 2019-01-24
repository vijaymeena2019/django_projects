from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User #we also need author for each post and this will be a user who created
from django.urls import reverse											#the post. now our user is separate table. so 1st we need to import the
											#user model.now Posts model and User model(class) are going to have a
											#relationship since user are going to author post specificaly this is going
											#to be called one to many relationship because one user have multiple post
											#but post can have only one author and to do this in Django we use a 
											#foreign key and aurgument we pass in foreign key is the related table
											#and that will be User and we also need a second argument here called 'on_delete'
											#and this is need bcoz we need to tell Django what we want to do if user who created
											#this post gets deleted. now if the user created a post and user was deleted so if a 
											#user created post and then the user was deleted then we want to delete the post or
											# we set the author to none or what we want to do

# Create your models here.
class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)  #if user deleted then post also deleted but if user delete the post then it is not going to delete user.
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)  #here this is like default= timezone.now() but here we do not want to run function so we put like this.

	def __str__(self):
		return self.title

	def get_absolute_url(self):                           # now in our post model we will create that get absolute url method to tell Django who to find the url to any specific instance of a post
		return reverse('post-detail', kwargs={'pk':self.pk})								# return a path to specific post, revese will return full path as a string so that the full path that we want to get is the pathe to the 'post-detail', and it need a specific post with primary key so 'kwargs={'pk':self.pk}'