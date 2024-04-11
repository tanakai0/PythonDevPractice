
def test_answer():
    # assert 3 == 5  # Assertion
    assert 1 + 2 == 3


# content of test_class.py
class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "this"
        assert "s" in x
