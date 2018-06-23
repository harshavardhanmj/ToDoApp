from django.db import models

# Create your models here.
class Task(models.Model):
	status_choices = (('ToDo', 'ToDo'), ('Doing', 'Doing'), ('Done', 'Done'))
	priority_choices = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'))
	task_name = models.CharField(null=True,blank=True,max_length=320)
	task_desc = models.CharField(null=True,blank=True,max_length=1000)
	status = models.CharField(max_length=300,null=True,blank=True,choices=status_choices)
	priority = models.CharField(null=True, blank=True,max_length=100,choices=priority_choices,default=priority_choices[2][0])
	due_date = models.DateField(auto_now=False, auto_now_add=False,null=True)

	def __str__(self):
		return self.task_name

	def get_absolute_url(self):
		return reverse('TaskUpdateView', kwargs={'pk': self.pk})

