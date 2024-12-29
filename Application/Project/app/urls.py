from django.urls import path
from .views import (
    HomePageView, AboutPageView, FeedbackListView, FeedbackDetailView, FeedbackCreateView,
    FeedbackUpdateView, FeedbackDeleteView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('feedback/', FeedbackListView.as_view(), name='feedback-list'),
    path('feedback/new/', FeedbackCreateView.as_view(), name='feedback-create'),  # Create view
    path('feedback/<int:pk>/', FeedbackDetailView.as_view(), name='feedback-detail'),
    path('feedback/<int:pk>/edit/', FeedbackUpdateView.as_view(), name='feedback-update'),
    path('feedback/<int:pk>/delete/', FeedbackDeleteView.as_view(), name='feedback-delete'),
]
