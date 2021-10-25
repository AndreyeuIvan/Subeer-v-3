from django.contrib import admin
from .models import Serial, Episode
from django.utils.safestring import mark_safe

# Register your models here.


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
	'''open Admin realpython'''
	search_fields = ('title',)
	


@admin.register(Serial)
class SerialAdmin(admin.ModelAdmin):
	'''open Admin realpython'''
	search_fields = ('title',)
	prepopulated_fields = {'slug': ('title',)}


	def get_img(self, serial):
		return mark_safe(f'<img src={ serial.poster.url } width="10" height="20"')

	get_img.short_description = 'Poster'