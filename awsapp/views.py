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
from .forms import S3FileUploadForm
import os
from .utils import upload_to_s3


# Create your views here.

class S3FileUploadView(TemplateView):
    template_name = "awsapp/s3_bucket_file_upload.html"

    def get_context_data(self, **kwargs):
        context = super(S3FileUploadView,
                        self).get_context_data(**kwargs)
        s3_form = S3FileUploadForm()
        context.update({"s3_form": s3_form})
        print(os.environ['AWS_ACCESS_KEY_ID'])
        return context

    def post(self, request, *args, **kwargs):
        s3_form = S3FileUploadForm(request.POST, request.FILES)
        if s3_form.is_valid():
            # The uploaded file
            s3_file = request.FILES.get('s3_file')
            upload_to_s3(s3_file, "intuitorit")

            return render(request, "awsapp/s3_bucket_file_upload.html")

        else:
            s3_form = S3FileUploadForm()
            context = {"s3_form": s3_form}
            return render(request, "awsapp/s3_bucket_file_upload.html", context)
