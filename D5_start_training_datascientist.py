import syft_rds as sy
from syft_core import Client
from pathlib import Path

DS = Client.load().email
print(f"DS's email: {DS}")

USE_RDS_DASHBOARD = False
ds = sy.init_session(host=DS, email=DS, 
        start_syft_event_server=not USE_RDS_DASHBOARD)


SYFT_FLWR_PROJECT_PATH = Path("./simple-classifier")
SYFTBOX_DATASET_NAME = "synthetic-dataset"

ds.job.delete_all()

job = ds.job.submit(
    name="simple_classifier",
    user_code_path=SYFT_FLWR_PROJECT_PATH,
    dataset_name=SYFTBOX_DATASET_NAME,
    entrypoint="main.py",
)
import time
time.sleep(10)  # wait for job to appear in ds.job.get_all()
#print(f"Approving job: {job}")
ds.job.approve(job)
#print(f"Submitted job: {job}")
ds.run_private(ds.job.get_all()[0], blocking=True)

#print(ds.job.show_logs(job))

