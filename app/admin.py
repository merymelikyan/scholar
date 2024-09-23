from django.contrib import admin


from .models import (
    HeaderText,
    FooterText,
    Serviceblocks,
    AboutBegin,
    AboutTogether,
    AboutBest,
    AboutSupport,
    AboutUs
    ) 

admin.site.register(HeaderText)
admin.site.register(FooterText)
admin.site.register(Serviceblocks)
admin.site.register(AboutBegin)
admin.site.register(AboutTogether)
admin.site.register(AboutBest)
admin.site.register(AboutSupport)
admin.site.register(AboutUs)


