from django.urls import path

from tinymce import views

urlpatterns = [
    path("spellchecker/", views.spell_check, name="tinymce-spellcheck"),
    path("flatpages_link_list/", views.flatpages_link_list, name="tinymce-linklist"),
    path("compressor/", views.compressor, name="tinymce-compressor"),
    path("filebrowser/", views.filebrowser, name="tinymce-filebrowser"),
]
