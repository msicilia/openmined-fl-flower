from pathlib import Path
from syft_rds.orchestra import remove_rds_stack_dir

remove_rds_stack_dir(root_dir=Path("."), key="local_syftbox_network")
