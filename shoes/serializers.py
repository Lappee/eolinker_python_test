from .models import User, Shoe
from rest_framework import serializers


class ShoeSerializer(serializers.ModelSerializer):
    #id = serializers.IntegerField(read_only=True)
    #size = serializers.IntegerField()
    #color = serializers.CharField(max_length=20)

    #def create(self, validated_data):
    #    return Shoe.objects.cerate(**validated_data)

    #def update(self, instance, validated_data):
    #    instance.size = validated_data.get('size', instance.size)
    #    instance.color = validated_data.get('color', instance.color)
    #    instance.save()
    #    return instance

    class Meta:
        model = Shoe
        fields = ('id', 'size', 'color')


class UserSerializer(serializers.ModelSerializer):
    shoes = ShoeSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'name', 'phone', 'shoes')

    def create(self, validated_data):
        shoes_data = validated_data.pop('shoes')
        user = User.objects.create(**validated_data)
        for shoe_data in shoes_data:
            Shoe.objects.create(user=user, **shoe_data)
        return user
