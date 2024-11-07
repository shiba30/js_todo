from typing import Any, Dict

from pydantic import ValidationError

from .models.notification_message import NotificationMessage


class NotificationValidator:
    @staticmethod  # 静的メソッド、インスタンス化しなくても呼び出せる
    def validate(sqs_message: Dict[str, Any]) -> NotificationMessage:
        try:
            return NotificationMessage(**sqs_message)
        except ValidationError as e:
            raise Exception(f"Validation error: {e.errors()}") from e
