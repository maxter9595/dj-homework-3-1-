from django.shortcuts import render

from phones.models import Phone


def show_catalog(request):
    sort_dict = {
        'name': 'name',
        'min_price': 'price',
        'max_price': '-price'
    }
    context = {
        'phones': Phone.objects.all(). \
            order_by(sort_dict[request.GET.get('sort', 'name')])
    }
    return render(
        request=request,
        template_name='catalog.html',
        context=context,
    )


def show_product(request, slug):
    context = {
        'phone': Phone.objects.get(slug=slug)
    }
    return render(
        request=request,
        template_name='product.html',
        context=context
    )
