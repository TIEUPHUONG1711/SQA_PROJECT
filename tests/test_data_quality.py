import pandas as pd
from SQA_PROJECT.logs.logger import get_logger
from SQA_PROJECT.utils.validator import (
    check_null,
    check_duplicate,
    check_email_format
)

logger = get_logger()
DATA_PATH = r"D:\SQA_PROJECT\SQA_PROJECT\data\users.csv"

def test_data_quality():
    logger.info("START TEST: DATA QUALITY")

    df = pd.read_csv(DATA_PATH)

    result, msg = check_null(df, ["id", "name", "email"])
    logger.info("NULL CHECK PASS" if result else f"NULL CHECK FAIL: {msg}")

    result, msg = check_duplicate(df, "id")
    logger.info("DUPLICATE CHECK PASS" if result else f"DUPLICATE CHECK FAIL: {msg}")

    result, msg = check_email_format(df, "email")
    logger.info("EMAIL FORMAT PASS" if result else f"EMAIL FORMAT FAIL: {msg}")

    logger.info(f"ROW COUNT PASS: {len(df)} records" if len(df) > 0 else "ROW COUNT FAIL")

    logger.info("END TEST: DATA QUALITY")

if __name__ == "__main__":
    test_data_quality()
