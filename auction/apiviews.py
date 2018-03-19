from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from  rest_framework import  generics
from .models import AuctionItem, Bidder
from  .serializers import AuctionItemSerializer, AuctionItemMinimalSerializer, BidderSerializer


class Collection(object):
	def __init__(self):
		pass

class AuctionList(generics.ListCreateAPIView):
	queryset = AuctionItem.objects.all()
	serializer_class = AuctionItemSerializer


class AuctionDetail(generics.RetrieveDestroyAPIView):
	queryset = AuctionItem.objects.all()
	serializer_class = AuctionItemSerializer

class BidView(APIView):
	def put(self,request,id):
		reqObj = Collection()
		reqObj.id = id
		reqObj.email = request.data['email']
		reqObj.name = request.data['name']
		reqObj.amount = request.data['bidAmount']

		bidderObject = Bidder.objects.filter(email = reqObj.email)
		if len(bidderObject):
			bidderObject = bidderObject[0]
			if bidderObject.name != reqObj.email:
				bidder = BidderSerializer(bidderObject,data = {'name':reqObj.name, 'email':reqObj.email})
				if bidder.is_valid():
					bidderObject = bidder.save()
		else:
			bidder = BidderSerializer(data = {'name':reqObj.name, 'email':reqObj.email})
			if bidder.is_valid():
				bidderObject = bidder.save()
			else:
				print bidder.errors

		item = AuctionItem.objects.get(id = id)
		if item.currentBid < reqObj.amount:
			item.currentBid = reqObj.amount
			item.currentBidder = bidderObject
			data = AuctionItemSerializer(item).data
		else:
			data = {'status':'failure: need higher amount'}

		return  Response(data)


