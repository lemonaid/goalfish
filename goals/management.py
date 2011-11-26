from django.db.models import signals
from django.conf import settings
from django.utils.translation import ugettext_noop as _

if "Goalfish.notification" in settings.INSTALLED_APPS:
    from Goalfish.notification import models as notification

    def create_notice_types(app, created_models, verbosity, **kwargs):
        notification.create_notice_type("goal_ended", _("Goal Ended"), _("One of Your Goals has reached its Completion Date"))
        notification.create_notice_type("goal_verify_response", _("Goal Verified"), _("One of Your Goals has been VERIFIED!"))
        notification.create_notice_type("goal_verify_request", _("Goal Verification Request"), _("One of Your Students has asked that You Verify a Goal"))


    signals.post_syncdb.connect(create_notice_types, sender=notification)
    
else:
    
    print "Skipping creation of NoticeTypes as notification app not found"