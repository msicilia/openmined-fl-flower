from pathlib import Path
import argparse
import syft_rds as sy
from syft_core import Client


do_email = Client.load().email
print(f"DO email: {do_email}")
do = sy.init_session(host=do_email, start_rds_server=True)

jobs = do.job.get_all(status="pending_code_review")

for job in jobs:
    print(f"Approving job {job.id} submitted by {job.user_email}")
    print(f"Job details: {job.show_user_code()}")
    approve = input("Approve this job? (y/n): ")
    if approve.lower() == "y":
        do.run_private(job)
    break