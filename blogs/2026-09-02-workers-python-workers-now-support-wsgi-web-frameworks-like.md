---
title: "Workers - Python Workers now support WSGI web frameworks like Django and Flask"
url: "https://developers.cloudflare.com/changelog/post/2026-09-02-python-workers-web-framework-support/"
date: "2026-09-02"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Python web frameworks following the Web Server Gateway Interface (WSGI) ↗ or Asynchronous Server Gateway Interface (ASGI) ↗ specification can now be used in Python Workers. Using web frameworks with Python Workers Based on the web framework you are using, you can use either wsgi or asgi from the workers module. WSGI frameworks For WSGI frameworks like Django or Flask: from workers import wsgi from django.core.wsgi import get_wsgi_application app = get_wsgi_application() Default = wsgi.entrypoint(app) The wsgi.entrypoint is equivalent to creating a WorkerEntrypoint class and using the wsgi.fetc
