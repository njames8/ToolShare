""" 
file: models.py
language: python3
author: Nicholas James 
author: Andrew Carpenter 
description: The model representations of objects in the database
"""
from django.db import models
from django import forms
from django.contrib.auth.models import User

class Shed(models.Model):
	"""
	Represents a Shed in the DB
	name = name of shed
	location = zipcode
	numUsers = the number of users of the shed
	numTools = number of tools in the shed
	"""
	name = models.CharField(max_length = 100)
	coordinator = models.ForeignKey(User)
	location = models.CharField(max_length=5)
	numUsers = models.IntegerField(default = 1)
	numTools = models.IntegerField(default = 0) 
	#toolListing = 
	#userListing = 

	def __str__(self):
		return self.name

	def getNumOfUsers(self):
		return len(UserProfile.objects.filter(shed=self))

	def getNumOfTools(self):
		return len(Tool.objects.filter(shed=self))

class UserProfile(User):
	"""
	Extends Django User class
	Represents a user in the DB
	"""
	# User zipcode
	location = models.CharField(max_length=5)
	
	# User status
	coordinator = models.BooleanField(default = False) #is the user a shed coordinator?
	borrower = models.BooleanField(default = False) #is the user borrowing a tool?
	admin = models.BooleanField(default = False) #is the user an admin?

	# number of tools user has
	numTools = models.IntegerField(default = 0)
	
	shed = models.ForeignKey(Shed, null=True, blank=True)


class Tool(models.Model):
	"""
	Represents a tool in the DB
	"""
	#Tool information
	name = models.CharField(max_length = 50)
	
	toolCondition = models.IntegerField('Condition (1-5)', default=3)
	
	#condition = models.CharField(max_length = 2,
	#                                 choices = TOOL_CONDITION_CHOICES)


	#brief description of tool
	description = models.CharField(max_length = 250)

	#is the tool available to share?
	availability = models.BooleanField(default=True)

	#is the tool in the shed?
	inShed = models.BooleanField(default=True)

	owner = models.ForeignKey(User, related_name='ownedTools')
	borrower = models.ForeignKey(User,null=True, blank=True, related_name='borrowedTools')
	#prevOwners 

	shed = models.ForeignKey(Shed, null=False,blank=False)
	
	def __str__(self):
		return self.name