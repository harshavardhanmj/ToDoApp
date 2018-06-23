from django.shortcuts import render
import datetime
from .models import Task
from .forms import TaskDetailForm, TaskFilter
from .documents import TaskDocumnent
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView

# Create your views here.
#Class to handle listing of task and its details on home screen, and to also search task based on due date
class TaskListView(FormView):
    template_name = "TaskList.html"
    form_class = TaskFilter
    success_url = '/'

    def post(self, request, *args, **kwargs):
    	object_list = Task.objects.all()
    	TaskFilter_form = self.form_class(request.POST)
    	if TaskFilter_form.is_valid():
    		search_date = request.POST.get("search_date")
    		if search_date:
    			object_list = Task.objects.filter(due_date = search_date)
    			if not object_list:
    				object_list = "No Data To Display"
    		else:
    			object_list = Task.objects.all()
    	return self.render_to_response(self.get_context_data(object_list1=object_list))

    def get_context_data(self, **kwargs):
    	currentDate = datetime.datetime.now().date()
    	kwargs['object_list'] = Task.objects.all()
    	kwargs['currentDate'] = currentDate
    	return super(TaskListView, self).get_context_data(**kwargs)

#Class to update the task details and also perform elastic search on editing the task
class TaskUpdateView(UpdateView):
    template_name = "TaskForm.html"
    queryset = Task.objects.all()
    form_class = TaskDetailForm
    success_url = "/"

    def get_context_data(self, **kwargs):
    	kwargs['Action'] = "Edit"
    	posts = TaskDocumnent.search().query("match_all")
    	kwargs['posts'] = posts
    	return super(TaskUpdateView, self).get_context_data(**kwargs)

#Class to add the task details and also perform elastic search on adding the task
class TaskCreateView(CreateView):
    template_name = "TaskForm.html"
    form_class = TaskDetailForm
    success_url = "/"

    def get_context_data(self, **kwargs):
    	posts = TaskDocumnent.search().query("match_all")
    	kwargs['Action'] = "Add New"
    	kwargs['posts'] = posts
    	return super(TaskCreateView, self).get_context_data(**kwargs)

#Class to delete the task upon confirmation
class TaskDeleteView(DeleteView):
    template_name = "TaskDelete.html"
    model = Task
    success_url = "/"