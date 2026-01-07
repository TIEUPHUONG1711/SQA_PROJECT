from SQA_PROJECT.logs.logger import get_logger
from SQA_PROJECT.utils.api_client import get_users
from SQA_PROJECT.config import BASE_URL, USERS_ENDPOINT, MAX_RESPONSE_TIME

logger = get_logger()

def test_get_users_api():
    logger.info("START TEST: GET /users API")

    url = BASE_URL + USERS_ENDPOINT
    response, response_time = get_users(url)

    if response.status_code == 200:
        logger.info("Status Code PASS")
    else:
        logger.error(f"Status Code FAIL: {response.status_code}")
        return

    if response_time <= MAX_RESPONSE_TIME:
        logger.info(f"Response Time PASS: {response_time:.2f}s")
    else:
        logger.warning(f"Response Time FAIL: {response_time:.2f}s")

    data = response.json()
    required_fields = ["id", "name", "email"]

    for i, user in enumerate(data):
        for field in required_fields:
            if field not in user:
                logger.error(f"Missing field {field} at record {i}")
                return

    logger.info("Mandatory Fields PASS")
    logger.info("END TEST: GET /users API")

if __name__ == "__main__":
    test_get_users_api()
