from django.db import models
from django.contrib.auth import get_user_model
from users.models import *
import ulid

class LocationModel(models.Model):
    location = models.CharField(verbose_name="地域",max_length=64, null=False, blank=False)
    class Meta:
        db_table = "location"
        verbose_name = "地域"
        verbose_name_plural = "地域"
    
    def __str__(self):
        return self.location


class IndustryModel(models.Model):
    industry = models.CharField(verbose_name="業界",max_length=64, null=False, blank=False)
    class Meta:
        db_table = "industry"
        verbose_name = "業界"
        verbose_name_plural = "業界"
    
    def __str__(self):
        return self.industry

class SectorModel(models.Model):
    sector = models.CharField(verbose_name="業種",max_length=64, null=False, blank=False)
    class Meta:
        db_table = "sector"
        verbose_name = "業種"
        verbose_name_plural = "業種"
    
    def __str__(self):
        return self.sector

class WantedTalentModel(models.Model):
    talent = models.CharField(verbose_name="人材条件",max_length=64, null=False, blank=False)
    class Meta:
        db_table = "WantedTalent"
        verbose_name = "人材条件"
        verbose_name_plural = "人材条件"
    
    def __str__(self):
        return self.talent