from django.core.mail import send_mail 



def send_confirmation_email(user):
    code = user.activation_code
    full_link = f'http://localhost:8000/api/v1/account/activate/{code}/'
    to_email = user.email
    send_mail(
        'Здавствуйте активируйте ваш аккаунт!',
        f'Чтобы активировать ваш аккаунт нужно перейти по ссылке: {full_link}',
        'from@example.com',
        [to_email,],
        fail_silently=False,
    )


def send_reset_password(user):
    code = user.activation_code
    to_email = user.email
    send_mail(
        'Восстановление пароля',
        f'Ваш код: {code}',
        'from@example.com',
        [to_email],
        fail_silently=False,
    )


def send_notification(user, id):
    to_email = user.email
    send_mail(
        'Уведомление о создании заказов!!',
        f'Вы создали заказ №{id}, ожидайте звонка от курьера! Спасибо за доверие',
        'market.place@gmail.com',
        [to_email],
        fail_silently=False,

    )