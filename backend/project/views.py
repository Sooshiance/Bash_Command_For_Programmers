from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from .serializers import (ProjectSerializer,
                          PostSerializer,
                          SkillSerializer,
                          TestimonialSerializer,
                          ContactMessageSerializer,
                          EducationSerializer,
                          ExperienceSerializer,
                          CertificationSerializer,)
from .services import (ProjectService,
                       PostService,
                       SkillService,
                       TestimonialService,
                       ContactMessageService,
                       EducationService,
                       ExperienceService,
                       CertificationService,)


class ProjectAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def __init__(self):
        self.service = ProjectService()

    def get(self, request, sku=None):
        if sku:
            project = self.service.get_project_by_sku(sku)
            srz = ProjectSerializer(project)
            return Response(srz.data, status=status.HTTP_200_OK)
        projects = self.service.get_all_projects()
        srz = ProjectSerializer(projects, many=True)
        return Response(srz.data, status=status.HTTP_200_OK)

    def post(self, request):
        project = self.service.create_project(
        user=request.user,
        title=request.data.get('title'),
        description=request.data.get('description'),
        image=request.data.get('image'),
        url=request.data.get('url')
        )
        srz = ProjectSerializer(project)
        return Response(srz.data, status=status.HTTP_201_CREATED)

    def put(self, request, sku):
        self.service.update_project(sku, **request.data)
        return Response(status=status.HTTP_205_RESET_CONTENT)

    def delete(self, request, sku):
        self.service.delete_project(sku)
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def __init__(self):
        self.service = PostService()

    def get(self, request, sku=None):
        if sku:
            post = self.service.get_post_by_sku(sku)
            srz = PostSerializer(post)
            return Response(srz.data, status=status.HTTP_200_OK)
        posts = self.service.get_all_posts()
        srz = PostSerializer(posts, many=True)
        return Response(srz.data, status=status.HTTP_200_OK)

    def post(self, request):
        post = self.service.create_post(
        title=request.data.get('title'),
        content=request.data.get('content'),
        author=request.user,
        )
        srz = PostSerializer(post)
        return Response(srz.data, status=status.HTTP_201_CREATED)

    def put(self, request, sku):
        self.service.update_post(sku, **request.data)
        return Response(status=status.HTTP_205_RESET_CONTENT)

    def delete(self, request, sku):
        self.service.delete_post(sku)
        return Response(status=status.HTTP_204_NO_CONTENT)


class SkillAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def __init__(self):
        self.service = SkillService()

    def get(self, request, sku=None):
        if sku:
            skill = self.service.get_skill_by_sku(sku)
            srz = SkillSerializer(skill)
            return Response(srz.data, status=status.HTTP_200_OK)
        skills = self.service.get_all_skills()
        srz = SkillSerializer(skills, many=True)
        return Response(srz.data, status=status.HTTP_200_OK)

    def post(self, request):
        skill = self.service.create_skill(
        user=request.user,
        name=request.data.get('name'),
        proficiency=request.data.get('proficiency')
        )
        srz = SkillSerializer(skill)
        return Response(srz.data, status=status.HTTP_201_CREATED)

    def put(self, request, sku):
        self.service.update_skill(sku, **request.data)
        return Response(status=status.HTTP_205_RESET_CONTENT)

    def delete(self, request, sku):
        self.service.delete_skill(sku)
        return Response(status=status.HTTP_204_NO_CONTENT)


class TestimonialAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def __init__(self):
        self.service = TestimonialService()

    def get(self, request, testimonial_id=None):
        if testimonial_id:
            testimonial = self.service.get_testimonial_by_id(testimonial_id)
            srz = TestimonialSerializer(testimonial)
            return Response(srz.data, status=status.HTTP_200_OK)
        testimonials = self.service.get_all_testimonials()
        srz = TestimonialSerializer(testimonials, many=True)
        return Response(srz.data, status=status.HTTP_200_OK)

    def post(self, request):
        testimonial = self.service.create_testimonial(
        user=request.user,
        name=request.data.get('name'),
        content=request.data.get('content'),
        position=request.data.get('position'),
        company=request.data.get('company')
        )
        srz = TestimonialSerializer(testimonial)
        return Response(srz.data, status=status.HTTP_201_CREATED)
    
    def put(self, request, testimonial_id):
        self.service.update_testimonial(testimonial_id, **request.data)
        return Response(status=status.HTTP_205_RESET_CONTENT)

    def delete(self, request, testimonial_id):
        self.service.delete_testimonial(testimonial_id)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ContactMessageAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def __init__(self):
        self.service = ContactMessageService()

    def get(self, request, sku=None):
        if sku:
            contact_message = self.service.get_contact_message_by_sku(sku)
            srz = ContactMessageSerializer(contact_message)
            return Response(srz.data, status=status.HTTP_200_OK)
        contact_messages = self.service.get_all_contact_messages()
        srz = ContactMessageSerializer(contact_messages, many=True)
        return Response(srz.data, status=status.HTTP_200_OK)

    def post(self, request):
        contact_message = self.service.create_contact_message(
        user=request.user,
        name=request.data.get('name'),
        email=request.data.get('email'),
        message=request.data.get('message')
        )
        srz = ContactMessageSerializer(contact_message)
        return Response(srz.data, status=status.HTTP_201_CREATED)

    def put(self, request, sku):
        self.service.update_contact_message(sku, **request.data)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, sku):
        self.service.delete_contact_message(sku)
        return Response(status=status.HTTP_204_NO_CONTENT)


class EducationAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def init(self):
        self.service = EducationService()

    def get(self, request, sku=None):
        if sku:
            education = self.service.get_education_by_sku(sku)
            srz = EducationSerializer(education)
            return Response(srz.data, status=status.HTTP_200_OK)
        educations = self.service.get_all_educations()
        srz = EducationSerializer(educations, many=True)
        return Response(srz.data, status=status.HTTP_200_OK)

    def post(self, request):
        education = self.service.create_education(
        user=request.user,
        degree=request.data.get('degree'),
        institution=request.data.get('institution'),
        graduation_date=request.data.get('graduation_date'),
        description=request.data.get('description')
        )
        srz = EducationSerializer(education)
        return Response(srz.data, status=status.HTTP_201_CREATED)
    
    def put(self, request, sku):
        self.service.update_education(sku, **request.data)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, sku):
        self.service.delete_education(sku)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ExperienceAPIView(APIView):
    def __init__(self):
        self.service = ExperienceService()

    def get(self, request, sku=None):
        if sku:
            experience = self.service.get_experience_by_sku(sku)
            srz = ExperienceSerializer(experience)
            return Response(srz.data, status=status.HTTP_200_OK)
        experiences = self.service.get_all_experiences()
        srz = ExperienceSerializer(experiences, many=True)
        return Response(experiences, status=status.HTTP_200_OK)

    def post(self, request):
        experience = self.service.create_experience(
        user=request.user,
        job_title=request.data.get('job_title'),
        company=request.data.get('company'),
        start_date=request.data.get('start_date'),
        url=request.data.get('url')
        )
        return Response(experience, status=status.HTTP_201_CREATED)

    def put(self, request, sku):
        self.service.update_experience(sku, **request.data)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, sku):
        self.service.delete_experience(sku)
        return Response(status=status.HTTP_204_NO_CONTENT)


class CertificationAPIView(APIView):
    def __init__(self):
        self.service = CertificationService()

    def get(self, request, sku=None):
        if sku:
            certification = self.service.get_certification_by_sku(sku)
            return Response(certification, status=status.HTTP_200_OK)
        certifications = self.service.get_all_certifications()
        return Response(certifications, status=status.HTTP_200_OK)

    def post(self, request):
        certification = self.service.create_certification(
        user=request.user,
        name=request.data.get('name'),
        issuing_organization=request.data.get('issuing_organization'),
        issue_date=request.data.get('issue_date'),
        expiration_date=request.data.get('expiration_date'),
        description=request.data.get('description'),
        )
        srz = CertificationSerializer(srz)
        return Response(srz.data, status=status.HTTP_201_CREATED)
    
    def put(self, request, sku):
        self.service.update_certification(sku, **request.data)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, sku):
        self.service.delete_experience(sku)
        return Response(status=status.HTTP_204_NO_CONTENT)
