from rest_framework_simplejwt import tokens


class GetUserTokens:
    def __init__(self, user) -> None:
        self.user = user

    def get_user_auth_tokens(self):
        refresh = tokens.RefreshToken.for_user(user=self.user)

        dict_tokens = {
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }
        return dict_tokens
