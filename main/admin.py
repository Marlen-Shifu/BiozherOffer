from django.contrib import admin
from .models import *


admin.site.register(Post)
admin.site.register(Product)
admin.site.register(DocumentationBlock)
admin.site.register(DocumentationBlockItem)
admin.site.register(TrialsPhoto)