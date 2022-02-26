from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

from .models import Phrase
from .models import Thinker

# Create "resource" to use in below registration
class PhraseResource(resources.ModelResource):

    class Meta:
        model = Phrase
        exclude = ('created_date',)

class ThinkerResource(resources.ModelResource):

    class Meta:
        model = Thinker

# Use the above model to show interface in Admin console
class PhraseAdmin(ImportExportModelAdmin):
    resource_class = PhraseResource
    list_display = ['id', 'text']

# Use the above model to show interface in Admin console
class ThinkerAdmin(ImportExportModelAdmin):
    resource_class = ThinkerResource
    list_display = ['id', 'name']

admin.site.register(Phrase, PhraseAdmin)
admin.site.register(Thinker, ThinkerAdmin)

# Change header title of Admin page
admin.site.site_header = 'Comfucius control panel'
