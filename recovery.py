
import logging
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RECOVERY_SCRIPT = BASE_DIR / "service_restart.sh"


def recover_service():
    logging.info("Recovery process initiated.")
    print("Recovery process started...")

    try:
        result = subprocess.run(
            ["bash", str(RECOVERY_SCRIPT)],
            capture_output=True,
            text=True,
            timeout=60,
            check=True,
        )

        if result.stdout:
            print(result.stdout, end="")
            logging.info(result.stdout.strip())

        if result.stderr:
            logging.warning(result.stderr.strip())

        logging.info("Recovery script completed successfully.")
        print("Recovery script completed successfully.")
        return True

    except subprocess.CalledProcessError as error:
        message = (
            f"Recovery script failed with exit code "
            f"{error.returncode}."
        )
        logging.error(message)

        if error.stdout:
            print(error.stdout, end="")
        if error.stderr:
            print(error.stderr, end="")

        print(message)
        return False

    except subprocess.TimeoutExpired:
        logging.error("Recovery script timed out.")
        print("Recovery failed: script timed out.")
        return False

    except Exception:
        logging.exception("Unexpected recovery error.")
        print("Recovery failed. Check the log for details.")
        return False
