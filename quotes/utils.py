import json
import traceback

from django.conf import settings
from .models import Phrase, Thinker

def get_fake_quote():

    # Get a default dictionary/JSON to display if something goes wrong
    retrieved_quote = get_shallow_quote()

    # Get Redis instance from settings
    redis = settings.REDIS_INSTANCE

    # Try to get cached phrase from redis
    cached_quote_json = redis.get("daily-quote")

    if cached_quote_json:
        retrieved_quote = json.loads(cached_quote_json)

    else:

        # Get a random phrase, save it and return to who asked
        retrieved_quote = generate_fake_quote(daily_quote=True)

    # Use a variable to hold number of fake-quotes-requests

    redis.incr("api-calls-counter")

    return retrieved_quote

def generate_fake_quote(daily_quote=False):

    # Get a default dictionary/JSON to display if something goes wrong
    generated_fake_quote = get_shallow_quote()

    try:

        # Get Redis instance from settings
        redis = settings.REDIS_INSTANCE

        generated_fake_quote = {

            "Phrase" : Phrase.get_random(),
            "Thinker" : Thinker.get_random()

        }

        print("[PYTHON] New generated_fake_quote: ", generated_fake_quote)

        if daily_quote:

            # Cache this new quote inside REDIS

            fake_quote_json = json.dumps(generated_fake_quote)

            redis.set("daily-quote", fake_quote_json)
            redis.expire("daily-quote", 10800) # 3 Hours

            print("[REDIS] New daily-quote set: ", fake_quote_json)

    except:

        print("[PYTHON] ERROR WHILE GENERATING FAKE QUOTE:")
        traceback.print_exc()

    return generated_fake_quote

def get_shallow_quote():

    return {
        "Phrase": Phrase.get_default_value(),
        "Thinker": Thinker.get_default_value(),
    }
