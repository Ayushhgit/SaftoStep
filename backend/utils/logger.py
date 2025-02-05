import logging
import os

# Define log directory and file path
LOG_DIR = "logs"
LOG_FILE = "app.log"
LOG_PATH = os.path.join(os.getcwd(), LOG_DIR)

# Ensure the logs directory exists
os.makedirs(LOG_PATH, exist_ok=True)

# Full log file path
LOG_FILE_PATH = os.path.join(LOG_PATH, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    filemode="a",  # Append mode to keep adding logs
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Test log
if __name__ == "__main__":
    logging.info("Logging has started")
    logging.warning("This is a warning")