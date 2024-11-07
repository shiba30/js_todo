from typing import List, Optional

from pydantic import BaseModel, Field, ValidationError

from .value_objects import EmailAddress, PhoneNumber


class NotificationMessage(BaseModel):
    # 必須項目
    pushType: str = Field(min_length=1, max_length=1)  # 通知種別
    system_id: str = Field(min_length=1, max_length=10)  # システムID
    message: str = Field(min_length=1, max_length=1024 * 10)  # 通知メッセージ(最大10KB)

    # 任意項目
    email_address: Optional[List[EmailAddress]] = None  # 送信先 メールアドレス(複数)
    phone_number: Optional[List[PhoneNumber]] = None  # 送信先 電話番号(複数)

    class Config:
        extra = "forbid"  # 許可されていないキーが渡された場合にエラーを発生させる


def get_test_data():
    """テストデータを取得"""
    success_data = {
        "pushType": "P",
        "message": "This is a test message.",
        "system_id": {"value": "1234567890"},
        "email_address": [{"value": "test@test.com"}, {"value": "test2@test.com"}],
        "phone_number": [{"value": "09012345678"}, {"value": "08012345678"}],
    }

    error_data = {
        "pushType": "",
        "system_id": {"value": "1234567890"},
        "email_address": [{"value": "test@test.com"}, {"value": "test2@test.com"}],
        "phone_number": [{"value": "09012345678"}, {"value": "08012345678"}],
    }

    error_data_2 = {
        "pushType": "P",
        "message": "This is a test message.",
        "system_id": {"value": "123456789"},
    }

    error_data_3 = {
        "pushType": "P",
        "message": "This is a test message.",
        "system_id": {"value": "1234567890"},
        "email_address": [{"value": "test.com"}],
    }

    error_data_4 = {
        "pushType": "P",
        "message": "This is a test message.",
        "system_id": {"value": "1234567890"},
        "phone_number": [{"value": "1234567890"}, {"value": "090123456789"}],
    }

    return [success_data, error_data, error_data_2, error_data_3, error_data_4]


if __name__ == "__main__":
    # 動作確認用のコード
    data_list = get_test_data()
    count = 0
    for data in data_list:
        print("-------------------------")
        try:
            NotificationMessage(**data)
            print(f"データ{count}: 成功")
        except ValidationError as e:
            print(f"エラー内容{count}: {e.errors()}")
        count += 1
        print("-------------------------")
