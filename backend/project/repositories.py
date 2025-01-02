from project.models import (
    Project,
    Post,
    Skill,
    Testimonial,
    ContactMessage,
    Education,
    Experience,
    Certification,
)


class ProjectRepository:
    def get_all_projects(self):
        return Project.objects.all()

    def get_project_by_sku(self, sku):
        return Project.objects.get(sku=sku)

    def create_project(self, user, title, description, image=None, url=None):
        project = Project(
            user=user, title=title, description=description, image=image, url=url
        )
        project.save()
        return project

    def update_project(self, sku, **kwargs):
        Project.objects.get(sku=sku).update(**kwargs)

    def delete_project(self, sku):
        Project.objects.get(sku=sku).delete()


class PostRepository:
    def get_all_post(self):
        return Post.objects.all()

    def get_post_by_sku(self, sku):
        return Post.objects.get(sku=sku)

    def create_post(self, title, content, author):
        project = Post(
            title=title,
            content=content,
            author=author,
        )
        project.save()
        return project

    def update_post(self, sku, **kwargs):
        Post.objects.get(sku=sku).update(**kwargs)

    def delete_post(self, sku):
        Post.objects.get(sku=sku).delete()


class SkillRepository:
    def get_all_skills(self):
        return Skill.objects.all()

    def get_skill_by_sku(self, sku):
        return Skill.objects.get(sku=sku)

    def create_skill(self, user, name, proficiency):
        project = Skill(user=user, name=name, proficiency=proficiency)
        project.save()
        return project

    def update_skill(self, sku, **kwargs):
        Skill.objects.get(sku=sku).update(**kwargs)

    def delete_skill(self, sku):
        Skill.objects.get(sku=sku).delete()


class TestimonialRepository:
    def get_all_testimonials(self):
        return Testimonial.objects.all()

    def get_testimonial_by_sku(self, sku):
        return Testimonial.objects.get(sku=sku)

    def create_testimonial(self, user, name, content, position, company):
        testimonial = Testimonial(
            user=user, name=name, content=content, position=position, company=company
        )
        testimonial.save()
        return testimonial

    def update_testimonial(self, sku, **kwargs):
        Testimonial.objects.get(sku=sku).update(**kwargs)

    def delete_testimonial(self, sku):
        Testimonial.objects.get(sku=sku).delete()


class ContactMessageRepository:
    def get_all_contact_messages(self):
        return ContactMessage.objects.all()

    def get_contact_message_by_sku(self, sku):
        return ContactMessage.objects.get(sku=sku)

    def create_contact_message(self, user, name, email, message):
        contact_message = ContactMessage(
            user=user, name=name, email=email, message=message
        )
        contact_message.save()
        return contact_message

    def update_contact_message(self, sku, **kwargs):
        ContactMessage.objects.get(sku=sku).update(**kwargs)

    def delete_contact_message(self, sku):
        ContactMessage.objects.get(sku=sku).delete()


class EducationRepository:
    def get_all_educations(self):
        return Education.objects.all()

    def get_education_by_sku(self, sku):
        return Education.objects.get(sku=sku)

    def create_education(self, user, degree, institution, graduation_date, description):
        education = Education(
            user=user,
            degree=degree,
            institution=institution,
            graduation_date=graduation_date,
            description=description,
        )
        education.save()
        return education

    def update_education(self, sku, **kwargs):
        Education.objects.get(sku=sku).update(**kwargs)

    def delete_education(self, sku):
        Education.objects.get(sku=sku).delete()


class ExperienceRepository:
    def get_all_experiences(self):
        return Experience.objects.all()

    def get_experience_by_sku(self, sku):
        return Experience.objects.get(sku=sku)

    def create_experience(
        self, user, job_title, company, start_date, end_date, description
    ):
        experience = Experience(
            user=user,
            job_title=job_title,
            company=company,
            start_date=start_date,
            end_date=end_date,
            description=description,
        )
        experience.save()
        return experience

    def update_experience(self, sku, **kwargs):
        Experience.objects.get(sku=sku).update(**kwargs)

    def delete_experience(self, sku):
        Experience.objects.get(sku=sku).delete()


class CertificationRepository:
    def get_all_certifications(self):
        return Certification.objects.all()

    def get_certification_by_sku(self, sku):
        return Certification.objects.get(sku=sku)

    def create_certification(
        self, user, name, issuing_organization, issue_date, expiration_date, description
    ):
        certification = Certification(
            user=user,
            name=name,
            issuing_organization=issuing_organization,
            issue_date=issue_date,
            expiration_date=expiration_date,
            description=description,
        )
        certification.save()
        return certification

    def update_certification(self, sku, **kwargs):
        Certification.objects.get(sku=sku).update(**kwargs)

    def delete_certification(self, sku):
        Certification.objects.get(sku=sku).delete()
