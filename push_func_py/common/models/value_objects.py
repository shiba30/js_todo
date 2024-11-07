from pydantic import BaseModel, EmailStr, StringConstraints
from typing_extensions import Annotated


# メールアドレス
class EmailAddress(BaseModel):
    value: EmailStr

    def __str__(self):
        return self.value


# 電話番号（日本形式）
class PhoneNumber(BaseModel):
    value: Annotated[str, StringConstraints(pattern=r"^0\d{9,10}$")]

    def __str__(self):
        return self.value
