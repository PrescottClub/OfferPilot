from rest_framework import serializers
from .models import UserProfile, Application


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'id', 'target_regions', 'target_universities', 'target_majors',
            'ielts_score', 'toefl_score', 'gre_score', 'gmat_score',
            'gpa', 'undergraduate_school', 'major', 'graduation_year',
            'work_experience', 'research_experience', 'extracurricular', 'awards',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = [
            'id', 'university_name', 'major_name', 'degree_type', 'status',
            'application_date', 'deadline', 'result_date', 'notes',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
