from django.db import models

# Create your models here.


class Mineral(models.Model):
    name = models.TextField() # in
    image_filename = models.TextField() # in
    image_caption = models.TextField() # in
    category = models.TextField() # in
    formula = models.TextField(blank=True) # in
    strunz_classification = models.TextField(blank=True) # in
    crystal_system = models.TextField(blank=True) # in
    unit_cell = models.TextField(blank=True) # in
    color = models.TextField(blank=True) # in
    crystal_symmetry = models.TextField(blank=True)
    cleavage = models.TextField(blank=True)
    mohs_scale_hardness = models.TextField(blank=True)
    luster = models.TextField(blank=True)
    streak = models.TextField(blank=True)
    diaphaneity = models.TextField(blank=True)
    optical_properties = models.TextField(blank=True)
    group = models.TextField() # in
    crystal_habit = models.TextField(blank=True)

    def __str__(self):
        return self.name
