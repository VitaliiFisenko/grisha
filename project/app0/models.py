from django.db import models

class MyGroup(models.Model):
	name = models.CharField(max_length=20)
	surname = models.CharField(max_length=20, default='')
	point = models.IntegerField(default=60)
	def __str__(self):
		return self.surname
