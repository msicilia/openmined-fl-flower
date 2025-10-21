
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

### Setup the dataset for the demonstration
The data needs to be available in the `DATASET_PATH` folder for the given partition chosen.

For example, this run:
```
uv run D1_prepare_datasite_distributed.py 1
```

Would create a record for partition 1 of the dataset, which has to be available locally to the script, with the layout created by 0_create_datasets.py``.
