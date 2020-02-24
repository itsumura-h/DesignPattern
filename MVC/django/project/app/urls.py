from django.urls import path, include
from app.views.static_page_views import (
    home,
    help,
    about
)
from app.views.app_views import (
    ListViews
)

static_pages_urls = [
    path('home/', home),
    path('help/', help),
    path('about/', about)
]

app_urls = [
    path('static_pages/', include(static_pages_urls)),
    path('', ListViews.as_view())
]
