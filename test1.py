for string, result in zip(["junyiacademy", "flipped class room is important"],
                          ["ymedacaiynuj", "deppilf ssalc moor si tnatropmi"]):
    rs = " ".join(["".join([list(i)[c] for c in range(len(list(i))-1, -1, -1)]) for i in string.split(' ')])
    print(rs)
    assert result == rs
