import time
import threading
from config import printers  # Load printer configuration
from dashboard_utils import get_printer_data, cache_printer_data  # Utility functions

def poll_printers():
    while True:
        for printer in printers:
            data = get_printer_data(printer)
            cache_printer_data(printer['name'], data)
            time.sleep(10)
        time.sleep(10000)  # Adjust polling interval as needed

if __name__ == "__main__":
    poll_thread = threading.Thread(target=poll_printers)
    poll_thread.daemon = True
    poll_thread.start()