def count_in_list(lst: list, s: any) -> int:
    """
    Counts the number of occurrences of an element in a list
    """
    count = 0
    for element in lst:
        if element == s:
            count += 1
    return count
