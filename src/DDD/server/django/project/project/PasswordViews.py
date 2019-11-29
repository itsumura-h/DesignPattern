from django.contrib.auth import views
# from django.http import request 


from inspect import getmembers
from pprint import pprint

# パスワードリセットするクラスを継承している ↓
class PasswordViews(views.PasswordResetView):
    def post(self, request):
        email = request._post['email']
        print(email)
        return super().post(self, request)