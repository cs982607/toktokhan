from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Car, Image, Company
from .serializers import CarSerializer,ImageSerializer,CompanySerializer

class CarSerializerView(CarSerializer):
    """
        차량정보를 저장하거나 불러오는 API
        ---
        # 내용
            - username         : 유저이름
            - name             : 차량 이름
            - accident_history : 사고이력
            - price            : 차량 가격
            - create_at        : 등록 날짜와 시간
            - update_at        : 수정 날짜와 시간
            - comany           : 제조사
            - image            : 이미지 사진
    """

    @api_view(['GET', 'POST'])
    def posts(request):
        if request.method == 'GET':
            posts = Car.objects.all()
            post_list = CarSerializer(posts, many=True)
            return Response(post_list.data)
        else:
            serializers = CarSerializer(data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=201)
            return Response(serializers.errors, status=400)

