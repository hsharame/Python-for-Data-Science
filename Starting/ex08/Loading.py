import os
import time


def format_time(seconds):
    """
    Change the time format from seconds to mm:ss
    """
    m = int(seconds / 60)
    s = int(seconds % 60)
    return f"{m:02d}:{s:02d}"


def ft_tqdm(lst: range) -> None:
    """
    Mini tqdm. Prints a dynamically updating
    progressbar every time a value is requested
    """
    size = os.get_terminal_size().columns
    len_range = len(lst)
    len_digit = len(str(len_range))
    start = time.time()
    bar_len = size - 5 - (len_digit * 2 + 1) - 28
    for i, val in enumerate(lst, 1):
        percent = int(i * 100 / len_range)
        done = int(i * bar_len / len_range)
        bar = "█" * done + " " * (bar_len - done)
        elapsed = time.time() - start
        vitesse = i / elapsed if elapsed > 0 else 0
        remain = (len_range - i) / vitesse if vitesse > 0 else 0
        print(
            f"{percent:3d}%|{bar}| {i}/{len_range} "
            f"[{format_time(elapsed)}<{format_time(remain)},"
            f"{vitesse:05.2f}it/s] ",
            end="\r"
            )
        yield val
    print()
