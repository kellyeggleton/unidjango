from django.contrib import admin
from .models import GeneName, Sequencing, Classification, Condition, Patient_Details, Variant_Details, Patient_Variant

# Register your models here.
admin.site.register(GeneName)
admin.site.register(Sequencing)
admin.site.register(Classification)
admin.site.register(Condition)
admin.site.register(Patient_Details)
admin.site.register(Variant_Details)
admin.site.register(Patient_Variant)
