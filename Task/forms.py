from django import forms
from .models import Task

class DateInput(forms.DateInput):
	input_type = 'date'
#form to handle both add and edit of the task
class TaskDetailForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = [
			'task_name',
			'task_desc',
			'status',
			'priority',
			'due_date'
		]

		widgets = {'due_date' : DateInput()}
	
	def __init__(self, *args, **kwargs):
		super(TaskDetailForm, self).__init__(*args, **kwargs)
		self.fields['task_name'].widget.attrs.update({'class' : 'form-control', 'onchange' : 'elastic(this.value)'})
		self.fields['task_name'].widget.attrs['required'] = True
		self.fields['task_desc'].widget.attrs.update({'class' : 'form-control'})
		self.fields['status'].widget.attrs.update({'class' : 'form-control'})
		self.fields['status'].widget.attrs['required'] = True
		self.fields['priority'].widget.attrs.update({'class' : 'form-control'})
		self.fields['priority'].widget.attrs['required'] = True
		self.fields['due_date'].widget.attrs.update({'class' : 'form-control'})

#form to handle search of task based on due date
class TaskFilter(forms.Form):
	search_date = forms.DateField(required=False)