from rest_framework import serializers
from sale.models import City, PropertyType, PurchaseType, Property, PropertyFeature, PorpertyImage


class PorpertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PorpertyImage
        fields = '__all__'


class PropertySerializer(serializers.ModelSerializer):

    images = PorpertyImageSerializer(many=True, read_only=True)
    def validate_price(self,value):
        if not 0<value<900000:
            raise serializers.ValidationError("0dan boyuk 900000 az olmalidir")
            

    class Meta:
        model = Property
        fields = '__all__'
        depth = 1


class CitySerializer(serializers.ModelSerializer):
    propertys = PropertySerializer(many=True,read_only=True)
    propertys = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='property-details'
    )

    class Meta:
        model = City
        fields = ["id","title","propertys"]
