def is_unique(x):
    M = []
    for value in x:
        if value not in M:
            M.append(value)
    return len(M) == len(x)


def triangle_shape(height):
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
