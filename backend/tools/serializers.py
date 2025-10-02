from rest_framework import serializers
from .models import Tool, University, Major


class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = ['id', 'name', 'description', 'icon', 'category', 'is_active', 'order', 'url']
        read_only_fields = ['id']


class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = ['id', 'name', 'name_en', 'degree_type', 'duration', 'tuition', 'currency', 'requirements', 'description']
        read_only_fields = ['id']


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ['id', 'name', 'name_en', 'region', 'country', 'city', 'ranking', 'website', 'description', 'logo']
        read_only_fields = ['id']


class UniversityDetailSerializer(serializers.ModelSerializer):
    majors = MajorSerializer(many=True, read_only=True)
    major_count = serializers.IntegerField(source='majors.count', read_only=True)

    class Meta:
        model = University
        fields = ['id', 'name', 'name_en', 'region', 'country', 'city', 'ranking', 'website', 'description', 'logo', 'majors', 'major_count']
        read_only_fields = ['id']
