from django.contrib import admin


from .models import (
    HeaderText,
    FooterText,
    Serviceblocks,
    AboutBegin,
    AboutTogether,
    AboutBest,
    AboutSupport,
    AboutUs,
    LatestCourses,
    EventsBlocks,
    FactsBlocks,
    TeamMembers,
    Authors,
    Testimonial,
    UpcomingEvents,
    Events,
    ContactUs,
    Socials
    ) 

admin.site.register(HeaderText)
admin.site.register(FooterText)
admin.site.register(Serviceblocks)
admin.site.register(AboutBegin)
admin.site.register(AboutTogether)
admin.site.register(AboutBest)
admin.site.register(AboutSupport)
admin.site.register(AboutUs)
admin.site.register(LatestCourses)
admin.site.register(EventsBlocks)
admin.site.register(FactsBlocks)
admin.site.register(TeamMembers)
admin.site.register(Authors)
admin.site.register(Testimonial)
admin.site.register(UpcomingEvents)
admin.site.register(Events)
admin.site.register(ContactUs)
admin.site.register(Socials)
