import time

def delay_action(seconds: int, action: str = "next action"):
    print(f"Waiting for {seconds} seconds before {action}...")
    time.sleep(seconds)
