from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class agency(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    website = models.CharField(max_length=50)
    about = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    location_lat = models.FloatField(default=0.0) 
    location_long = models.FloatField(default=0.0)  
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


class non_approved_agency(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    website = models.CharField(max_length=50)
    about = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    location_lat = models.FloatField(default=0.0) 
    location_long = models.FloatField(default=0.0)  
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
        verbose_name_plural = "non_approved_agencies"
    
    def approve(self):
        agency.objects.create(name=self.name, address=self.address, phone=self.phone, email=self.email, website=self.website, about=self.about, created_at=self.created_at, updated_at=self.updated_at, location_lat=self.location_lat, location_long=self.location_long, locality=self.locality, city=self.city, state=self.state, manpower=self.manpower, volunteers=self.volunteers, category_of_calamity=self.category_of_calamity, category_of_service=self.category_of_service)
        self.delete()
        return True

class CollaborationRequest(models.Model):
    request_id = models.AutoField(primary_key=True)
    requesting_agency = models.ForeignKey(agency, on_delete=models.CASCADE, related_name='requests_sent')
    target_agency = models.ForeignKey(agency, on_delete=models.CASCADE, related_name='requests_received')
    request_details = models.TextField()
    request_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request from {self.requesting_agency.name} to {self.target_agency.name}"

class CollaborationResponse(models.Model):
    response_id = models.AutoField(primary_key=True)
    collaboration_request = models.ForeignKey(CollaborationRequest, on_delete=models.CASCADE)
    response_agency = models.ForeignKey(agency, on_delete=models.CASCADE)
    response_details = models.TextField()
    response_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Response to {self.collaboration_request}"

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


@receiver(post_save, sender=non_approved_agency)
def new_agency(sender, instance, created, **kwargs):
    if created:
        print("New agency created")
        return True
    else:
        print("New agency not created")
        return False