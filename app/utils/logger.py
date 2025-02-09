import logging
from pathlib import Path
from typing import Optional

class AppLogger:
    _logger = None

    @classmethod
    def get_logger(cls, log_file: Optional[str] = '/data/app.log') -> logging.Logger:
        if cls._logger is None:
            cls._logger = logging.getLogger('DataWorksAgent')
            cls._logger.setLevel(logging.DEBUG)

            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )

            # Console handler
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)
            console_handler.setFormatter(formatter)
            cls._logger.addHandler(console_handler)

            # File handler
            if log_file:
                Path(log_file).parent.mkdir(parents=True, exist_ok=True)
                file_handler = logging.FileHandler(log_file)
                file_handler.setLevel(logging.DEBUG)
                file_handler.setFormatter(formatter)
                cls._logger.addHandler(file_handler)

        return cls._logger
