import os

# Корневая директория проекта
ROOT_DIR = os.path.dirname(__file__)

# Директория для логов
LOGS_DIR = os.path.join(ROOT_DIR, "logs")

PATH = os.path.dirname(__file__)
DATA_PATH = os.path.join(PATH, "data")
LOGS_PATH = os.path.join(PATH, "logs")

UTILS_LOGS = os.path.join(LOGS_DIR, "utils.log")
SERVICES_LOGS = os.path.join(LOGS_DIR, "services.log")
REPORTS_LOGS = os.path.join(LOGS_DIR, "reports.log")
VIEWS_LOGS = os.path.join(LOGS_DIR, "views.log")