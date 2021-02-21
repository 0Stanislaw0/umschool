from django.contrib.auth.forms import AuthenticationForm


class UserAuthForm(AuthenticationForm):
    """
    Форма авторизации в системе
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {
                "id": "login",
                "type": "text",
                "name": "login",
                "placeholder": "Введите логин",
            }
        )
        self.fields["password"].widget.attrs.update(
            {
                "id": "password",
                "type": "text",
                "name": "login",
                "placeholder": "Введите пароль",
            }
        )
