import collections.abc
import copy
import os


def update_deep(d, u, first=True):
    """
    Deep update
    https://stackoverflow.com/a/3233356/2425183
    """
    if first:
        d = copy.deepcopy(d)
        u = copy.deepcopy(u)
    for k, v in u.items():
        if isinstance(v, collections.abc.Mapping):
            d[k] = update_deep(d.get(k, {}), v, False)
        else:
            d[k] = v
    return d


def asset_path(name: str) -> str:
    return os.path.join(os.path.dirname(__file__), 'assets', name)
