from django.shortcuts import render

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
    FactsBlocks
)

def index(request):
    context = {
          "header_text": HeaderText.objects.all(),
          "footer_text": FooterText.objects.all().first(),
          "service_blocks": Serviceblocks.objects.all(),
          "about_begin": AboutBegin.objects.all().first(),
          "about_together": AboutTogether.objects.all().first(),
          "about_best": AboutBest.objects.all().first(),
          "about_support": AboutSupport.objects.all().first(),
          "about_us": AboutUs.objects.all().first(),
          "latest_courses": LatestCourses.objects.all().first(),
          "events_blocks": EventsBlocks.objects.all(),
          "facts_blocks": FactsBlocks.objects.all(),
    }      

    return render(request,"base.html" , context)
