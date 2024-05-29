from django.db import models

class Operateur(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    numtel = models.CharField(max_length=15)
    password = models.CharField(max_length=255)

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    drone_choices = [
        ('orange', 'orange'),
        ('TT', 'TT'),
    ]
    operateur = models.CharField(max_length=100, choices=drone_choices, default='orange')

class Firewall(models.Model):
    ip = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=15)

class FirewallPolicy(models.Model):
    name = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    destination = models.CharField(max_length=15)
    fortinet = models.CharField(max_length=15)

class SDWAN(models.Model):
    sdwanzone = models.CharField(max_length=255)
    sdwanmembers = models.CharField(max_length=255)
    gateway = models.CharField(max_length=255)
    cost = models.CharField(max_length=15)
    download = models.CharField(max_length=15)
    upload = models.CharField(max_length=15)
    fortigate = models.CharField(max_length=15)

class SDWANRules(models.Model):
    name = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    destination = models.CharField(max_length=15)
    members = models.CharField(max_length=15)
    fortigate = models.CharField(max_length=15)