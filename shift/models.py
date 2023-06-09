from django.db import models
from venue.models import Venue
from booking.models import Booking
from django.contrib.auth.models import User

class Group(models.Model):
	name = models.CharField(max_length=200)
	members = models.ManyToManyField(User, blank=True, related_name='shift_groups')

	def __str__(self):
		return self.name

class Shift(models.Model):
	booking = models.ForeignKey(Booking, related_name='shifts', on_delete=models.CASCADE)
	group = models.ForeignKey(Group, related_name='shifts', on_delete=models.CASCADE)
	user = models.ForeignKey(User, blank=True, null=True, related_name='shifts', on_delete=models.CASCADE)
	name = models.CharField(max_length=200)

	def __str__(self):
		return "%s - %s" % (self.booking, self.name)

	class Meta:
		permissions = (
			("my_view_shift", "View shift"),
		)

class DefaultShiftSet(models.Model):
	venue = models.ForeignKey(Venue, related_name='shiftsets', on_delete=models.CASCADE)
	name = models.CharField(max_length=200)

	def __str__(self):
		return "%s - %s" % (self.venue, self.name)

class DefaultShift(models.Model):
	shiftset = models.ForeignKey(DefaultShiftSet, related_name='shifts', on_delete=models.CASCADE)
	group = models.ForeignKey(Group, related_name='default_shifts', on_delete=models.CASCADE)
	name = models.CharField(max_length=200)

	def __str__(self):
		return "%s - %s" % (self.shiftset, self.name)
