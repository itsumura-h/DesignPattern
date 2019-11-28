from django.contrib.auth import views
from django.http import request 


from inspect import getmembers
from pprint import pprint

class PasswordViews(views.PasswordResetView):
    def __init__(self):
        print('追加の処理')
        pprint(getmembers(self))
        # if self.request.method == 'POST':
        #     print(self.request.data)
