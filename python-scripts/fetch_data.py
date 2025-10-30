import os
import sys
import tarfile
from six.moves import urllib

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

def fetch_housing_data(housing_url=HOUSING_URL, housing_path="datasets/housing"):
    """Download and extract the housing dataset into the given directory."""
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)

    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    
    with tarfile.open(tgz_path) as housing_tgz:
        housing_tgz.extractall(path=housing_path)


if __name__ == "__main__":
    # Default directory if no argument is provided
    housing_dir = sys.argv[1] if len(sys.argv) > 1 else os.path.join("datasets", "housing")
    
    print(f"Downloading dataset into: {housing_dir}")
    fetch_housing_data(housing_path=housing_dir)
    print("Done!")
