from functools import lru_cache

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from dal import autocomplete
from demo.models import Company
from demo.demo_functions import dictionary
from demo.demo_functions import dictionary2
from demo.demo_functions import filter_example
from demo.demo_functions import filter2_example


def index(request):
    return render(request, 'index.html')

def d(request):
    dictionary.associate_balances()
    return HttpResponse("Done")


def d2(request):
    dictionary2.associate_balances()
    return HttpResponse("Done")


def fil(request):
    return HttpResponse("The number of values divisible by 42 is {0}".format(filter_example.search_for_number()))


def fil2(request):
    return HttpResponse("The number of values divisible by 42 is {0}".format(filter2_example.search_for_number()))


def fil3(request):
    return HttpResponse("The number of values divisible by 42 is {0}".format(filter2_example.search_for_number()))


def get_company(request):
    qs = Company.objects.values()
    return JsonResponse(list(qs), safe=False)


def get_company_values(request):
    qs = Company.objects.all().values('id', 'symbol')
    return JsonResponse(list(qs), safe=False)


class CompanyAutoComplete(autocomplete.Select2QuerySetView):
    def get_result_label(self, result):
        return result.symbol

    @lru_cache(maxsize=None)
    def get_queryset(self):
        qs = Company.objects.all()

        if self.q:
            qs = qs.filter(symbol__istartswith=self.q)

        return qs
