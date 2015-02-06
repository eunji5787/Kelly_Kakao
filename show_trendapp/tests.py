from unittest import TestCase
from show_trendapp.models import *
from django.utils import timezone
from django.core.urlresolvers import reverse
from show_trendapp.forms import *
from django.core.exceptions import ValidationError
import unittest

class FirstTest(unittest.TestCase):
	def setUp(self):
		Url_db.objects.create(fname ="20160101_1.txt", yyyy= "2016", mm="01", hh="01", dd= "01")
		Url_db.objects.create(fname ="20140101_2.txt", yyyy= "2014", mm="01", hh="02", dd= "01")

	def test_filename(self):
		invalid_filename = "2016"
		testObj = Url_db(fname = invalid_filename)
		self.assertEqual(testObj.test_error(), 123 )
		

