from rest_framework.serializers import ModelSerializer
from .models import Car, Company, Image
from user.serializers import UserSerializer

class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']

class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = ['company_name']

class CarSerializer(ModelSerializer):
    image = ImageSerializer(read_only=True)
    company = CompanySerializer(read_only=True)
    class Meta:
        model = Car
        fields = [ 'username' , 'image', 'company', 'name', 'accident_history', 'price' ]

