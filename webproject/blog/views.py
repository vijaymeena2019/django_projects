from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView , DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin  

# Create your views here.

# posts = [ 
# 	{
# 	'author':'vijay',
# 	'title':'i am vijay',
# 	'content': 'This is a content from vijay meena',
# 	'date_posts': '27 nov 2001'
# 	},
# 	{
# 	'author':'vijay',
# 	'title':'i am vijay',
# 	'content': 'This is a content from vijay meena',
# 	'date_posts': '27 nov 2001'
# 	}
# ]

def home(request):
	posts = models.Post.objects.all()
	return render(request,'blog/home.html',{'posts':posts})

class PostListView(ListView): #PostListView which inherit form ListView and within our ListView we need to create a variable
	model = Post #what model to query in order to create the list and in this case we want it to be all our posts             #called model and this will tell our list view what model to query in order to create the list
	template_name= 'blog/home.html'    #<app>/<model>_<viewtype>.html   # lastly even this change in place this is not going to work just yet because it does not know what we want the variable to be named in our template that we are going to be looping over 
	context_object_name = 'posts'  # *posts* = models.Post.objects.all()                            # and also need little bit more to do # and in this case we want it to be all our posts so we will set that model equal to post
	ordering = ['-date_posted']	#create new attribute				# in order to use this list view we can open up our blog urls.py module and say that we want to 
								# use this post list view instead of our current home funtion so within our blog app let's open up
								# those urls and instead of using 'views.home'  we are going to use our post list view so let me actually
								#import that directly so i will keep the view (go to urls.py)

class PostDetailView(DetailView): 
	model = Post  
#now lets create the url pattern 



class PostCreateView(LoginRequiredMixin, CreateView):  #so this is going to be a view with a form where we create a new post so the only other thing we need to provide are the fields that we want to be in that form
	model = Post 
	fields = ['title','content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):  
	model = Post 
	fields = ['title','content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object() #get the post currently tring to update
		if self.request.user == post.author:
			return True
		return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView): # must be left from DeleteView and we also copy the test fn
	model = Post
	success_url = '/'  #add success_url attribute with address of home page

	def test_func(self):
		post = self.get_object() #get the post currently tring to update
		if self.request.user == post.author:
			return True
		return False


def about(request):
	return render(request,'blog/about.html',{'title':'MyTitle'})

