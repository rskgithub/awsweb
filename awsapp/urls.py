from django.conf.urls import url, include
from . import views as views

urlpatterns = [
    url(r'^s3/file/upload/', views.S3FileUploadView.as_view(), name='s3-file-upload'),

]
