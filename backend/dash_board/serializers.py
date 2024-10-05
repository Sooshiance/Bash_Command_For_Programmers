from rest_framework import serializers


class ProjectSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    url = serializers.CharField(required=False)
    created_at = serializers.DateTimeField(required=False)


class ExperienceSerializer(serializers.Serializer):
    job_title = serializers.CharField(required=False)
    company = serializers.CharField(required=False)


class CertificationSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    issuing_organization = serializers.CharField(required=False)
