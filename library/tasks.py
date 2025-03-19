from celery import shared_task
from .models import Loan
from django.core.mail import send_mail
from django.conf import settings
from django.utils.timezone import now
@shared_task
def send_loan_notification(loan_id):
    try:
        loan = Loan.objects.get(id=loan_id)
        member_email = loan.member.user.email
        book_title = loan.book.title
        send_mail(
            subject='Book Loaned Successfully',
            message=f'Hello {loan.member.user.username},\n\nYou have successfully loaned "{book_title}".\nPlease return it by the due date.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[member_email],
            fail_silently=False,
        )
    except Loan.DoesNotExist:
        pass

@shared_task
def check_overdue_loans():
    overdue_loans = Loan.objects.filter(is_returned = False, due_date__lt = now().date())

    for loan in overdue_loans:
        user_email = loan.member.user.email
        book_title = loan.book.title

        send_mail(
            subject="Overdue Book Loan Reminder",
            message=f""" Dear {loan.member.user.username},\n\n You Have an overdue book: {book_title}. Please Return it as soon as possible.\n\n Thanks""",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user_email],
            fail_silently=False,
        )

    return f"{len(overdue_loans)} overdue notifications sent."