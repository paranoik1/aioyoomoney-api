from datetime import datetime

from .exceptions import TechnicalError
from .globals import ERROR_CODES


def raise_error(error_code: str) -> None:
    if error_code in ERROR_CODES:
        raise ERROR_CODES[error_code]()
    else:
        raise TechnicalError(error_code)


def convert_datetime_to_str(date: datetime) -> str | None:
    if date is not None:
        return "{Y}-{m}-{d}T{H}:{M}:{S}".format(
            Y=str(date.year),
            m=str(date.month),
            d=str(date.day),
            H=str(date.hour),
            M=str(date.minute),
            S=str(date.second)
        )

    return None
