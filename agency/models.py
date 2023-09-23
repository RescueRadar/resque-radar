from django.db import models

# Create your models here.


class agency(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    website = models.CharField(max_length=50)
    about = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    location_coordinates = models.CharField(max_length=50)
    locality = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    manpower = models.IntegerField()
    volunteers = models.IntegerField()
    category_of_calamity = models.CharField(max_length=50)
    category_of_service = models.CharField(max_length=50)


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "agencies"


class requests(models.Model):
    from_agency = models.ManyToManyField(agency, related_name='from_agency')
    to_agency = models.ManyToManyField(agency, related_name='to_agency')
    request = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.request
    
    class Meta:
        verbose_name_plural = "requests"



