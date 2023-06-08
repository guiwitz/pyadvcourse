from pyadvcourse import algos
import numpy as np
import pandas as pd
import pytest

def test_add_one():
    
    a = 1
    out = algos.add_one(a)
    assert out == 2

def test_add_one_to_df():
        
    a = np.array([1,2,3])
    out = algos.add_one_to_df(a)
    assert isinstance(out, pd.DataFrame)


@pytest.mark.parametrize("test_input, expected", 
                         [([[1.2, 2.1],1], 1), ([[1.9, 3.1],1], 2)])
def test_sum_thresholding_fun(test_input, expected):

    input = np.array(test_input[0]) 
    out = algos.sum_thresholding_fun(input, test_input[1])
    assert out == expected