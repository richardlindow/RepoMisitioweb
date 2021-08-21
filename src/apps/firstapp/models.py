from django.db import models

# Create your models here.


class FirstClass(models.Model):
	columna1 = models.CharField(max_length=255)
	columna2 = models.CharField(max_length=255)

	class Meta:
		db_table = 'firstapp'
'''
	def __str__(self):
		return self.columna1
'''

