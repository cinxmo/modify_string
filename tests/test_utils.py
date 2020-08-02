import pytest
from app.utils import retrieve_n_letter


@pytest.mark.parametrize('string_combos', pytest.valid_tests, indirect=True)
def test_retrieve_n_letter(string_combos):
    input_string = string_combos[0]
    expected_output_string = string_combos[1]
    assert retrieve_n_letter(input_string) == expected_output_string


def test_test_retrieve_n_letter_invalid_input():
    with pytest.raises(TypeError) as e:
        retrieve_n_letter(1234)  # integer instead of string as input
    assert str(e.value) == "Invalid input type of <class 'int'> for input_string"

