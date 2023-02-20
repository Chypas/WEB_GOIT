import logging
from logger import get_logger

logger = get_logger(__name__)


def main():
    logger.info('Тут пишемо що, хочемо логгувати в файлі')
    logger.debug("Тут пишемо, що хочемо логгувати в терміналі")
    try:
        pass
    except Exception as err:
        logger.error(f'[ERROR] {err}') # тут логгуємо помилки, будуть записані в файл



if __name__ == "__main__":
    logger.log(level=logging.DEBUG, msg=f"Start")
    main()
