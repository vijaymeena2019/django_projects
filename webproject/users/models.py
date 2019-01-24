# from django.db import models
# from django.contrib.auth.models import User
# from PIL import Image  # form pillow import specifically image 

# class Profile(models.Model):
# 	user = models.OneToOneField(User, on_delete='CASECADE')   # creating one to one relationship with User model. #CASECADE means if user is delete then also delete the profile but is profile deleted then do not delete user 
# 	image = models.ImageField(default='default.jpg', upload_to='profile_pics')  #adding image field. we can also add another fields 

# 	def __str__(self): #adding dunder method . it means when profile pic display then how it can be diplay
# 		return f'{self.user.username} Profile'# without dunder str method anytime we print out a profile then it gona say profiel object and we need to more discriptive then at all 

# 	def save(self): #this save method is the method that gets run after our model is saved. it is a method that already
# 	                #exist in our parent class but we are crating our own so that we can add some functionality
# 	    super().save()   #we are going to run the save() mathod to our parent class and we do this by 'super()'. so that parent class save method would have been run when we saved an instace of this profile
# 	    					#if we uploaded a large image then that should have saved it but now we are going to grab the image that it is saved and resize it so to do this we need to import pillow library

# 	    img = Image.open(self.image.path)		#so this will open the image of the current instance and now we are going to resize that so we want to specity what size that we want our image to be (125px or upto 300px)
	    
# 	    if img.height > 300 or img.width > 300: #condition
# 	    	output_size = (300, 300)  #it is tuple
# 	    	img.thumbnail(output_size) #resize it and save it
# 	    	img.save(self.image.path) #save it back to same loction to override the proviour big image 



from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kawrgs):
        super().save( *args, **kawrgs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)