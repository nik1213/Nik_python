import time

def retry(max_attempts=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    time.sleep(1)
            raise Exception("Max retry attempts exceeded")
        return wrapper
    return decorator