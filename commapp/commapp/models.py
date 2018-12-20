from django.db import models


class ServiceProviderEntity(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=255)


class UserEntity(models.Model):
    name = models.CharField(max_length=50)


class Counters(models.Model):
    name = models.CharField(max_length=50)
    info = models.CharField(max_length=255)
    previous_value = models.FloatField()
    current_value = models.FloatField()


class ServiceProviders(models.Model):
    service_provider = models.ForeignKey(ServiceProviderEntity,
                                         on_delete=models.CASCADE)
    counter = models.ForeignKey(Counters, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class Apartments(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    service_provider = models.ForeignKey(ServiceProviders,
                                         on_delete=models.CASCADE)


class Users(models.Model):
    user = models.ForeignKey(UserEntity, on_delete=models.CASCADE)
    apartment = models.ForeignKey(Apartments, on_delete=models.CASCADE)
