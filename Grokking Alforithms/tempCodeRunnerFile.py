
d = {None: 1}
d.update({3: 4})
# d.setdefault(0, 0)
print({k: d[k] for k in d})