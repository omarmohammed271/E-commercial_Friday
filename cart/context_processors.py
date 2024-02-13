from .models import Cart_item

def cart_count(request):
    items = Cart_item.objects.all().filter(is_active=True)
    items_count = items.count()
    return {'items_count':items_count}

