from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from . import utils

def get_fake_quote(request):

    return JsonResponse(utils.get_fake_quote())

@login_required
def get_random_fake_quote(request):

    return JsonResponse(utils.generate_fake_quote())

@login_required
def generate_new_daily_quote(request):

    return JsonResponse(utils.generate_fake_quote(daily_quote=True))
