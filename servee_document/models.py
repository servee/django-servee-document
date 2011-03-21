from django.db import models
from django.conf import settings
from servee_document.settings import DEFAULT_STORAGE, DOCUMENT_UPLOAD_TO
import datetime

class BaseDocument(models.Model):
    """
    Document model, You may notice that there's no file here,
    That's because you could still use this app, and subclass
    BaseDocument, and do something interesting with your own
    Document, like autoconvert to plain text for searching.
    
    """
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    uploaded = models.DateTimeField(blank=True)
    modified = models.DateTimeField(blank=True)

    def __unicode__(self):
        return '%s' % self.title
        
    def save(self, *args, **kwargs):
        self.modified = datetime.datetime.now()
        if not self.title:
            self.title = self.document.name
        if not self.uploaded:
            self.uploaded = datetime.datetime.now()
        super(BaseDocument, self).save(*args, **kwargs) # Call the "real" save() method.
        
    def get_absolute_url(self):
        return '%s%s' % (settings.MEDIA_URL, self.document)

    class Meta:
        abstract = True
    
class Document(BaseDocument):
    """
    """
    document = models.FileField(
        upload_to=DOCUMENT_UPLOAD_TO,
        storage=DEFAULT_STORAGE()
    )
    
    class Meta:        
        verbose_name = "servee document"
        verbose_name_plural = "servee documents"
        ordering = ['modified',]