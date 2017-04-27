from django.conf.urls import patterns, url
from . import views

urlpatterns = [
    url(r"^upload/$", views.upload_documents, name="servee_document_upload_documents"),
    url(r"^recent/$", views.recent_documents, name="servee_document_recent_documents")
]
