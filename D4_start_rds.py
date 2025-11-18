import os
import syft_rds as sy
from pathlib import Path
import time

from syft_core import Client

C = Client.load().email
print(f"email: {C}")

try:
    print(f"[RDS] Starting RDS server...")
    client = sy.init_session(host=C, start_rds_server=True)
    print("[RDS] Server ready. Press Ctrl+C to stop.")
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    print("\n[RDS] Stopping. Bye!")
except Exception as e:
    print(f"[RDS] Error: {e}")