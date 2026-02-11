from rest_framework import serializers
from .models import Products, TestDrive, BodyColor, InteriorColor, ExteriorFeatures, InteriorFeatures


class BodyColorSerializers(serializers.ModelSerializer):
    class Meta:
        model = BodyColor
        fields = '__all__'


class InteriorColorSerializers(serializers.ModelSerializer):
    class Meta:
        model = InteriorColor
        fields = '__all__'


class ExteriorFeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExteriorFeatures
        fields = '__all__'


class InteriorFeaturesSerializers(serializers.ModelSerializer):
    class Meta:
        model = InteriorFeatures
        fields = '__all__'


class ProductSerializers(serializers.ModelSerializer):
    title_modern = serializers.SerializerMethodField(method_name='transform_title')
    body_color_info = BodyColorSerializers(many=True, read_only=True)
    interior_color_info = InteriorColorSerializers(many=True, read_only=True)
    exterior_features_info = ExteriorFeaturesSerializer(many=True, read_only=True)
    interior_features_info = InteriorFeaturesSerializers(many=True, read_only=True)

    class Meta:
        model = Products
        fields = '__all__'

    def transform_title(self, products: Products):
        return 'ZEEKR ' + str(products.title)


class TestDriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestDrive
        fields = ['name_customer', 'phone_number_customer']


class TelegramAuthSerializer(serializers.Serializer):
    telegram_id = serializers.IntegerField()
    username = serializers.CharField(required=False)

