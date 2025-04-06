from datetime import date

from django.http import Http404
from django.shortcuts import render

from .models import Phrase, Thinker

from . import utils

# Create your views here

def show_daily_quote_page(request):

    try:
        retrieved_quote = utils.get_fake_quote()

    except Phrase.DoesNotExist:
        raise Http404
    except Thinker.DoesNotExist:
        raise Http404

    ## Put in a context the found quote and extra useful infos
    my_context = {

        "current_year": date.today().year,
        **retrieved_quote

    }

    return render(request, "base.html", my_context)


def show_frame_quote_page(request):

    try:
        retrieved_quote = utils.get_fake_quote()

    except Phrase.DoesNotExist:
        raise Http404
    except Thinker.DoesNotExist:
        raise Http404

    ## Put in a context the found quote and extra useful infos
    my_context = {

        "current_year": date.today().year,
        **retrieved_quote

    }

    return render(request, "frame.html", my_context)
