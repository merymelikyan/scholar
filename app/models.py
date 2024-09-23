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