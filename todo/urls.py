from django.urls import path

from todo.views import TodoListCreateAPIView, TodoUpdateDeleteAPIView


urlpatterns = [
    path('', TodoListCreateAPIView.as_view()),
    path('<int:pk>/', TodoUpdateDeleteAPIView.as_view())
]