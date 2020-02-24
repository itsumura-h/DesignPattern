from django.shortcuts import render, redirect, HttpResponse
from rest_framework.views import APIView
from models.orator import (
    User,
    MicroPost
)

# Create your views here.


class ApplicationListViews(APIView):
    def get(self, request):
        return HttpResponse('hello world!')


class UserListViews(APIView):
    def get(self, request):
        users = User.get().serialize()
        return render(request, 'toy_app/users/index.html', {'users': users})

    def post(self, request):
        name = request.data['name']
        email = request.data['email']
        User.insert({
            'name': name,
            'email': email
        })
        return redirect('/toy_app/users/')


class UserDetailViews(APIView):
    def get(self, request, id):
        user = User.find(id).serialize()
        name = user['name']
        email = user['email']
        return render(
            request,
            'toy_app/users/show.html',
            {'id': id, 'name': name, 'email': email}
        )

    def post(self, request, id):
        name = request.data['name']
        email = request.data['email']
        User.where('id', id).update({
            'name': name,
            'email': email
        })
        return redirect(f'/toy_app/users/{id}/')


class UserCreateViews(APIView):
    def get(self, request):
        return render(request, 'toy_app/users/create.html')

    def post(self, request):
        name = request.data['name']
        email = request.data['email']
        print(name, email)
        return render(
            request,
            'toy_app/users/create_confirm.html',
            {'name': name, 'email': email}
        )


class UserEditViews(APIView):
    def get(self, request, id):
        user = User.find(id).serialize()
        name = user['name']
        email = user['email']
        return render(
            request,
            'toy_app/users/edit.html',
            {'name': name, 'email': email}
        )

    def post(self, request, id):
        name = request.data['name']
        email = request.data['email']
        print(name, email)
        return render(
            request,
            'toy_app/users/edit_confirm.html',
            {'id': id, 'name': name, 'email': email}
        )


class UserDeleteViews(APIView):
    def get(self, request, id):
        User.where('id', id).delete()
        return redirect('/toy_app/users/')


class MicropostsListViews(APIView):
    def get(self, request):
        posts = MicroPost.get().serialize()
        return render(
            request,
            'toy_app/microposts/index.html',
            {'posts': posts}
        )

    def post(self, request):
        content = request.data['content']
        user_id = request.data['user_id']
        MicroPost.insert({
            'content': content,
            'user_id': user_id
        })
        return redirect('/toy_app/microposts/')


class MicropostsDetailViews(APIView):
    def get(self, request, id):
        posts = MicroPost.find(id).serialize()
        content = posts['content']
        user_id = posts['user_id']
        return render(
            request,
            'toy_app/microposts/show.html',
            {'id': id, 'content': content, 'user_id': user_id}
        )


class MicropostsCreateViews(APIView):
    def get(self, request):
        return render(request, 'toy_app/microposts/create.html')

    def post(self, request):
        content = request.data['content']
        user_id = request.data['user_id']

        errors = {}
        if len(content) > 140:
            errors['content'] = ['content should less than 140']

        if len(user_id) == 0:
            errors['user_id'] = ['user_id is required']

        if len(errors) > 0:
            return render(
                request,
                'toy_app/microposts/create.html',
                {'errors': errors, 'content': content, 'user_id': user_id}
            )

        return render(
            request,
            'toy_app/microposts/create_confirm.html',
            {'content': content, 'user_id': user_id}
        )


class MicropostsEditViews(APIView):
    pass


class MicropostsDeleteViews(APIView):
    pass
