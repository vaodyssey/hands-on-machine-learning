from numpy import *
def test_set_check(identifier, test_ratio, hash): 
    return hash(int64(identifier)).digest()[-1] < 256 * test_ratio