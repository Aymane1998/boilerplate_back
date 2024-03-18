class ResetUserPasswordService:
    def __init__(self, token, password) -> None:
        self.token = token
        self.password = password

    def handler(self):
        if self.token.has_expired:
            raise ValueError("The token has expired.")

        user = self.token.user

        user.set_password(self.password)
        user.save()

        self.token.delete()
