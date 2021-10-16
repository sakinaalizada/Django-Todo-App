from django.urls import path
from .views import TaskList, TaskDetail,TaskCreate, TaskUpdate,CustomLoginView, RegisterPage,BoardList,BoardCreate,BoardUpdate,DeleteBoard, DeleteTask
#BoardList,BoardCreate,BoardUpdate,DeleteBoard
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',CustomLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path('task/<int:pk>',TaskDetail.as_view(),name='task'),
    path('task-create/<int:pk>',TaskCreate.as_view(),name='task-create'),
    path('task-update/<int:pk>',TaskUpdate.as_view(),name='task-update'),
    path('task-delete/<int:pk>',DeleteTask.as_view(),name='task-delete'),
    path('',BoardList.as_view(),name='boards'),
    path('board-create/',BoardCreate.as_view(),name='board-create'),
    path('board-update/<int:pk>',BoardUpdate.as_view(),name='board-update'),
   path('board-delete/<int:pk>',DeleteBoard.as_view(),name='board-delete'),
]



