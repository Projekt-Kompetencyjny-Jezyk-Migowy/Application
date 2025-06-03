from django.contrib.auth.models import User
from django.db import models


class Section(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    difficulty_level = models.PositiveSmallIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Lesson(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    show_image = models.URLField(blank=True, null=True)
    gesture_name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='draft')  # np. draft, published
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('section', 'title')
        ordering = ['section', 'title']

    def __str__(self):
        return f"{self.section.name} - {self.title}"


class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Mężczyzna'),
        ('F', 'Kobieta'),
        ('O', 'Inna'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)

    def __str__(self):
        return f"Profil użytkownika {self.user.username}"


class UserSection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_sections')
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='user_sections')
    unlocked = models.BooleanField(default=False)
    unlocked_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('user', 'section')
        indexes = [
            models.Index(fields=['user', 'section']),
            models.Index(fields=['unlocked']),
        ]

    def __str__(self):
        status = 'Odblokowana' if self.unlocked else 'Zablokowana'
        return f"{self.user.username} - {self.section.name} - {status}"


class UserLessonProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lesson_progress')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='user_progress')
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('user', 'lesson')
        indexes = [
            models.Index(fields=['user', 'lesson']),
            models.Index(fields=['completed']),
        ]

    def __str__(self):
        status = 'Ukończona' if self.completed else 'Nieukończona'
        return f"{self.user.username} - {self.lesson.title} - {status}"
