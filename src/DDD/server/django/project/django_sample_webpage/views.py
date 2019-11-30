from rest_framework.views import APIView
from django.shortcuts import render, HttpResponse, redirect
from models.models import (
    Auth,
    User
)

# Create your views here.


class ManageUsersView(APIView):
    """一覧表示
    """

    def get(self, request):
        users = User.objects.select_related().all()
        return render(request, 'django_sample_webpage/index.html', {'users': users})


class ManageUserView(APIView):
    """一件表示
    """

    def get(self, request, id):
        user = User.objects.select_related().filter(id=id).first()
        return render(request, 'django_sample_webpage/show.html', {'user': user})


class ManageUserCreateView(APIView):
    def get(self, request):
        """新規作成ページ
        """
        auth_list = Auth.objects.all()
        return render(request, 'django_sample_webpage/create.html', {'auth_list': auth_list})

    def post(self, request):
        """新規作成
        """
        params = request.data
        name = params['name']
        auth_id = params['auth']
        User(name=name, auth_id=auth_id).save()
        return redirect('/WebPageSample/')


class ManageUserEditView(APIView):
    def get(self, request, id):
        """編集ページ
        """
        auth_list = Auth.objects.all()
        user = User.objects.select_related().filter(id=id).first()
        return render(
            request,
            'django_sample_webpage/edit.html',
            {
                'auth_list': auth_list,
                'user': user
            }
        )

    def post(self, request, id):
        """編集
        """
        params = request.data
        name = params['name']
        auth_id = params['auth']
        user = User.objects.filter(id=id).first()
        user.name = name
        user.auth_id = auth_id
        user.save()
        return redirect('/WebPageSample/')


class ManageUserDeleteView(APIView):
    def get(self, request, id):
        """削除ページ
        """
        return HttpResponse('削除ページ')

    def post(self, request):
        """削除
        """
        pass
