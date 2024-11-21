from django.core.mail import EmailMultiAlternatives

def send_email(subject, to, text_content,html_content):
    """
    Send an email using Django's built-in EmailMultiAlternatives.
    """
    email = EmailMultiAlternatives(subject, text_content, to=to)
    email.attach_alternative(html_content, 'text/html')
    email.send()