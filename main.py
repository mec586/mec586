# ____________________________________________________________
# import functions



# ____________________________________________________________
# solve equations

def solveEuler(variables):
    while (condition):

        # calculer ici les trucs qui dépendent pas du temps
        m1 += integrate15(pv, Dv, Rs, BM, step)
        Ts += integrate17(m, Cpl, kg, As, Rs, Tinf, m1dot, hfg, el, step)
        l += integrate19(S, gcr, Ccr, Ea, R, Ts, step)
        m3cr += integrate20(ps, l, ldot, step)
        # actualiser ici les trucs qui dépendent du temps
    return

# ____________________________________________________________
# plot solutions