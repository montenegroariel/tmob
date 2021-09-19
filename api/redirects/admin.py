from django.contrib import admin
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache
from .models import Redirect

class RedirectAdmin(admin.ModelAdmin):
    list_display = ('key', 'url', 'created_at', 'updated_at')

    @receiver(post_save, sender=Redirect)
    def cache_redirect(sender, instance, created, **kwargs):
        if not created:
            redirects = Redirect.objects.filter(active=True)
            cache.set('QuerysetRedirect', redirects, None)
            pass    

admin.site.register(Redirect,RedirectAdmin)

