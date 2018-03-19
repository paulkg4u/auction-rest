# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Bidder(models.Model):
	name = models.CharField(max_length=250)
	email = models.CharField(max_length=250, unique=True, primary_key=True)

	def __unicode__(self):
		return self.name

class AuctionItem(models.Model):
	itemName = models.CharField(max_length=200)
	itemDescription = models.TextField(default="")
	startTime = models.DateTimeField()
	endTime = models.DateTimeField()
	currentBidder = models.ForeignKey(Bidder, blank=True, null=True)
	bidAmount = models.IntegerField(default=0)
	currentBid = models.IntegerField(default=0)
	itemImage = models.URLField(default="")

	def __unicode__(self):
		return  self.itemName