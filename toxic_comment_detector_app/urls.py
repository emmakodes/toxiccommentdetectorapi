from django.urls import path
from . import views

app_name = 'toxic_comment_detector_app'

urlpatterns = [
    path('', views.DetectToxicComment.as_view(), name='detect_toxic_comment')
]