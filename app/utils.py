def retrieve_n_letter(input_string: str, n: int = 3) -> str:
    """
    :param input_string: string we want to cut
    :param n: nth letter we wish to extract (cut) from input_string
    :return: every nth letter of input_string extracted
    """
    if not isinstance(input_string, str):
        raise TypeError(f"Invalid input type of {str(type(input_string))} for input_string")
    result = ""
    for i in range(n-1, len(input_string), n):
        result += input_string[i]
    return result
