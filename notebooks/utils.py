def cast_to_number(string_with_symbols):
    """converts a string to a number by removing commas and percentage signs
    """
    if isinstance(string_with_symbols, float):  # already a number!
        return string_with_symbols
    no_commas = string_with_symbols.replace(',', '')
    no_percent = no_commas.replace('%', '')
    number = float(no_percent)
    return number