from django.shortcuts import render
from django.http import HttpResponse
import appoptics_apm
# Create your views here.
from demo.demo_functions import dictionary
from demo.demo_functions import dictionary2
from demo.demo_functions import filter_example
from demo.demo_functions import filter2_example


def index(request):
    return HttpResponse("Hello world")


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
