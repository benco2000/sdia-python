<<<<<<< HEAD
def is_unique(x):
=======
"""
Renvoie un booléen indiquant si la liste contient une seule fois chaque élément

Argument
x -- la liste
"""


def is_unique(x):

>>>>>>> 3c636899c387ba3f029a7fbe27a61f7616986909
    M = []
    for value in x:
        if value not in M:
            M.append(value)
<<<<<<< HEAD
    return len(M) == len(x)


def triangle_shape(height):
    """[summary]

    Args:
        height ([type]): [description]

    Returns:
        [type]: [description]
    """
    if height == 0:
        return ""
    else:
        M = ""
        for k in range(height):
            M = (
                M
                + (height - (k + 1)) * " "
                + (2 * k + 1) * "x"
                + (height - (k + 1)) * " "
            )

            if k < (height - 1):
                M = M + "\n"

    return M
=======
        else:
            return False
    return True


"""
Retourne une chaine vide si l'argument vaut 0, sinon retourne une chaine de caractère formant un triangle, avec une hauteur spécifiée par l'argument.

height -- la hauteur du triangle
"""


def triangle_shape(height):
    s = ""
    if height == 0:
        return s
    for k in range(0, height):
        if k != 0:
            s += "\n"
        t = ""
        for i in range(0, height - k - 1):
            t += " "
        for j in range(0, 2 * k + 1):
            t += "x"
        for i in range(0, height - k - 1):
            t += " "
        s += t
    return s
>>>>>>> 3c636899c387ba3f029a7fbe27a61f7616986909
