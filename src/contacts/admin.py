from django.contrib import admin

from .models import Contact, MyContact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = ("user", "email", "company", "contact_text")
    list_display_links = ("user", "email", "company")

admin.site.register(MyContact)
