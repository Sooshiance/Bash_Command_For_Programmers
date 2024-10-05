from .repositories import (ProjectRepository,
                           PostRepository,
                           SkillRepository,
                           TestimonialRepository,
                           ContactMessageRepository,
                           EducationRepository,
                           ExperienceRepository,
                           CertificationRepository)


class ProjectService:
    def __init__(self):
        self.repository = ProjectRepository()

    def get_all_projects(self):
        return self.repository.get_all_projects()

    def get_project_by_sku(self, sku):
        return self.repository.get_project_by_sku(sku)

    def create_project(self, user, title, description, image=None, url=None):
        return self.repository.create_project(user, title, description, image, url)

    def update_project(self, sku, **kwargs):
        self.repository.update_project(sku, **kwargs)

    def delete_project(self, sku):
        self.repository.delete_project(sku)


class PostService:
    def __init__(self):
        self.repository = PostRepository()

    def get_all_posts(self):
        return self.repository.get_all_post()

    def get_post_by_sku(self, sku):
        return self.repository.get_post_by_sku(sku)

    def create_post(self, user, title, content, author):
        return self.repository.create_post(user, title, content, author)

    def update_post(self, sku, **kwargs):
        self.repository.update_post(sku, **kwargs)

    def delete_post(self, sku):
        self.repository.delete_post(sku)


class SkillService:
    def __init__(self):
        self.repository = SkillRepository()

    def get_all_skills(self):
        return self.repository.get_all_skills()

    def get_skill_by_sku(self, sku):
        return self.repository.get_skill_by_sku(sku)

    def create_skill(self, user, name, proficiency):
        return self.repository.create_skill(user, name, proficiency)

    def update_skill(self, sku, **kwargs):
        self.repository.update_skill(sku, **kwargs)

    def delete_skill(self, sku):
        self.repository.delete_skill(sku)


class TestimonialService:
    def __init__(self):
        self.repository = TestimonialRepository()

    def get_all_testimonials(self):
        return self.repository.get_all_testimonials()

    def get_testimonial_by_id(self, sku):
        return self.repository.get_testimonial_by_sku(sku)

    def create_testimonial(self, user, name, content, position, company):
        return self.repository.create_testimonial(user, name, content, position, company)

    def update_testimonial(self, sku, **kwargs):
        self.repository.update_testimonial(sku, **kwargs)

    def delete_testimonial(self, sku):
        self.repository.delete_testimonial(sku)


class ContactMessageService:
    def __init__(self):
        self.repository = ContactMessageRepository()

    def get_all_contact_messages(self):
        return self.repository.get_all_contact_messages()

    def get_contact_message_by_sku(self, sku):
        return self.repository.get_contact_message_by_sku(sku)

    def create_contact_message(self, user, name, email, message):
        return self.repository.create_contact_message(user, name, email, message)

    def update_contact_message(self, sku, **kwargs):
        self.repository.update_contact_message(sku, **kwargs)

    def delete_contact_message(self, sku):
        self.repository.delete_contact_message(sku)


class EducationService:
    def __init__(self):
        self.repository = EducationRepository()

    def get_all_educations(self):
        return self.repository.get_all_educations()

    def get_education_by_sku(self, sku):
        return self.repository.get_education_by_sku(sku)

    def create_education(self, user, degree, institution, graduation_date, description):
        return self.repository.create_education(user, degree, institution, graduation_date, description)

    def update_education(self, sku, **kwargs):
        self.repository.update_education(sku, **kwargs)

    def delete_education(self, sku):
        self.repository.delete_education(sku)


class ExperienceService:
    def __init__(self):
        self.repository = ExperienceRepository()

    def get_all_experiences(self):
        return self.repository.get_all_experiences()

    def get_experience_by_sku(self, sku):
        return self.repository.get_experience_by_sku(sku)

    def create_experience(self, user,job_title,company,start_date,end_date,description):
        return self.repository.create_experience(user,job_title=job_title,company=company,
                                                 start_date=start_date,
                                                 end_date=end_date,
                                                 description=description,)

    def update_experience(self, sku, **kwargs):
        self.repository.update_experience(sku, **kwargs)

    def delete_experience(self, sku):
        self.repository.delete_experience(sku)


class CertificationService:
    def __init__(self):
        self.repository = CertificationRepository()

    def get_all_certifications(self):
        return self.repository.get_all_certifications()

    def get_certification_by_sku(self, sku):
        return self.repository.get_certification_by_sku(sku)

    def create_certification(self, user,name,issuing_organization,issue_date,expiration_date,description):
        return self.repository.create_certification(user,name=name,issuing_organization=issuing_organization,
                                                    issue_date=issue_date,
                                                    expiration_date=expiration_date,
                                                    description=description,)

    def update_certification(self, sku, **kwargs):
        self.repository.update_certification(sku, **kwargs)

    def delete_certification(self, sku):
        self.repository.delete_certification(sku)
