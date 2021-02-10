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
    image = ImageSerializer()
    company = CompanySerializer()
    class Meta:
        model = Car
        fields = [ 'username' , 'image', 'company', 'name', 'accident_history', 'price' ]

    def create(self, validated_data):
        image_data = validated_data.pop('image')
        company_data = validated_data.pop('company')
        car = Car.objects.create(**validated_data)
        Image.objects.create(car=car, **image_data)
        Company.objects.create(car=car, **company_data)
        return car


