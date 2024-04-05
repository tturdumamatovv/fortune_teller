from rest_framework import serializers
from .models import Service, Comment, Certificate


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'name', 'text']


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['id', 'image']


class ServiceSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    certificates = CertificateSerializer(many=True, read_only=True)
    additional_texts = serializers.ListField(child=serializers.CharField(), source='get_additional_texts_list')

    class Meta:
        model = Service
        fields = ['id', 'title', 'main_text', 'additional_texts', 'comments', 'certificates']
