from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
import numpy as np
import os
import shutil

DATA_FOLDER = "data/"
N_NODES = 10
N_SAMPLES = 20_000

# Remove all subfolders and files under DATA_FOLDER
if os.path.exists(DATA_FOLDER):
    for item in os.listdir(DATA_FOLDER):
        item_path = os.path.join(DATA_FOLDER, item)
        if os.path.isdir(item_path):
            shutil.rmtree(item_path)
        else:
            os.remove(item_path)

X, y = make_classification(n_samples=N_SAMPLES)
n_features = X.shape[1]
header = [f"feat_{i}" for i in range(n_features)] + ["label"]

for i in range(N_NODES):
    start = i * (N_SAMPLES // N_NODES)
    end = (i + 1) * (N_SAMPLES // N_NODES)
    X_part = X[start:end]
    y_part = y[start:end].astype(int)  # Ensure labels are integers
    X_part_train, X_part_test, y_part_train, y_part_test = train_test_split(
        X_part, y_part, test_size=0.2
    )

    node_folder = os.path.join(DATA_FOLDER, f"node_{i}", "private")
    mock_folder = os.path.join(DATA_FOLDER, f"node_{i}", "mock")
    os.makedirs(node_folder, exist_ok=True)
    os.makedirs(mock_folder, exist_ok=True)

    train_data = np.column_stack((X_part_train, y_part_train.astype(int)))
    test_data = np.column_stack((X_part_test, y_part_test.astype(int)))

    # Save train and test CSVs with headers
    np.savetxt(
        os.path.join(node_folder, "train.csv"),
        train_data,
        delimiter=",",
        header=",".join(header),
        comments="",
        fmt=["%.8f"] * n_features + ["%d"]
    )
    np.savetxt(
        os.path.join(node_folder, "test.csv"),
        test_data,
        delimiter=",",
        header=",".join(header),
        comments="",
        fmt=["%.8f"] * n_features + ["%d"]
    )

    # Save 3 sample rows from train and test to mock folder with headers
    train_sample = train_data[:3]
    test_sample = test_data[:3]
    np.savetxt(
        os.path.join(mock_folder, "train.csv"),
        train_sample,
        delimiter=",",
        header=",".join(header),
        comments="",
        fmt=["%.8f"] * n_features + ["%d"]
    )
    np.savetxt(
        os.path.join(mock_folder, "test.csv"),
        test_sample,
        delimiter=",",
        header=",".join(header),
        comments="",
        fmt=["%.8f"] * n_features + ["%d"]
    )

    # Save README.md in each node folder
    readme_path = os.path.join(DATA_FOLDER, f"node_{i}", "README.md")
    with open(readme_path, "w") as f:
        f.write(f"This is the dataset from node {i}\n")


