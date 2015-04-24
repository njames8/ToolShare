""" 
file: test.py
language: python3
author: Andrew Carpenter 
description: tests the app
"""

from django.test import TestCase
from .models import User

# Create your tests here.

class UserTest(TestCase):
	def setUp(self):
		User.objects.makeUser(fname="Jon", lname="Doe", email="jd@mail.com", password="jondoe", location=14623)
	
	def test_make_user(self):
		jd = User.objects.get(fname="Jon")