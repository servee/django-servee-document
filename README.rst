Django-servee-document is a document plugin for django-servee

It requires django-easy-thumbnails (which, requires PIL, and to use document thumbnails, you must have imagick/convert+wvWare installed)

Also note, the default settings should suffice, and these are not required.

SERVEE_INSERT_STORAGE_CLASS
SERVEE_DOCUMENT_INSERT_UPLOAD_TO

There are no views or URLS for this project, it uses the default views, urls, and forms of the Servee ModelInsert class.


To try it out:

1.   Download the project.
2.   run python setup.py develop [requires django-servee=>0.6 which is trunk, not in PyPI]
3.   cd example_project
4.   python manage.py syncdb
5.   python manage.py runserver
6.   http://localhost:8000/login/
7.   Click "edit flatpage"
8.   Put your cursor in the wysiwyg window
9.   Click the "add button" at the bottom left of the wysiwyg toolbar and click "document"
10.  Upload a document from your computer
11.  Click the document thumbnail, then place it in your editor.