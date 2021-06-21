from django.contrib import admin

from .models import GitHub, HardSkill, ExtraSkill, SoftSkill, Resume, English


admin.site.register(GitHub)
admin.site.register(HardSkill)
admin.site.register(ExtraSkill)
admin.site.register(SoftSkill)
admin.site.register(Resume)
admin.site.register(English)