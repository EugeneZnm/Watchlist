from flask_mail import Message
from flask import render_template
from . import mail


def mail_message(subject, template,to,**kwargs):
    """
    mail message function
    :param subject:
    :param template: (passed without extension because both a text and html version should be created)
    :param to: (recipient)
    :param kwargs: (keyword argument)
    :return:
    """
    sender_email='x41808715@gmail.com'

    email = Message(subject, sender=sender_email, recipients=[to])
    """
    message instance with subject, sender_email and recipient passed in
    """
    email.body = render_template(template + ".txt", **kwargs)
    """
    setup email body
    """
    email.html = render_template(template + ".html", ** kwargs)
    mail.send(email)
    """
    send method with email instance passed in to send email
    """