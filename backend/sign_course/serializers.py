from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Section, Lesson, UserLessonProgress, UserSection
from .models import UserProfile

class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    birth_date = serializers.DateField(write_only=True)
    gender = serializers.ChoiceField(choices=UserProfile.GENDER_CHOICES, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password2', 'birth_date', 'gender']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True}
        }

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Hasła nie są zgodne.")
        return data

    def create(self, validated_data):
        birth_date = validated_data.pop('birth_date')
        gender = validated_data.pop('gender')
        validated_data.pop('password2')

        user = User(
            username=validated_data['username'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()

        UserProfile.objects.create(user=user, birth_date=birth_date, gender=gender)

        return user

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class UserLessonProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLessonProgress
        fields = '__all__'