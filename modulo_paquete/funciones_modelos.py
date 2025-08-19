def fibor(ord):
    if ord < 0:
        return None
    elif ord == 0:
        return 1
    elif ord == 1:
        return 1
    else:
        return fibor(ord - 1) + fibor(ord - 2)


def fiboi(ord):
    if ord < 0:
        return None
    elif ord == 0:
        return 1
    elif ord == 1:
        return 1
    else:
        unoAnt = 1
        dosAnt = 1
        for n in range(2, ord + 1):
            nuevo = dosAnt + unoAnt
            dosAnt = unoAnt
            unoAnt = nuevo
        return unoAnt
