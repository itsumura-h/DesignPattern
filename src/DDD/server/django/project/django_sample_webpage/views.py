from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from django.shortcuts import render, HttpResponse, redirect
# from models.models import (
#     Auth,
#     User
# )
from models.orator import (
    Auth,
    User
)

# Create your views here.


class ManageUsersView(APIView):
    """一覧表示
    """

    def get(self, request):
        # users = User.objects.select_related().all()
        users = User.all()
        return render(request, 'django_sample_webpage/index.html', {'users': users})


class ManageUserView(APIView):
    """一件表示
    """
    def get(self, request, id):
        # user = User.objects.select_related().filter(id=id).first()
        user = User.select('id', 'name', 'auth').find(id)
        resonse = render(request, 'django_sample_webpage/show.html', {'user': user})
        token = request.session
        print(vars(token))
        HttpResponse.set_cookie(resonse, 'sessionid', token)
        return resonse


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
    authentication_classes = (SessionAuthentication)
    def get(self, request, id):
        """編集ページ
        """
        # auth_list = Auth.objects.all()
        # user = User.objects.select_related().filter(id=id).first()
        auth_list = Auth.all()
        user = User.select('id', 'name', 'auth').find(id)
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
        # user = User.objects.filter(id=id).first()
        # user.name = name
        # user.auth_id = auth_id
        # user.save()
        User.where('id', id) \
            .update({
                'name': name,
                'auth_id': auth_id
            })
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
