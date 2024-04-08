
from api.views import SubjectListView
from django.urls import path

app_name = 'apis'

urlpatterns = [
    path('', SubjectListView.as_view(), name='apis')
]

