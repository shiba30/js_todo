import logging


class Logger:
    def __init__(self, log_level: str = "INFO"):
        self.logger = logging.getLogger()
        self.set_log_level(log_level)
        self.set_log_format()

    def set_log_level(self, log_level: str) -> None:
        level = logging.getLevelName(log_level.upper())
        self.logger.setLevel(level)

    def set_log_format(self) -> None:
        """
        ログのフォーマットを設定する
        """
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def info(self, message: str) -> None:
        self.logger.info(message)

    def error(self, message: str) -> None:
        self.logger.error(message)

    def debug(self, message: str) -> None:
        self.logger.debug(message)

    def warning(self, message: str) -> None:
        self.logger.warning(message)
