from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.http import Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission, User
from django.core.files.storage import default_storage
from django.contrib.auth.hashers import check_password
from .forms import S3FileUploadForm, S3NewBucketForm
import os
from .utils import upload_to_s3, create_s3_bucket

AWS_BASE_URL = "https://s3.amazonaws.com/"


# Create your views here.

class S3FileUploadView(TemplateView):
    template_name = "awsapp/s3_bucket_file_upload.html"

    def get_context_data(self, **kwargs):
        context = super(S3FileUploadView,
                        self).get_context_data(**kwargs)
        s3_form = S3FileUploadForm()
        s3_new_bucket = S3NewBucketForm()
        context.update({"s3_form": s3_form, "new_bucket": s3_new_bucket, "status": False})

        return context

    def post(self, request, *args, **kwargs):
        s3_form = S3FileUploadForm(request.POST, request.FILES)
        if s3_form.is_valid():
            # The uploaded file
            s3_file = request.FILES.get('s3_file')
            bucket_name = request.POST.get('bucket_list')
            status = upload_to_s3(s3_file, bucket_name)
            context = {"file_url": AWS_BASE_URL + bucket_name + "/" + s3_file.name}
            context.update({"status": status})
            return render(request, "awsapp/s3_bucket_file_upload.html", context)

        else:
            s3_form = S3FileUploadForm()
            context = {"s3_form": s3_form, "status": False}
            return render(request, "awsapp/s3_bucket_file_upload.html", context)


def create_bucket(request):
    """
    Function based view used to create new bucket
    :param request:
    :return:
    """
    s3_new_bucket = S3NewBucketForm(request.POST)

    if s3_new_bucket.is_valid():
        bucket_name = request.POST.get('bucket_name')

        bucket_status = create_s3_bucket(bucket_name)

        context = {"bucket_status": bucket_status, "status": False}

        s3_form = S3FileUploadForm()
        s3_new_bucket = S3NewBucketForm()
        context.update({"s3_form": s3_form, "new_bucket": s3_new_bucket})

        return render(request, "awsapp/s3_bucket_file_upload.html", context)

    else:
        s3_form = S3FileUploadForm()
        s3_new_bucket = S3NewBucketForm()
        context = {}
        context.update({"s3_form": s3_form, "new_bucket": s3_new_bucket, "bucket_status": False})

        return render(request, "awsapp/s3_bucket_file_upload.html", context)
