# services/user_service.py
from django.utils import timezone
from .user_repository import OTPRepository

import pyotp

from .models import User
from .utils import sendToken
from .user_repository import UserRepository, ProfileRepository


class UserService:
    """
    
    """
    @staticmethod
    def register_user(email, username, phone, password, first_name, last_name):
        user = UserRepository.create_user(
        email=email,
        username=username,
        phone=phone,
        password=password,
        first_name=first_name,
        last_name=last_name
        )
        return user

    @staticmethod
    def get_user_by_email(email):
        return UserRepository.get_user_by_email(email)


class ProfileService:
    """
    
    """
    @staticmethod
    def get_profile(user):
        return ProfileRepository.get_profile_by_user(user)
    
    @staticmethod
    def update_profile(user, **kwargs):
        profile = ProfileRepository.get_profile_by_user(user)
        if profile:
            return ProfileRepository.update_profile(profile, **kwargs)
        return None
    
    @staticmethod
    def delete_profile(user):
        profile = ProfileRepository.get_profile_by_user(user)
        if profile:
            ProfileRepository.delete_profile(profile)
            return True
        return False


class OTPService:
    """
    
    """
    @staticmethod
    def request_otp(email):
        try:
            user = User.objects.get(email=email)
            result = sendToken(user)
            return result
        except User.DoesNotExist:
            return {'error': 'User not found', 'otp': False}
    
    @staticmethod
    def verify_otp(email, otp):
        try:
            user = User.objects.get(email=email)
            otp_record = OTPRepository.get_otp_by_user(user)
            if otp_record and otp_record.token == otp and (timezone.now() - otp_record.created_at).seconds < 60:
                return True
            return False
        except User.DoesNotExist:
            return False

    @staticmethod
    def reset_password(email, otp, new_password):
        if OTPService.verify_otp(email, otp):
            user = User.objects.get(email=email)
            user.set_password(new_password)
            user.save()
            OTPRepository.delete_otp_by_user(user)
            return True
        return False
