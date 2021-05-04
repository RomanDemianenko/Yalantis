from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from yala.forms import CourseForm
from yala.models import Course


class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    success_url = '/course/'
    template_name = 'create.html'


class CourseListView(ListView):
    model = Course
    form_class = CourseForm
    ordering = ['-id']
    paginate_by = 10
    template_name = 'course.html'


class CourseDetailView(DetailView):
    model = Course
    form_class = CourseForm
    template_name = 'detail.html'
    context_object_name = 'course'


class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseForm
    success_url = '/course/'
    template_name = 'update.html'

    def post(self, request, *args, **kwargs):
        course_pk = self.kwargs['pk']
        seance = Course.objects.get(id=course_pk)
        form = CourseForm(request.POST, instance=seance)
        if form.is_valid():
            messages.success(self.request, "You Update the Curse")
            return HttpResponseRedirect('/course/')
        else:
            messages.warning(self.request, 'You must change date')
        context = {'form': form}
        return render(request, 'update.html', context)


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'delete.html'
    success_url = '/course/'
    context_object_name = 'obj'


class SearchListView(ListView):
    model = Course
    template_name = 'search_result.html'

    def get_queryset(self):
        search = self.request.GET.get('title')
        title = Course.objects.filter(title__icontains=search)
        return title


class DateFilterListView(ListView):
    model = Course
    template_name = 'date_filter.html'

    def get_queryset(self):
        date1 = self.request.GET.get('date1')
        date2 = self.request.GET.get('date2')
        q1 = Q(start__lte=date1, end__gte=date1)
        q2 = Q(start__lte=date2, end__gte=date2)
        queryset = Course.objects.filter(q1 | q2)
        return queryset
