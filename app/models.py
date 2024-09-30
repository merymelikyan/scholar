from django.db import models


class HeaderText (models.Model):
    tag = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    question= models.CharField(max_length=255,blank=True, null=True)
    request = models.CharField(max_length=255,blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Header Text"
        verbose_name_plural = "Header Texts"
 

class FooterText(models.Model):
    text1 = models.CharField(max_length=255, blank=True, null=True)
    text2 = models.CharField(max_length=255, blank=True, null=True)
    text3 = models.CharField(max_length=255, blank=True, null=True)
    link_url = models.URLField(max_length=200, blank=True, null=True) 

    def __str__(self):
        return f"{self.text1} {self.text2}"

    class Meta:
        verbose_name = "Footer Text"
        verbose_name_plural = "Footer Text"


class Serviceblocks(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to="service_blocks")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Serviceblocks"
        verbose_name_plural = "Serviceblocks"


class AboutBegin(models.Model):
    title = models.CharField(max_length=255)
    description1 = models.TextField(max_length=255, blank=True, null=True)
    description2 = models.TextField(max_length=255, blank=True, null=True)
    description3 = models.TextField(max_length=255, blank=True, null=True)
    description4 = models.TextField(max_length=255, blank=True, null=True)
    description5 = models.TextField(max_length=255, blank=True, null=True)
   

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "About Begin"
        verbose_name_plural = "About Begin"

class AboutTogether(models.Model):
    title = models.CharField(max_length=255)
    description1 = models.TextField(max_length=255, blank=True, null=True)
    description2 = models.TextField(max_length=255, blank=True, null=True)
    description3 = models.TextField(max_length=255, blank=True, null=True)
    description4 = models.TextField(max_length=255, blank=True, null=True)
    description5 = models.TextField(max_length=255, blank=True, null=True)
   

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "About Together"
        verbose_name_plural = "About Together"        


class AboutBest(models.Model):
    title = models.CharField(max_length=255)
    description1 = models.TextField(max_length=255, blank=True, null=True)
    description2 = models.TextField(max_length=255, blank=True, null=True)
    description3 = models.TextField(max_length=255, blank=True, null=True)
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "About Best"
        verbose_name_plural = "About Best"        


class AboutSupport(models.Model):
    title = models.CharField(max_length=255)
    description1 = models.TextField(max_length=255, blank=True, null=True)
    description2 = models.TextField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "About Support"
        verbose_name_plural = "About Support"     


class AboutUs(models.Model):
    tag = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255, blank=True, null=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "About Us"
        verbose_name_plural = "About Us"     


class LatestCourses(models.Model):
    title= models.TextField(max_length=255)
    description = models.TextField(max_length=255)
    category1 = models.CharField(max_length=255, blank=True, null=True)
    category2 = models.CharField(max_length=255, blank=True, null=True)
    category3 = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Latest Courses"
        verbose_name_plural = "Latest Courses"


class EventsBlocks(models.Model):
    category = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    title1 = models.CharField(max_length=255, blank=True, null=True)
    title2 = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="events_blocks")
    
    def __str__(self):
        return self.category

    class Meta:
        verbose_name = "Events Blocks"
        verbose_name_plural = "Events Blocks"

class FactsBlocks(models.Model):
    title= models.TextField(max_length=255)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Facts Blocks"
        verbose_name_plural = "Facts Blocks"


class TeamMembers(models.Model):
    name = models.CharField(max_length=45)
    position = models.CharField(max_length=60)
    image = models.ImageField(upload_to="team_members")
  
    def __str__(self):
        return f"{self.name}{self.position}"

    class Meta:
        verbose_name = "Team Members"
        verbose_name_plural = "Team Members"

class Authors(models.Model):
    name = models.CharField(max_length=45)
    position = models.CharField(max_length=60)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to="authors")
      
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Authors"
        verbose_name_plural = "Authors"



class Testimonial(models.Model):
    tag = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.tag
      
    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"


class UpcomingEvents(models.Model):
    tag = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
  
    def __str__(self):
        return self.tag
      
    class Meta:
        verbose_name = "Upcoming Events"
        verbose_name_plural = "Upcoming Events"


class Events(models.Model):
    tag = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="events")
    data = models.CharField(max_length=50, null=True, blank=True, help_text="FontAwesome icon")
    duration = models.CharField(max_length=10, null=True, blank=True)
    price = models.CharField(max_length=50, null=True, blank=True)
    html_class = models.CharField(max_length=55)

    def __str__(self):
        return self.tag
      
    class Meta:
        verbose_name = "Events"
        verbose_name_plural = "Events"


class ContactUs(models.Model):
    tag = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255, blank=True, null=True)
    offer_percent = models.CharField(max_length=50, null=True, blank=True)
    valide = models.CharField(max_length=50, null=True, blank=True)
    html_class = models.CharField(max_length=255)

    def __str__(self):
        return self.tag
      

    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"


class Socials(models.Model):
    title = models.CharField(max_length=50)
    url = models.URLField(max_length=255, blank=True)
    html_class = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Social"
        verbose_name_plural = "Socials"
