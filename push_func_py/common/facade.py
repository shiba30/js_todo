from .models.notification_message import NotificationMessage
from .services.email_service import EmailService
from .services.push_service import PushService
from .services.sms_service import SMSService


class NotificationFacade:
    def __init__(
        self,
        email_service: EmailService,
        sms_service: SMSService,
        push_service: PushService,
    ) -> None:
        self.email_service = email_service
        self.sms_service = sms_service
        self.push_service = push_service

    def send_notification(self, message: NotificationMessage) -> None:
        """
        通知を送信する

        Args:
            message (NotificationMessage): 通知メッセージ
        """
        if message.pushType == "M":
            self.email_service.send(message)
        elif message.pushType == "S":
            self.sms_service.send(message)
        elif message.pushType == "P":
            self.push_service.send(message)
        else:
            raise Exception(f"Unknown notification type: {message.pushType}")
