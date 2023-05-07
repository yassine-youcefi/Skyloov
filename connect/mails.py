
import os
from datetime import date
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings




class MailUtil:

    def __init__(self, user, to_email, *args):
        self.jinja_dict = {}
        self.args = args
        self.sender = " Skyloov " + "<" + settings.EMAIL_HOST_USER + ">" 
        self.to_email = to_email
        self.user = user


    def send_email_welcome(self):
                
            '''
                user signup and welcome email.
            '''
            
            self.jinja_dict["username"] = self.user.username

            html_content = render_to_string(
                "mails/signup_email.html", self.jinja_dict)

            text_content = strip_tags(html_content)
            email = EmailMultiAlternatives(
                # subject
                "welcome to Skyloov.",
                # content
                text_content,
                # from email
                self.sender,
                # recipient mail
                [self.to_email],
            )

            email.attach_alternative(html_content, "text/html")
            email.send()