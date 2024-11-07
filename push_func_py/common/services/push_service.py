from ..logger import Logger
from ..models.notification_message import NotificationMessage


class PushService:

    def __init__(self, logger: Logger) -> None:
        self.logger = logger

    def send(self, message: NotificationMessage) -> None:
        self.logger.info(
            f"Sending push notification to {message.system_id}: {message.message}"
        )
