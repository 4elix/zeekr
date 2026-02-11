from rest_framework import serializers
from .models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

    # переопределение метода для удаления объекта
    def delete(self):
        raise serializers.ValidationError('Удаление объекта News запрещено !!!')

