from rest_framework.exceptions import APIException, _get_error_details


class CustomException(APIException):
    status_code = None
    default_code = None
    default_detail = None
    attr = None

    def __init__(self, status=None, detail=None, code=None, attr=None):
        if status is None:
            status = self.status_code
        if code is None:
            code = self.default_code
        if detail is None:
            detail = self.default_detail
        if attr is None:
            attr = self.attr

        self.detail = _get_error_details(detail, code)
        self.status_code = status
        self.attr = attr

        super().__init__(detail, code)


class InternalServerError(CustomException):
    status_code = 500
    default_code = "internal_server_error"
    default_detail = "Внутреняя ошибка сервера"


class ParseError(CustomException):
    status_code = 400
    default_code = "JSON parse error"
    default_detail = "Проверьте правильность введенных данных"


class UniqueError(CustomException):
    status_code = 400
    default_code = "unique"
    default_detail = "Такая запись уже существует"


class TokenNotValid(CustomException):
    status_code = 401
    default_code = "token_not_valid"
    default_detail = "Вы нe авторизованы"


class NoActiveAccount(CustomException):
    status_code = 401
    default_code = "no_active_account"
    default_detail = "Не найдена активная учетная запись с указанными учетными данными"
