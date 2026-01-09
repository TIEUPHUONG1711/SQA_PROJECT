import logging
import os #để làm việc với đường dẫn hệ thống và thư mục

def get_logger():
    logger = logging.getLogger("SQA_LOGGER")# để cấu hình logger ghi log vào file và hiện thị trên terminal
    logger.setLevel(logging.INFO)
    
    if logger.handlers: #ktra xem logger đã có handler chưa, nếu có rồi thì trả về luôn
        return logger

    log_dir = os.path.join(os.path.dirname(__file__), "..", "logs") 
    #tạo thư mục logs nếu chưa tồn tại
    os.makedirs(log_dir, exist_ok=True) 

    log_file = os.path.join(log_dir, "sqa_run.log")

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    # File handler (ghi toàn bộ log)
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(formatter)

    # Console handler (hiện terminal)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(
        logging.Formatter("%(levelname)s - %(message)s")
    )

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# đoạn code trên để cấu hình logger ghi log vào file và hiện thị trên terminal
