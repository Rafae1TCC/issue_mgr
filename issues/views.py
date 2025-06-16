from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Issue
from .models import Status
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class IssueListView(ListView):
    template_name = 'issues/list.html'
    model = Issue

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        todo_status = Status.objects.get(name="to_do")
        progress_status = Status.objects.get(name="in_progress")
        done_status = Status.objects.get(name="done")

        context["to_do_list"] = (
            Issue.objects
            .filter(status=todo_status)
            .order_by('-created_on')
        )

        context["in_progress_list"] = (
            Issue.objects
            .filter(status=progress_status)
            .order_by('-created_on')
        )

        context["done_list"] = (
            Issue.objects
            .filter(status=done_status)
            .order_by('-created_on')
        )
        return context

class IssueDetailView(DetailView, LoginRequiredMixin, UpdateView):
    template_name = 'issues/detail.html'
    model = Issue
    fields = ["status"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class IssueCreateView(LoginRequiredMixin, CreateView):
    template_name = 'issues/new.html'
    model = Issue
    fields = ["title", "summary", "description", "reporter", "assignee", "status"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
