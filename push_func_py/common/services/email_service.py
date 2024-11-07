from ..logger import Logger
from ..models.notification_message import NotificationMessage


class EmailService:

    def __init__(self, logger: Logger) -> None:
        self.logger = logger

    def send(self, message: NotificationMessage) -> None:
        self.logger.info(f"Sending email to {message.email_address}: {message.message}")
