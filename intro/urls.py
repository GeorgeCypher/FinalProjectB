from django.urls import path
from intro.views import HomeTemplateView

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='homepage')

]