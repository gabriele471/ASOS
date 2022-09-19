import time, datetime
import threading

def log_message(pid : str, message : str) -> None:
    time = str(datetime.datetime.now())
    print(f'[{time}] [THREAD {threading.current_thread().getName().upper()}] - [{pid}] - {message}')