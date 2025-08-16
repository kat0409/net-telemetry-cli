import random, time

def expo_backoff(attempt: int, base: float = 0.5, jitter: float = 0.3) -> float:
    return base * (2 ** attempt) + random.uniform(0, jitter)

def sleep_backoff(attempt: int, base: float = 0.5, jitter: float = 0.3):
    time.sleep(expo_backoff(attempt, base, jitter))
