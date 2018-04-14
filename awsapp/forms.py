from django import forms


class S3FileUploadForm(forms.Form):
    """
    Class the presents a form for uploading a file

    """
    s3_file = forms.FileField(label="Upload a File to S3 Bucket", required=True)
