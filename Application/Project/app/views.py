from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import Feedback

# Home and About pages
class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

# Feedback Views
class FeedbackListView(ListView):
    model = Feedback
    template_name = 'app/feedback_list.html'  # Custom template
    context_object_name = 'feedbacks'

class FeedbackDetailView(DetailView):
    model = Feedback
    template_name = 'app/feedback_detail.html'  # Custom template
    context_object_name = 'feedback'

class FeedbackCreateView(CreateView):
    model = Feedback
    template_name = 'app/feedback_form.html'
    fields = ['name', 'email', 'barangay', 'rating', 'comments']

    def form_valid(self, form):
        # Automatically associate the logged-in user if authenticated
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('feedback-list')  # Redirect to feedback list after submission


class FeedbackUpdateView(UpdateView):
    model = Feedback
    template_name = 'app/feedback_form.html'
    fields = ['name', 'email', 'barangay', 'rating', 'comments']

    def get_success_url(self):
        return reverse_lazy('feedback-list')  # Redirect to feedback list after update

class FeedbackDeleteView(DeleteView):
    model = Feedback
    template_name = 'app/feedback_confirm_delete.html'
    success_url = reverse_lazy('feedback-list')
