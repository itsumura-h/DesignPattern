from django.urls import path
from .views import (
    ManageUsersView,
    ManageUserView,
    ManageUserCreateView,
    ManageUserEditView,
    ManageUserDeleteView
)

web_page_urls = [
    path('', ManageUsersView.as_view()),
    path('<int:id>/', ManageUserView.as_view()),
    path('create/', ManageUserCreateView.as_view()),
    path('<int:id>/edit/', ManageUserEditView.as_view()),
    path('<int:id>/delete/', ManageUserDeleteView.as_view())
]
