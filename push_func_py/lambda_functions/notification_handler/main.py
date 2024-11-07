""" ローカル環境でLambda関数を実行するためのスクリプト """

from typing import Any, Dict

from handler import LambdaHandler

from common.facade import NotificationFacade
from common.logger import Logger
from common.services.email_service import EmailService
from common.services.push_service import PushService
from common.services.sms_service import SMSService

if __name__ == "__main__":
    logger = Logger(log_level="DEBUG")
    facade = NotificationFacade(
        EmailService(logger), SMSService(logger), PushService(logger)
    )
    handler = LambdaHandler(facade, logger)

    # テスト用のSQSメッセージ
    test_message: Dict[str, Any] = {
        "pushType": "P",  # 必須フィールド
        "system_id": "1234567890",  # 必須フィールド
        "message": "This is a test push.",  # 既存のフィールド
    }
    handler.handle(test_message)
