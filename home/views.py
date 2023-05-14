import requests as req
import uuid
from django.shortcuts import render, redirect, HttpResponse
from products.models import Categories, MyOrder, Product
from django.http import Http404
from django.views.generic import ListView
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from django.db.models import F, Q, Sum

# Create your views here.


def home(request):
    all_product = Product.objects.filter(is_available=True).all()
    context = {
        "active_nav": "home",
        "best_sellers": all_product.order_by('-total_sales')[:8],
        "new_arrivals": all_product.order_by('-create_date')[:8],
        "trending": all_product.order_by('total_click')[:8]
    }
    return render(request, 'home/home.html', context)


@login_required
def my_cart(request):
    oid = uuid.uuid4()
    products = MyOrder.objects.filter(my_user=request.user, is_paid=False)
    products.update(order_id=oid)
    total = 0
    for product in products:
        product_price = product.quantity*product.product.price
        total += product_price
    context = {
        "products": products,
        "total": total,
        "pid": oid
    }
    return render(request, 'home/cart.html', context)


def product_details(request, id):

    # try:
    product = Product.objects.get(id=id)

    # print(product.categories.all())
    try:
        related_product = Product.objects.filter(
            categories__in=product.categories.all()).exclude(pk=product.pk)[:4]
    except:
        related_product = None
    context = {
        "product": product,
        "realated_products": related_product
    }
    return render(request, 'home/product_details.html', context)


# class AllProductListView(ListView):
#     model = Product
#     template_name = "home/all_product.html"
#     paginate_by = 9
#     context_object_name="products"


class ProductSearch(ListView):
    model = Product
    template_name = "home/search.html"
    paginate_by = 9
    context_object_name = 'products'

    def get_queryset(self, *args, **kwargs):
        search_parameter = self.request.GET.get('search')
        price_range = self.request.GET.get('price')
        category = self.request.GET.get('categories')
        sorting = self.request.GET.get('sorting')

        all_product = Product.objects.all().order_by('total_click')

        if search_parameter:
            all_product = all_product.filter(Q(name__icontains=search_parameter) | Q(
                categories__name__icontains=search_parameter) | Q(tags__icontains=search_parameter))

        if price_range:
            if price_range == '1':
                print(price_range)
                all_product = all_product.filter(price__gt=0, price__lte=500)
            elif price_range == '2':
                all_product = all_product.filter(
                    price__gt=500, price__lte=1000)
            elif price_range == '3':
                all_product = all_product.filter(
                    price__gt=1000, price__lte=5000)
            elif price_range == '4':
                all_product = all_product.filter(
                    price__gt=5000, price__lte=10000)
            elif price_range == '5':
                all_product = all_product.filter(price__gte=10000)

        if category:
            all_product = all_product.filter(
                categories__name__icontains=category)

        if sorting:
            if sorting == 'low':
                all_product = all_product.order_by('price')
            elif sorting == 'high':
                all_product = all_product.order_by('-price')

        return all_product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Categories.objects.all()
        context["search"] = self.request.GET.get('search', '')
        context["mycategory"] = self.request.GET.get('categories', '')
        context["myprice"] = self.request.GET.get('price', '')
        context['mysorting'] = self.request.GET.get('sorting', '')
        return context


def esewa_success(request):

    import xml.etree.ElementTree as ET
    data = request.GET.copy()
    url = "https://uat.esewa.com.np/epay/transrec"

    d = {
        'amt': data['amt'],
        'scd': 'EPAYTEST',
        'rid': data['refId'],
        'pid': data['oid'],
    }

    resp = req.post(url, d)
    root = ET.fromstring(resp.content)
    status = root[0].text.strip()

    if status == 'Success':

        MyOrder.objects.filter(
            order_id=data['oid']
        ).update(
            is_paid=True
        )
        return redirect(f'/order_details/{data["oid"]}')
    else:
        return HttpResponse('failure')


@login_required()
def my_order(request):
    my_order = MyOrder.objects.filter(
        my_user=request.user).filter(is_paid=True)
    rewards_point = my_order.aggregate(
        Total=(Sum('product__price') / 1000))['Total']
    print(my_order.aggregate(Total=(Sum('product__price'))))
    orders = set(
        my_order.values_list('order_id', 'is_paid', 'is_order_sent', 'is_order_delivered'))
    context = {'my_orders': orders, 'rewards_point': rewards_point}
    return render(request, 'home/my_order.html', context)


@login_required()
def view_order_details(request, orderid):
    order_details = MyOrder.objects.filter(
        order_id=orderid).filter(my_user=request.user)
    context = {'my_orders': order_details}
    return render(request, 'home/order_details.html', context)


def view_customer_product(request):
    context = {
        'products': Product.objects.filter(is_available=True).filter(user__is_superuser=False).filter(stock__gt=0).order_by('-create_date'),
        "categories": Categories.objects.all()
    }
    return render(request, 'home/search.html', context)
