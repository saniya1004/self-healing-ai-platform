import time
from datetime import datetime

def log_event(event_type: str, data: dict):
    log = {
        "type": event_type,
        "data": data,
        "timestamp": str(datetime.now())
    }

    print("[LOG]:", log)