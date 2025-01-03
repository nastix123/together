import traceback
from typing import Any

from drf_standardized_errors.formatter import ExceptionFormatter

from core.utils.exceptions import (
    InternalServerError,
    NoActiveAccount,
    ParseError,
    TokenNotValid,
    UniqueError,
)

exception_dict = {
    "error": InternalServerError,
    "parse_error": ParseError,
    "unique": UniqueError,
    "token_not_valid": TokenNotValid,
    "no_active_account": NoActiveAccount,
}


class MyExceptionFormatter(ExceptionFormatter):
    def format_error_response(self, exc: type[Any]) -> dict[str, Any]:
        print(traceback.format_exc())
        if exc.errors[0].attr:
            attr = exc.errors[0].attr
        else:
            attr = self.original_exc.__dict__.get("attr")
        if exc.errors[0].code in exception_dict:
            return {
                "type": exc.type,
                "errors": [
                    {
                        "code": exception_dict[exc.errors[0].code].default_code,
                        "detail": exception_dict[exc.errors[0].code].default_detail,
                        "attr": attr,
                    }
                    # for error in exc.errors
                ],
            }
        else:
            return {
                "type": exc.type,
                "errors": [
                    {"code": error.code, "detail": error.detail, "attr": error.attr}
                    for error in exc.errors
                ],
            }
