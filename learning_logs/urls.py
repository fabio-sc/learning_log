from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    #home page
    path('', views.index, name='index'),

    #topics page
    path('topics', views.topics, name='topics'),

    path('topics/<int:topic_id>', views.topic, name='topic'),
]