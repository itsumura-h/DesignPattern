from django.contrib.auth import views

# パスワードリセットするクラスを継承している ↓
class PasswordViews(views.PasswordResetView):
    def post(self, request):
        email = request._post['email']
        print(email)
        return super().post(self, request)