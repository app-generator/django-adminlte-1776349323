# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Branches(models.Model):

    #__Branches_FIELDS__
    branch_id = models.IntegerField(null=True, blank=True)
    branch_name = models.TextField(max_length=255, null=True, blank=True)
    address = models.TextField(max_length=255, null=True, blank=True)
    upi_id = models.TextField(max_length=255, null=True, blank=True)
    clinic_email = models.TextField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField()
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    created_by = models.TextField(max_length=255, null=True, blank=True)

    #__Branches_FIELDS__END

    class Meta:
        verbose_name        = _("Branches")
        verbose_name_plural = _("Branches")


class Users(models.Model):

    #__Users_FIELDS__
    user_id = models.IntegerField(null=True, blank=True)
    username = models.TextField(max_length=255, null=True, blank=True)
    password_hash = models.TextField(max_length=255, null=True, blank=True)
    full_name = models.TextField(max_length=255, null=True, blank=True)
    role = models.TextField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    created_by = models.TextField(max_length=255, null=True, blank=True)

    #__Users_FIELDS__END

    class Meta:
        verbose_name        = _("Users")
        verbose_name_plural = _("Users")


class Patients(models.Model):

    #__Patients_FIELDS__
    branch_id = models.IntegerField(null=True, blank=True)
    display_id = models.TextField(max_length=255, null=True, blank=True)
    first_name = models.TextField(max_length=255, null=True, blank=True)
    last_name = models.TextField(max_length=255, null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    email = models.TextField(max_length=255, null=True, blank=True)
    dob = models.DateTimeField(blank=True, null=True, default=timezone.now)
    medical_history = models.TextField(max_length=255, null=True, blank=True)
    sync_status = models.TextField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    created_by = models.TextField(max_length=255, null=True, blank=True)
    updated_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    updated_by = models.TextField(max_length=255, null=True, blank=True)

    #__Patients_FIELDS__END

    class Meta:
        verbose_name        = _("Patients")
        verbose_name_plural = _("Patients")


class Appointments(models.Model):

    #__Appointments_FIELDS__
    appointment_id = models.IntegerField(null=True, blank=True)
    dentist_id = models.IntegerField(null=True, blank=True)
    appointment_time = models.DateTimeField(blank=True, null=True, default=timezone.now)
    status = models.TextField(max_length=255, null=True, blank=True)
    notes = models.TextField(max_length=255, null=True, blank=True)
    is_manual_entry = models.BooleanField()
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    created_by = models.TextField(max_length=255, null=True, blank=True)

    #__Appointments_FIELDS__END

    class Meta:
        verbose_name        = _("Appointments")
        verbose_name_plural = _("Appointments")


class Xray_Images(models.Model):

    #__Xray_Images_FIELDS__
    file_path = models.TextField(max_length=255, null=True, blank=True)
    captured_by = models.IntegerField(null=True, blank=True)
    captured_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    created_by = models.TextField(max_length=255, null=True, blank=True)

    #__Xray_Images_FIELDS__END

    class Meta:
        verbose_name        = _("Xray_Images")
        verbose_name_plural = _("Xray_Images")


class Ai_Diagnostics(models.Model):

    #__Ai_Diagnostics_FIELDS__
    ai_result = models.TextField(max_length=255, null=True, blank=True)
    dentist_confirmation = models.BooleanField()
    confirmed_by = models.TextField(max_length=255, null=True, blank=True)
    dentist_notes = models.TextField(max_length=255, null=True, blank=True)
    confirmed_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Ai_Diagnostics_FIELDS__END

    class Meta:
        verbose_name        = _("Ai_Diagnostics")
        verbose_name_plural = _("Ai_Diagnostics")


class Bills(models.Model):

    #__Bills_FIELDS__
    total_amount = models.IntegerField(null=True, blank=True)
    tax_amount = models.IntegerField(null=True, blank=True)
    upi_payment_link = models.TextField(max_length=255, null=True, blank=True)
    payment_status = models.TextField(max_length=255, null=True, blank=True)
    payment_method = models.TextField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    created_by = models.TextField(max_length=255, null=True, blank=True)

    #__Bills_FIELDS__END

    class Meta:
        verbose_name        = _("Bills")
        verbose_name_plural = _("Bills")



#__MODELS__END
