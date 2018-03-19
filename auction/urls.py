from django.conf.urls import url
from views import  auction_details, index
from apiviews import  AuctionDetail, AuctionList, BidView
urlpatterns = [
	# url('^$', index, name = "index"),
	# url('^item/(?P<id>[0-9-])$', auction_details, name = "auction_details"),
	url('^$', AuctionList.as_view(), name = 'auction_list'),
	url('^item$', AuctionList.as_view(), name = 'auction_list'),
	url('^item/(?P<id>[0-9-])$', AuctionDetail.as_view(), name = 'auction_detail'),
	url('^item/(?P<id>[0-9-])/bid$', BidView.as_view(), name = 'bid_view')
]