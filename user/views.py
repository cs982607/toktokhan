from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import User
from .serializers import UserSerializer


class UserSerializerView(UserSerializer):
    """
        회원가입을 하거나 로그인하는 API
        ---
        # 내용
            - email    : 이메일
            - password : 패스워드
    """

    @api_view(['POST'])
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)




