from django.conf import settings
from django.core.files.storage import get_storage_class

DEFAULT_STORAGE = get_storage_class(
    getattr(settings, "SERVEE_INSERT_STORAGE_CLASS", settings.DEFAULT_FILE_STORAGE)
)

DOCUMENT_UPLOAD_TO = getattr(settings, "SERVEE_DOCUMENT_INSERT_UPLOAD_TO", "servee_documents")