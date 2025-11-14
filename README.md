
## Generation of synthetic datasets and overall setup

...

## Local execution
...

## Distributed execution

### Setup local Syftbox data site

Installs and optionally starts the client. 
```
curl -fsSL https://syftbox.net/install.sh | sh
```
The client can be started at any time using the command `syftbox`.

The datasite shall be visible at the Datasites Web page, e.g.:
```
https://syftbox.net/datasites/msicilia@gmail.com/
```

### Launch your instance 

```
syftbox
```

### Setup the dataset for the demonstration
The data needs to be available in the `DATASET_PATH` folder for the given partition chosen.

For example, this run:
```
uv run D1_prepare_datasite_distributed.py 1
```

Would create a record for partition 1 of the dataset, which has to be available locally to the script, with the layout created by `0_create_datasets.py`.

### Submit the code to the datasites

The script `D2_submit_code_fl_job.py` shall be run for each of the datasites that are to be participating in the federated learning cycle. It takes the DID of the datasite as param.


### Approve the requests

The `D3_approve_jobs.py` script takes the first job submitted and asks the datasite admin for approval. If approve, it participates in the federated learning cycle.

### Run the simulation

From the data scientist (coordinator) machine:
```
 uv run simple-classifier/main.py --active
```