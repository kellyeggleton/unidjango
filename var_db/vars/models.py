from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


#each class creates a model that corresponds to a table in the database


class GeneName(models.Model):
	GeneName_ID=models.AutoField(primary_key=True)
	GeneName=models.CharField(max_length=100,null=True)
	def __str__(self):
        	return (self.GeneName)


class Sequencing(models.Model):
	Sequencer=models.CharField(max_length=100,null=False)
	Platform=models.AutoField(primary_key=True) 
	def __str__(self):
        	return (self.Sequencer)



class Classification(models.Model):
	Class_ID=models.AutoField(primary_key=True)
	Classification=models.CharField(max_length=100,null=True)
	def __str__(self):
        	return (self.Classification)




class Condition(models.Model):
	Condition_ID=models.AutoField(primary_key=True)
	Condition=models.CharField(max_length=100,null=True)
	def __str__(self):
        	return (self.Condition)



class Patient_Details(models.Model):
	name=models.CharField(max_length=100,null=False)
	created_date = models.DateTimeField(default = timezone.now)
	age=models.IntegerField(null=False)
	Patient_ID=models.AutoField(primary_key=True)
	Condition_ID=models.ForeignKey(Condition,null=True)
	def __str__(self):
        	return"%s, %s" %(self.name, self.age)



class Variant_Details(models.Model):
	Variant_ID=models.AutoField(primary_key=True)
	Variant_cDNA=models.CharField(max_length=100,null=True)
	Variant_Protein=models.CharField(max_length=100,null=True)
	Variant_Genome=models.CharField(max_length=100)
	GeneName_ID=models.ForeignKey(GeneName)
	Class_ID=models.ForeignKey(Classification,null=True)
	Platform=models.ForeignKey(Sequencing)
	def __str__(self):
        	return "%s" %(self.Variant_Genome)



class Patient_Variant(models.Model):
	Variant_ID=models.ForeignKey(Variant_Details)
	Patient_ID=models.ForeignKey(Patient_Details)
	


	



















