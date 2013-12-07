from django.conf.urls import patterns, url

urlpatterns = patterns("",
    url(r"^upload/$", "servee_document.views.upload_documents", name="servee_document_upload_photos"),
    url(r"^recent/$", "servee_document.views.recent_documents", name="servee_document_recent_photos")
)
