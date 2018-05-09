def vert_mirror(strng):
    result = list()
    for word in strng:
        result.append(''.join(reversed(word)))
    return result

def hor_mirror(strng):
    strng.reverse()
    return strng

def oper(fct, s):
    return "\n".join(fct(s.splitlines()))


oper(vert_mirror, "hSgdHQ\nHnDMao\nClNNxX\niRvxxH\nbqTVvA\nwvSyRu")
# "QHdgSh\noaMDnH\nXxNNlC\nHxxvRi\nAvVTqb\nuRySvw")
oper(vert_mirror, "IzOTWE\nkkbeCM\nWuzZxM\nvDddJw\njiJyHF\nPVHfSx")
# "EWTOzI\nMCebkk\nMxZzuW\nwJddDv\nFHyJij\nxSfHVP")

oper(hor_mirror, "lVHt\nJVhv\nCSbg\nyeCt")
# "yeCt\nCSbg\nJVhv\nlVHt"
oper(hor_mirror, "njMK\ndbrZ\nLPKo\ncEYz")
# "cEYz\nLPKo\ndbrZ\nnjMK"
