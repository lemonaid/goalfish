from Goalfish.groups.models import Classes
from Goalfish.fishes.models import Teacher
from django.core.mail import EmailMultiAlternatives

class AutomatedTasks:
    
    def send_welcome_email(self, username):
        #sends out a welcome email to teachers who aren't registered but students identify
        u = Teacher.objects.get(username=username)
        
        
        subject, from_email, to = "Welcome to Goalfish", "teachers@goalfish.es", 
        
    
    def auto_register_teacher(self, class_id):
        #will create a teacher account for classes created with a non-registered teacher
        
        c = Classes.objects.get(pk=class_id)
        if c.has_unregistered_teacher():
            
            _username = c.unregistered_teacher.replace(" ","_")
            if c.unregistered_teacher_email:
                _email = c.unregistered_teacher_email
            else:
                _email = '%s@goalfish.es' % _username
            
            try:
                u = Teacher.objects.create_user(username=_username, email=_email)
                u.save()
                
            except:
                
                return False