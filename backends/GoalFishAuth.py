from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import ImproperlyConfigured
from django.db.models import get_model


class MultiModelBackend(ModelBackend):
    def authenticate(self, username=None, password=None):
        try:
            user = self.student_class.objects.get(username=username)
            if user.check_password(password):
                return user
        except:
            try:
                user = self.teacher_class.objects.get(username=username)
                if user.check_password(password):
                    return user
            except:
                try:
                    user = self.parent_class.objects.get(username=username)
                    if user.check_password(password):
                        return user
                except:
                    try:
                        user = self.mentor_class.objects.get(username=username)
                        if user.check_password(password):
                            return user
                    except:
                        try:                                            
                            user = self.sponsor_class.objects.get(username=username)
                            if user.check_password(password):
                                return user
                        except:
                            try:
                                user = User.objects.get(username=username)
                                if user.check_password(password):
                                    return user
                            except User.DoesNotExist:
                                return None

    def get_user(self, user_id):
        try:
            return self.student_class.objects.get(pk=user_id)
        except:
            try: 
                return self.teacher_class.objects.get(pk=user_id)
            except:
                try:
                    return self.parent_class.objects.get(pk=user_id)
                except:
                    try:
                        return self.mentor_class.objects.get(pk=user_id)
                    except:
                        try:
                            return self.sponsor_class.objects.get(pk=user_id)
                        except:
                            try:
                                return User.objects.get(pk=user_id)
                            except User.DoesNotExist:
                                return None
    @property
    def student_class(self):
        if not hasattr(self, '_student_class'):
            self._student_class = get_model(*settings.STUDENT_USER_MODEL.split('.', 2))
            if not self._student_class:
                raise ImproperlyConfigured('Could not get custom student user model')
            return self._student_class
    
    @property
    def teacher_class(self):
        if not hasattr(self, '_teacher_class'):
            self._teacher_class = get_model(*settings.TEACHER_USER_MODEL.split('.', 2))
            if not self._teacher_class:
                raise ImproperlyConfigured('Could not get custom teacher user model')
            return self._teacher_class
            
    @property
    def parent_class(self):
        if not hasattr(self, '_parent_class'):
            self._parent_class = get_model(*settings.PARENT_USER_MODEL.split('.', 2))
            if not self._parent_class:
                raise ImproperlyConfigured('Could not get custom parent user model')
            return self._parent_class
        
    @property
    def mentor_class(self):
        if not hasattr(self, '_mentor_class'):
            self._mentor_class = get_model(*settings.MENTOR_USER_MODEL.split('.', 2))
            if not self._mentor_class:
                raise ImproperlyConfigured('Could not get custom mentor user model')
            return self._mentor_class
    
    @property
    def sponsor_class(self):
        if not hasattr(self, '_sponsor_class'):
            self._sponsor_class = get_model(*settings.SPONSOR_USER_MODEL.split('.', 2))
            if not self._sponsor_class:
                raise ImproperlyConfigured('Could not get custom sponsor user model')
            return self._sponsor_class
    
        