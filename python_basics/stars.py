def draw_stars(list):
    for el in list:
        if isinstance(el, int):
            print '*' * el
        elif isinstance(el, str):
            el = el.lower()
            print el[:1] * len(el)

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

draw_stars(x)
