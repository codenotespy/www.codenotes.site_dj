# Model Translation
from modeltranslation.translator import translator, TranslationOptions, register
from .models import *

@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'letter')







#python manage.py makemigrations
#python manage.py migrate

#The newly added translation fields on the model will be empty then, and your templates will show the translated value of the fields (see Rule 1) which will be empty in this case. To correctly initialize the default translation field you can use the update_translation_fields command:

#python manage.py update_translation_fields




#This command compares the database and translated models definitions (finding new translation fields) and provides SQL statements to alter tables. You should run this command after adding a new language to your settings.LANGUAGES or a new field to the TranslationOptions of a registered model.

#python manage.py sync_translation_fields