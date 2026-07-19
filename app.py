def add(a, b):
    """Return the sum of a and b.

    Works for numbers and for types that implement `+` (e.g., strings, lists).
    """
    return a + b

def subtract(a, b): 
    """Return the difference of a and b."""
    return a - b            
def multiply(a, b):
    """Return the product of a and b."""
    return a * b

if __name__ == "__main__":
    import sys
    print(add(3, 4))
    print(add(4, 4))
    print(add(6, 4))
    

