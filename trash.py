m = {
    '/': ['a', 'd', 23352670],
    'a': ['e', 94269],
    'e': 584,
    'd': 24933642,
    }

for dir in m:
    if isinstance(m[dir], int):
        print(m[dir])