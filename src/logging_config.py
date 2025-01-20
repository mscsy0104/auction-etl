import logging
from logging.handlers import RotatingFileHandler


def setup_logging(log_file="etl-program.log"):
    """
    Set up logging configuration for the application.
    Args:
        log_file (str): Path to the log file.
    """
    # 로그 포맷 정의
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # 파일 핸들러 생성 (자동 회전 기능 포함)
    file_handler = RotatingFileHandler(
        log_file, maxBytes=5 * 1024 * 1024, backupCount=3  # 5MB, 백업 3개
    )
    file_handler.setFormatter(formatter)

    # 콘솔 핸들러 생성 (CLI에 출력용)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # 루트 로거 설정
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)

    logging.info("Logging is set up.")  # 초기화 확인 메시지