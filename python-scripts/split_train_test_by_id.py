import hashlib
import numpy as np
from test_set_check import test_set_check
def split_train_test_by_id(data, test_ratio, id_column, hash=hashlib.md5):    
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: test_set_check(id_, test_ratio, hash))
    return data.loc[~in_test_set], data.loc[in_test_set]