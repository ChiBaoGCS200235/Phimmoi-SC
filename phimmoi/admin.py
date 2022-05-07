from django.contrib import admin
from .models import Movie, episode, Viewer

# Register your models here.
admin.site.register(Movie)
admin.site.register(episode)
admin.site.register(Viewer)
