from django.urls import path

from wagtail.admin.views import workflows

app_name = 'wagtailadmin_workflows'
urlpatterns = [
    path('', workflows.Index.as_view(), name='index'),
    path('add/', workflows.create, name='add'),
    path('edit/<int:pk>', workflows.edit, name='edit'),
]
