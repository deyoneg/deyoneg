def date_time(time: str) -> str:
    import re

    def checkone(num):
        return "" if int(num) == 1 else "s"

    r = list(map(int, re.findall(r"(\d{2}).(\d{2}).(\d{4}) (\d{2}):(\d{2})", time)[0]))
    m = (
        "blank January February March April May June July August September October November December"
    ).split()
    p = f"{(r[0])} {m[int(r[1])]} {r[2]} year {r[3]} hour{checkone (r[3])} {r[4]} minute{checkone (r[4])}"
    return p
