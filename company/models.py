from django.db import models

# Create your models here.
class company_detail(models.Model):
	Name = models.CharField(max_length=200)
	description = models.TextField(blank=False,null=False)
	CTC =models.DecimalField(decimal_places=2, max_digits=10000)
	Profile = models.TextField(default='software')
	description = models.TextField(blank=False,null=False)
	
	def __str__(self):
		return str(self.Name)