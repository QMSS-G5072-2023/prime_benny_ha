from prime_bh2896.prime_bh2896 import is_prime

def test_is_prime():
    assert is_prime(2)
    assert not is_prime(1)
    assert not is_prime(0)
    assert is_prime(5)
    assert not is_prime(9)

