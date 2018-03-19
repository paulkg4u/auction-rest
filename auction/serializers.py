from rest_framework import serializers

from models import AuctionItem, Bidder

class BidderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Bidder
		fields = "__all__"


class AuctionItemSerializer(serializers.ModelSerializer):
	currentBidder = BidderSerializer(required=False)
	class Meta:
		model = AuctionItem
		fields = '__all__'


class AuctionItemMinimalSerializer(serializers.ModelSerializer):
	class Meta:
		model = AuctionItem
		fields = ('itemName','itemDescription','startTime','endTime', 'currentBid', 'id')

