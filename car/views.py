from django.contrib.auth.decorators import login_required
from rest_framework import viewsets

from .models import Car, Image, Company
from .serializers import CarSerializer,ImageSerializer,CompanySerializer

class CarViewSet(viewsets.ModelViewSet):
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
    queryset = Car.objects.select_related('company', 'image').all()
    serializer_class = CarSerializer



