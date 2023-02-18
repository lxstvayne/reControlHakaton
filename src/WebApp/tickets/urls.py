from django.urls import path

from . import views


urlpatterns = [
    path('tickets/', views.TicketListCreateView.as_view()),
    path('tickets/<int:pk>', views.TicketRetrieveView.as_view()),
    path('tasks/', views.TaskListCreateView.as_view()),
    path('tasks/<int:pk>', views.TaskUpdateDestroyView.as_view()),
    path('followUp/', views.FollowUpCreateView.as_view()),
]
