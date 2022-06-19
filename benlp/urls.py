from django.urls import path
# from .views import main
from .views import Summarizer_View
from . import views
from .views import index


urlpatterns = [
    # path('', main),
    # path('summarizer', SummarizerView.as_view()),
    # path('summarizer', SummarizerView.as_view()),
    path('summarizer', views.Summarizer_View, name='summarizer'),
    path("", index, name="index"),
    



]