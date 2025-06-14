from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Issue
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class IssueListView(ListView):
    template_name = 'issues/list.html'
    model = Issue

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        todo = Status.objects.get(name="to-do")

        context["to-do-list"] = (
            Post.objects
            .filter(status=published)
            .order_by('created_on').reverse()
        )

        progress = Status.objects.get(name="in-progress")

        context["in-progress-list"] = (
            Post.objects
            .filter(status=published)
            .order_by('created_on').reverse()
        )

        done = Status.objects.get(name="done")

        context["done-list"] = (
            Post.objects
            .filter(status=published)
            .order_by('created_on').reverse()
        )
        return context

class IssueDetailView(DetailView):
    template_name = 'issues/detail.html'
    model = Issue

class IssueCreateView(LoginRequiredMixin, CreateView):
    template_name = 'issues/new.html'
    model = Issue
    fields = ["title", "summary", "description", "reporter", "assignee", "status"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)