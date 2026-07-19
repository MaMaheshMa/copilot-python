# use pytest 
from app import add


def test_add():
	assert add(2, 3) == 5
	assert add(-1, 1) == 0
  

#add main function
if __name__ == "__main__":
    test_add()
    print("All tests passed!")  