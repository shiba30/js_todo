from ..logger import Logger
from ..models.notification_message import NotificationMessage


class SMSService:

    def __init__(self, logger: Logger) -> None:
        self.logger = logger

    def send(self, message: NotificationMessage) -> None:
        self.logger.info(f"Sending SMS to {message.phone_number}: {message.message}")
