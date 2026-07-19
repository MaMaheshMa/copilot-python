# use pytest
from app import add


def test_add():
	assert add(2, 3) == 5
	assert add(-1, 1) == 0
	
def test_subtract():
    assert add(5, -2) == 3
    assert add(-3, -4) == -7


# add main function
if __name__ == "__main__":
	test_add()
	test_subtract()
	print("All tests passed!")