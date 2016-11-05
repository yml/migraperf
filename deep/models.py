from django.db import models

class Level1(models.Model):
    name = models.CharField(max_length=100)

class Level2(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(Level1, related_name='child')

class Level3(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(Level2, related_name='child')

class Level4(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(Level3, related_name='child')

class Level5(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(Level4, related_name='child')

