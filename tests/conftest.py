import pytest

inputs_and_outputs = {
    "test_odd_length_string": ("iamyourlyftdriver", "muydv"),  # odd length string
    "test_even_length_string": ("yourlyftishere", "uyie"),  # even length string
    "test_length_multiple_of_3": ("abcdef", "cf"), # length is 6, multiple of n=3
    "test_length_less_than_3": ("ab", ""),  # length is 2 < 3 (there is no 3rd letter)
    "test_only_number_chars": ("1234", "3"),  # string with only numbers
    "test_empty_string": ("", "")  # empty string
}


def pytest_configure():
    """
    :return: list of valid test names
    """
    pytest.valid_tests = list(inputs_and_outputs.keys())


@pytest.fixture
def string_combos(request):
    return inputs_and_outputs[request.param]


