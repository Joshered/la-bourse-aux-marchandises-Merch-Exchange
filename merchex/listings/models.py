from django.db import models

# Table  groupes et les annonces d’articles à vendre
class Band(models.Model):
    name = models.fields.CharField(max_length=100)
    
# Model Listings
class Listings(models.Model):
    title = models.fields.CharField(max_length=100)
