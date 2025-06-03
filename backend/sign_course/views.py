from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

from .models import Section, Lesson, UserSection, UserLessonProgress, UserProfile
from .serializers import UserSerializer, SectionSerializer, LessonSerializer, UserLessonProgressSerializer

from rest_framework import serializers

# Dodany brakujący serializer profilu użytkownika
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['birth_date', 'gender']

# Rejestracja użytkownika
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Logowanie użytkownika (z sesją)
@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    user = authenticate(username=request.data['username'], password=request.data['password'])
    if user:
        login(request, user)
        return Response({"message": "Logged in"})
    return Response({"error": "Invalid credentials"}, status=401)

# Wylogowanie użytkownika
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    logout(request)
    return Response({"message": "Logged out"})

# Lista sekcji
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_sections(request):
    sections = Section.objects.all()
    user_sections = UserSection.objects.filter(user=request.user)
    unlocked_ids = [us.section.id for us in user_sections if us.unlocked]
    data = [
        {
            "id": sec.id,
            "name": sec.name,
            "description": sec.description,
            "unlocked": sec.id in unlocked_ids
        }
        for sec in sections
    ]
    return Response(data)

# Szczegóły sekcji
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def section_detail(request, section_id):
    try:
        section = Section.objects.get(id=section_id)
        lessons = Lesson.objects.filter(section=section)
        data = SectionSerializer(section).data
        data['lessons'] = LessonSerializer(lessons, many=True).data
        return Response(data)
    except Section.DoesNotExist:
        return Response({"error": "Not found"}, status=404)

# Odblokowanie sekcji
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlock_section(request, section_id):
    try:
        section = Section.objects.get(id=section_id)
        if section_id > 1:
            previous_section = Section.objects.get(id=section_id - 1)
            if not UserSection.objects.filter(user=request.user, section=previous_section, unlocked=True).exists():
                return Response({"error": "Previous section not unlocked"}, status=403)

        user_section, _ = UserSection.objects.get_or_create(user=request.user, section=section)
        user_section.unlocked = True
        user_section.save()
        return Response({"message": "Section unlocked"})
    except Section.DoesNotExist:
        return Response({"error": "Section not found"}, status=404)

# Szczegóły lekcji
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def lesson_detail(request, lesson_id):
    try:
        lesson = Lesson.objects.get(id=lesson_id)
        return Response(LessonSerializer(lesson).data)
    except Lesson.DoesNotExist:
        return Response({"error": "Lesson not found"}, status=404)

# Oznaczenie lekcji jako ukończonej
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def complete_lesson(request, lesson_id):
    progress, _ = UserLessonProgress.objects.get_or_create(user=request.user, lesson_id=lesson_id)
    progress.completed = True
    progress.save()
    return Response({"message": "Lesson marked as complete"})

# Pobranie postępu użytkownika
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_progress(request):
    lessons = UserLessonProgress.objects.filter(user=request.user, completed=True)
    return Response({"completed_lessons": [l.lesson.id for l in lessons]})

# Sprawdzenie autoryzacji
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def check_auth(request):
    return Response({"authenticated": True, "username": request.user.username})

# Panel użytkownika
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_dashboard(request):
    unlocked_sections = UserSection.objects.filter(user=request.user, unlocked=True)
    completed_lessons = UserLessonProgress.objects.filter(user=request.user, completed=True)

    return Response({
        "unlocked_sections": SectionSerializer([us.section for us in unlocked_sections], many=True).data,
        "completed_lessons": LessonSerializer([c.lesson for c in completed_lessons], many=True).data
    })

# Reset postępu
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def reset_progress(request):
    UserLessonProgress.objects.filter(user=request.user).delete()
    UserSection.objects.filter(user=request.user).delete()
    return Response({"message": "Progress reset"})

# Oznaczenie lekcji jako nieukończonej
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def uncomplete_lesson(request, lesson_id):
    try:
        progress = UserLessonProgress.objects.get(user=request.user, lesson_id=lesson_id)
        progress.completed = False
        progress.save()
        return Response({"message": "Lesson marked as incomplete"})
    except UserLessonProgress.DoesNotExist:
        return Response({"error": "No progress to update"}, status=404)

# JWT logowanie
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            })
        return Response({"error": "Nieprawidłowe dane logowania"}, status=status.HTTP_401_UNAUTHORIZED)

# Widok profilu użytkownika
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile = UserProfile.objects.get(user=request.user)
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)
