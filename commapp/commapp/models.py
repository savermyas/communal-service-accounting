from django.db import models


class ServiceProviderEntity(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=255)


class UserEntity(models.Model):
    name = models.CharField(max_length=50)


class Counter(models.Model):
    name = models.CharField(max_length=50)
    info = models.CharField(max_length=255)
    previous_value = models.FloatField(default=-1)
    current_value = models.FloatField(default=-1)


class ServiceProvider(models.Model):
    entity = models.ForeignKey(ServiceProviderEntity,
                               on_delete=models.CASCADE)
    counters = models.ManyToManyField(Counter)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class Apartment(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    service_providers = models.ManyToManyField(ServiceProvider)


class User(models.Model):
    entity = models.ForeignKey(UserEntity, on_delete=models.CASCADE)
    apartments = models.ManyToManyField(Apartment)
