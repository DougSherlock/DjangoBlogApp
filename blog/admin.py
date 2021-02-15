from django.contrib import admin
from .models import Post

# make Posts visible on the Admin page
admin.site.register(Post) 
