from tabulate import tabulate


def beautify(input):
    return _beautify_dict(input)


# FIXME needs to guarantee dict order
def _beautify_dict(input):
    return tabulate(input, headers="keys", tablefmt="fancy_grid")
