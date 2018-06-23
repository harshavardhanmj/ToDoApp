from django_elasticsearch_dsl import DocType, Index
from .models import Task

posts = Index('posts')

@posts.doc_type
class TaskDocumnent(DocType):
	class Meta:
		model = Task
		fields = [
			'task_name',
			'task_desc',
			'status',
			'priority',
			'due_date'
		]