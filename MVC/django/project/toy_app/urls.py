from django.urls import path
from toy_app.views import (
    ApplicationListViews,
    UserListViews,
    UserDetailViews,
    UserCreateViews,
    UserEditViews,
    UserDeleteViews,
    MicropostsListViews,
    MicropostsDetailViews,
    MicropostsCreateViews,
    MicropostsEditViews,
    MicropostsDeleteViews
)

toy_app_urls = [
    path('', ApplicationListViews.as_view()),
    path('users/', UserListViews.as_view()),
    path('users/<int:id>/', UserDetailViews.as_view()),
    path('users/create/', UserCreateViews.as_view()),
    path('users/<int:id>/edit/', UserEditViews.as_view()),
    path('users/<int:id>/delete/', UserDeleteViews.as_view()),

    path('microposts/', MicropostsListViews.as_view()),
    path('microposts/<int:id>/', MicropostsDetailViews.as_view()),
    path('microposts/create/', MicropostsCreateViews.as_view()),
    path('microposts/<int:id>/edit/', MicropostsEditViews.as_view()),
    path('microposts/<int:id>/delete/', MicropostsDeleteViews.as_view()),
]
