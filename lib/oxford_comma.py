def oxford_comma(items):
    if len(items) <= 1: return items[0]
    return ", ".join(items[0:-1]) + (f" and {items[-1]}" if len(items) == 2 else f", and {items[-1]}")
    # return (", ".join(items[0:-1]) + f" and {items[-1]}") if len(items) == 2 else (", ".join(items[0:-1]) + f", and {items[-1]}")
