from rest_framework import serializers
from .models import User, UserProfile

class SimpleRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    age = serializers.IntegerField(required=False)
    gender = serializers.CharField(required=False)
    location = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ('email', 'password', 'age', 'gender', 'location')

    def create(self, validated_data):
        age = validated_data.pop('age', None)
        gender = validated_data.pop('gender', '')
        location = validated_data.pop('location', '')
        password = validated_data.pop('password')

        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        UserProfile.objects.update_or_create(
            user=user,
            defaults={
                "age": age,
                "gender": gender,
                "location": location
            }
        )
        return user
