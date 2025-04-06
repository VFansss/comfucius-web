
# comfucius-web

![Comfucius Banner](themes/dimension-comfucius/static/images/capsule.jpg)

> For your daily dose of misquoted, feel-good, self-referential wisdom.

**Comfucius** is a quote generator that produces completely fake, pseudo-philosophical sayings attributed to famous thinkers. Inspired by motivational social media posts, but with a wink.

👉 [Live demo](https://comfucius.xyz)

## 🧠 Features

- Fake quotes in the style of Confucius (but more cursed).
  - **Everyone gets the same quote**
  - Quote changes once in a while
- Lightweight, mobile-friendly frontend.

## 🛠️ Tech Stack

- **Backend**: Python 3.x, Django
- **Frontend**: HTML, CSS (Dimension theme derived from [HTML5Up](https://html5up.net/)/[Pixelarity](https://pixelarity.com/)), a sprinkle of JS
- **Database**: SQLite
- **Caching**: Redis

## ⚙️ Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/VFansss/comfucius-web.git
cd comfucius-web
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the development server

❗❗❗ Database is into it's own subdirectory, create it before below commands

```bash
mkdir database
```

then create actual database (flag is needed):

```bash
python manage.py migrate --run-syncdb
```

(Optional) Create admin user for admin console:

```bash
python manage.py createsuperuser
```

"Collect" the statics (so everything shows up right):

```bash
python manage.py collectstatic
```

Start the Redis server on the right port - check [Redis setup instructions](#🧰-redis-for-caching)

Finally, start the development server:

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

## 🧰 Redis for Caching

If you have Redis installed, Comfucius will use it to cache previously generated quotes.

You can configure the Redis hostname using an environment variable:

```bash
export COMFUCIUS_REDISHOST=localhost
```

Default Redis settings:

- Host: `localhost` (or value from `COMFUCIUS_REDISHOST`)
- Port: `6379`

## 📄 License

This project is licensed under the **MIT License**. See [`LICENSE.md`](LICENSE.md) for more information.

> ⚠️ All quotes are 100% fictional. No philosophers were harmed in the making of this website.
