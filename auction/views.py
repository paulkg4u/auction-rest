# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from django.http import  JsonResponse


from models import AuctionItem
# Create your views here.
def index(request):
	MAX_ITEMS = 20
	auction_items = AuctionItem.objects.all()[:MAX_ITEMS]
	data = {'results':list(auction_items.values('id','itemName','itemDescription','startTime', 'endTime','itemImage'))}
	return JsonResponse(data)


def auction_details(request, id):
	auction_item = AuctionItem.objects.get(id = id)
	data = {}
	return  JsonResponse(data)

