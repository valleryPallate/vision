from django.db import models
from django.urls import reverse


# Lost Child Model
class LostChild(models.Model):
    first_name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    other_name = models.CharField(max_length=20, blank=True, null=True)
    GENDER_CHOICES = [
        ('m', 'male'),
        ('f', 'female')]
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(blank=True)
    home_country = models.CharField(
        max_length=20, blank=True, null=True, help_text="Enter home County")
    home_county = models.CharField(
        max_length=20, blank=True, null=True, help_text="Enter home County")
    home_town = models.CharField(
        max_length=20, blank=True, null=True, help_text="Enter home Town")
    religion = models.CharField(max_length=10, blank=True, null=True)
    # Description
    height_in_feet: models.FloatField(null=True)
    hair_colour: models.CharField(max_length=20, blank=True, null=True)
    eye_colour: models.CharField(max_length=20, blank=True, null=True)
    ethnicity: models.CharField(max_length=20, blank=True, null=True)
    other_relevant_information: models.TextField(max_length=255, blank=True, null=True)
    # Parents Details
    father_alive = models.BooleanField(default=True, blank=True,
                                       help_text="Is the father alive?")
    mother_alive = models.BooleanField(
        default=True, blank=True,
        help_text="Is the mother alive?")
    father_first_name = models.CharField(max_length=20, blank=True, help_text="Enter the first name of the child's "
                                                                              "male guardian")
    father_surname = models.CharField(max_length=20, blank=True, null=True, )
    father_email = models.EmailField(blank=True, null=True)
    father_phone = models.IntegerField(null=True, blank=True)
    mother_first_name = models.CharField(max_length=20, blank=True, help_text="Enter the first name of the child's "
                                                                              "female guardian")
    mother_surname = models.CharField(max_length=20, blank=True)
    mother_email = models.EmailField(null=True)
    mother_phone = models.IntegerField(null=True)
    # Last Seen
    time_last_seen = models.DateTimeField()
    place_last_seen = models.CharField(max_length=40, blank=True)
    county_last_seen = models.CharField(max_length=20, blank=True, null=True)
    city_last_seen = models.CharField(max_length=20, blank=True, null=True)
    district_last_seen = models.CharField(max_length=20, blank=True, null=True)
    # Images # We will definitely find a better way to handle images...
    photo = models.ImageField(upload_to='lost')
    #
    time_added = models.DateTimeField(auto_now_add=True)
    time_last_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.surname} {self.first_name}'

    class Meta:
        ordering = ['surname', 'first_name']

    def get_absolute_url(self):
        reverse('lost_child_detail', args=[str(self.id)])


# Found Child Model
class FoundChild(models.Model):
    first_name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    other_name = models.CharField(max_length=20, blank=True, null=True)
    GENDER_CHOICES = [
        ('m', 'male'),
        ('f', 'female')]
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(blank=True)
    home_country = models.CharField(
        max_length=20, blank=True, null=True, help_text="Enter home County")
    home_county = models.CharField(
        max_length=20, blank=True, null=True, help_text="Enter home County")
    home_town = models.CharField(
        max_length=20, blank=True, null=True, help_text="Enter home Town")
    religion = models.CharField(max_length=10, blank=True, null=True)
    # Description
    height_in_feet: models.FloatField(null=True)
    hair_colour: models.CharField(max_length=20, blank=True, null=True)
    eye_colour: models.CharField(max_length=20, blank=True, null=True)
    ethnicity: models.CharField(max_length=20, blank=True, null=True)
    other_relevant_information: models.TextField(max_length=255, blank=True, null=True)
    # Parents Details
    father_first_name = models.CharField(max_length=20, blank=True,null=True, help_text="Enter the first name of the child's "
                                                                              "male guardian")
    father_surname = models.CharField(max_length=20, blank=True, null=True, )
    mother_first_name = models.CharField(max_length=20, blank=True, help_text="Enter the first name of the child's "
                                                                              "female guardian")
    mother_surname = models.CharField(max_length=20, blank=True)
    # Found
    time_found = models.DateTimeField()
    county_found = models.CharField(max_length=20, blank=True, null=True)
    city_found = models.CharField(max_length=20, blank=True, null=True)
    district_found = models.CharField(max_length=20, blank=True, null=True)
    place_found = models.CharField(max_length=40, blank=True, null=True)
    # Images
    photo = models.ImageField(upload_to='found')
    #
    time_added = models.DateTimeField(auto_now_add=True)
    time_last_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.surname} {self.first_name}'

    class Meta:
        ordering = ['surname', 'first_name']

    def get_absolute_url(self):
        reverse('found_child_detail', args=[str(self.id)])
