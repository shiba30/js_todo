""" AWS Lambda functionのエントリーポイント """

import json
import os
import sys
from typing import Any, Dict

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)

from common.facade import NotificationFacade
from common.logger import Logger
from common.notification_validator import NotificationValidator
from common.services.email_service import EmailService
from common.services.push_service import PushService
from common.services.sms_service import SMSService


def lambda_handler(event: Dict[str, Any], context: Any) -> None:
    """
    AWS Lambdaのエントリーポイント

    Args:
        event (Dict[str, Any]): イベントデータ
        context (Any): コンテキストデータ
    """
    # ロガーの初期化
    logger = Logger(log_level=os.getenv("LOG_LEVEL", "INFO"))

    # 通知ファサードの初期化
    facade = NotificationFacade(
        EmailService(logger), SMSService(logger), PushService(logger)
    )

    # Lambdaハンドラーの初期化
    handler = LambdaHandler(facade, logger)

    for record in event["Records"]:
        # SQSメッセージを処理する
        handler.handle(json.loads(record["body"]))


class LambdaHandler:

    def __init__(
        self,
        facade: NotificationFacade,
        logger: Logger,
    ) -> None:
        self.facade = facade
        self.logger = logger

    def handle(self, sqs_message: Dict[str, Any]) -> None:
        """
        SQSメッセージを処理する

        Args:
            sqs_message (Dict[str, Any]): SQSメッセージ
        """
        try:
            self.logger.info(f"start push: {sqs_message}")
            message = NotificationValidator.validate(sqs_message)
            self.facade.send_notification(message)
        except Exception as e:
            self.logger.error(f"An error occurred: {e}")
            raise e
        finally:
            self.logger.info("end push")
