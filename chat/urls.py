
from django.conf.urls import url
from chat import views

app_name = 'chat'
urlpatterns = [
    url(r'^$', views.chat_index, name="chat_index"),
    url(r'^message_handle/', views.message_handle, name="message_handle"),
]
