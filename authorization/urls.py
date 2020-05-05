from django.urls import path

from authorization import views

urlpatterns = [
    path('test', views.test_session),
    path('authorize', views.authorize, name='authorize'),
    path('user', views.UserView.as_view()),
    path('status', views.get_status, name='get_status'),
]
