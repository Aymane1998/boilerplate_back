from rest_framework.exceptions import APIException


class APIValidationError(APIException):
    status_code = 400
    detail = ""

    def __init__(self, detail=None, status=None, errors=None):
        if detail is not None:
            self.detail = detail
        if status is not None:
            self.status_code = status

        # If errors is not None, include it in detail
        if errors is not None:
            self.detail = {"detail": self.detail, "errors": errors}
        super().__init__(self.detail, self.status_code)
