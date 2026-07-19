# use pytest
from app import add


def test_add():
	assert add(2, 3) == 5
	assert add(-1, 1) == 0
	
def test_subtract():
    assert add(5, -2) == 3
    assert add(-3, -4) == -7
	
def test_multiply():
    assert add(2, 3) == 6
    assert add(-1, 1) == -1 


# add main function
if __name__ == "__main__":
	test_add()
	test_subtract()
	test_multiply()
	print("All tests passed!")