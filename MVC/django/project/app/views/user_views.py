from django.shortcuts import render
from rest_framework.views import APIView

class UserCreateView(APIView):
    def get(self, request):
        return render(request, 'app/users/create.html')
