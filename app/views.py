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
    FactsBlocks,
    TeamMembers,
    Authors,
    Testimonial,
    UpcomingEvents,
    Events,
    ContactUs,
    Socials

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
          "team_members" :TeamMembers.objects.all(),
          "authors": Authors.objects.all(),
          "testimonial": Testimonial.objects.all().first(),
          "upcoming_events": UpcomingEvents.objects.all().first(),
          "events": Events.objects.all(),
          "contact_us": ContactUs.objects.all().first(),
          "socials": Socials.objects.all()
    }      

    return render(request,"home.html" , context)


def about(request):
    context = {
        "header_text": HeaderText.objects.all(),
        "footer_text": FooterText.objects.all().first(),
        "about_begin": AboutBegin.objects.all().first(),
        "about_together": AboutTogether.objects.all().first(),
        "about_best": AboutBest.objects.all().first(),
        "about_support": AboutSupport.objects.all().first(),
        "about_us": AboutUs.objects.all().first(),
        "contact_us": ContactUs.objects.all().first(),
        "socials": Socials.objects.all(),
        
    }
    return render(request, "about.html", context)




def contact(request):
    context = {
        "header_text": HeaderText.objects.all(),
        "footer_text": FooterText.objects.all().first(),
        "contact_us": ContactUs.objects.all().first(),
        "socials": Socials.objects.all(),
        
    }
    return render(request, "contact.html", context)




def courses(request):
    context = {
        "header_text": HeaderText.objects.all(),
        "footer_text": FooterText.objects.all().first(),
        "latest_courses": LatestCourses.objects.all().first(),
        "events_blocks": EventsBlocks.objects.all(),
        "contact_us": ContactUs.objects.all().first(),
        "socials": Socials.objects.all(),
       
      
    }
    
    return render(request, "courses.html", context)


def team(request):
    context = {
        "header_text": HeaderText.objects.all(),
        "footer_text": FooterText.objects.all().first(),
        "team_members" :TeamMembers.objects.all(),
        "authors": Authors.objects.all(),
        "testimonial": Testimonial.objects.all().first(),
        "contact_us": ContactUs.objects.all().first(),
        "socials": Socials.objects.all(),
        
     
    }
    return render(request, "team.html", context)




def services(request):
    context = {
        "header_text": HeaderText.objects.all(),
        "footer_text": FooterText.objects.all().first(),
        "service_blocks": Serviceblocks.objects.all(),
        "contact_us": ContactUs.objects.all().first(),
        "socials": Socials.objects.all(),
        
    }

    return render(request, "services.html", context)


def events(request):
    context = {
        "header_text": HeaderText.objects.all(),
        "footer_text": FooterText.objects.all().first(),
        "upcoming_events": UpcomingEvents.objects.all().first(),
        "events": Events.objects.all(),
        "contact_us": ContactUs.objects.all().first(),
        "socials": Socials.objects.all(),
        
    }
    
    return render(request, "events.html", context)
