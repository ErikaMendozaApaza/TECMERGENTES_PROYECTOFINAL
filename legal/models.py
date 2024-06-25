from django.db import models
from ckeditor.fields import RichTextField

# # # # # # # # # # # # # # # # # #
# Modelo de términos y condiciones#
# # # # # # # # # # # # # # # # # #

class Terms(models.Model):
    term_texts = RichTextField(blank=True, null=True)

    def __str__(self):
        return 'Terms And Conditions'
    
# # # # # # # # # # # # # # # # # #
# Modelo de Política de Privacidad#
# # # # # # # # # # # # # # # # # #
class Policy(models.Model):
    policy_texts = RichTextField(blank=True, null=True)

    def __str__(self):
        return 'Privacy Policy'