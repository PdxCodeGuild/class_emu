from django.urls import path

from . import views

app_name = 'mySurvey'
urlpatterns = [
    # ex: /mySurvey/
    path('', views.index, name='index'),
    # ex: /mySurvey/5/, /mySurvey/112/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /mySurvey/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /mySurvey/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
