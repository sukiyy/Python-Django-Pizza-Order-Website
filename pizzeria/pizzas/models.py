from django.db import models
# Create your models here.

class Pizza(models.Model):
	
	 ''' Define a model Pizza with a field called name, 
	 which will hold name values such as Hawaiian and Meat Lovers. '''
	 name = models.CharField(max_length=30)
	 def __str__(self):
		 '''Return a string representation of the model.'''
		 return self.name
		 
class Topping(models.Model):
	pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class Entry(models.Model):
	pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField (auto_now_add=True )
	class Meta:
		verbose_name_plural = 'entries'
	
	def __str__(self):
		return self.text[:50]+"..."
