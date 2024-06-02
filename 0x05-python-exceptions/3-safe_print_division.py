#!/usr/bin/python3
def safe_print_division(a, b):
    """Returns the division of a by b."""
    try:
        res = a / b
    except Exception:
        res = None
    finally:
        print('Inside result: {}'.format(res))
    return res
