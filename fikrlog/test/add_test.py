# import pytest
# from add import add

# @pytest.mark.parametrize("a, b, expected", table = [
#         (1, 2, 3),
#         (1, 1, 2),
#         (2, 4, 6),
#     ])
# def test_add(a, b, expected):
    
#     got = add(a, b)
    
#     assert got == expected, f"{expected=}, {got=}"
    


import pytest
from add import add

@pytest.mark.parametrize("a, b, expected", [
		(1, 1, 2),
		(2, 3, 5),
		(2, 2, 4),
])
def test_add(a, b, expected):
		got = add(a, b) 
		assert got == expected, f"{expected=}, {got=}"