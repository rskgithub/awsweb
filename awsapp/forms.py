from django import forms
from .utils import list_all_buckets


class S3FileUploadForm(forms.Form):
    """
    Class the presents a form for uploading a file

    """

    bucket_list = forms.ChoiceField(
        choices=list_all_buckets(), label="Select a Bucket", required=True)
    s3_file = forms.FileField(label="Upload a File to S3 Bucket", required=True)
