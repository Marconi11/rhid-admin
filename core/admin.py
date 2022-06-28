from django.contrib import admin
from . models import Cliente, Sistema, Treinamento

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Sistema)
admin.site.register(Treinamento)

