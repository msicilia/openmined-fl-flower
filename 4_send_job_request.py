import argparse

parser = argparse.ArgumentParser(description="Send job request to a node")
parser.add_argument("node_id", type=int, help="ID of the node (mandatory integer)")
args = parser.parse_args()


DO_EMAIL = f"{args.node_id}@openmined.org"

do_guest = ds_stack.init_session(host=DO_EMAIL)

SYFTBOX_DATASET_NAME = "dataset"

os.environ["SYFTBOX_CLIENT_CONFIG_PATH"] = str(ds_stack.client.config_path)
# os.environ["SYFT_FLWR_MSG_TIMEOUT"] = "60"
SYFT_FLWR_PROJECT_PATH = Path("./simple-classifier")
assert SYFT_FLWR_PROJECT_PATH.exists()