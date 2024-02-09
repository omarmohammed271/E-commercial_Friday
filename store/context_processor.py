from django.shortcuts import render
from .models import Offer
def offers(request):
    offers = Offer.objects.all().filter(is_active=True)
    offer_count = offers.count()

    return {'offers':offers,'offer_count':offer_count,}
