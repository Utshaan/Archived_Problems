from random import choice, randint
from rich import print
from time import time

ti = time()
square = [
    "GO",
    "A1",
    "CC1",
    "A2",
    "T1",
    "R1",
    "B1",
    "CH1",
    "B2",
    "B3",
    "JL",
    "C1",
    "U1",
    "C2",
    "C3",
    "R2",
    "D1",
    "CC2",
    "D2",
    "D3",
    "FP",
    "E1",
    "CH2",
    "E2",
    "E3",
    "R3",
    "F1",
    "F2",
    "U2",
    "F3",
    "G2J",
    "G1",
    "G2",
    "CC3",
    "G3",
    "R4",
    "CH3",
    "H1",
    "T2",
    "H2",
]


def generate_game():
    l = [i for i in range(1, 17)]
    ch_list = []
    cc_list = []
    while len(ch_list) < 2:
        ele = choice(l)
        ch_list.append(ele)
        l.remove(ele)

    l = [i for i in range(1, 17)]
    while len(cc_list) < 10:
        ele = choice(l)
        cc_list.append(ele)
        l.remove(ele)

    return cc_list, ch_list


ch_order = ["GO", "JL"]
cc_order = ["GO", "JL", "C1", "E3", "H2", "R1", "RN", "RN", "UN", "3B"]

occurance = [0]*40
pos = 0
rep = [0, 0, 0]
cc_list, ch_list = generate_game()
c_card, h_card = 1, 1


def play():
    global square, ch_order, cc_order, occurance, pos, rep, cc_list, ch_list, c_card, h_card
    roll1, roll2 = randint(1, 4), randint(1, 4)
    if roll1 == roll2:
        rep = rep[1:] + [1]
    else:
        rep = rep[1:] + [0]
    pos += roll1 + roll2
    pos %= 40
    if c_card > 16:
        c_card = 1
    if h_card > 16:
        h_card = 1
    match square[pos]:
        case "CH1" | "CH2" | "CH3":
            if c_card in cc_list:
                match cc_order[cc_list.index(c_card)]:
                    case "GO":
                        pos = 0
                    case "JL":
                        pos = 10
                    case "C1":
                        pos = square.index("C1")
                    case "E3":
                        pos = square.index("E3")
                    case "H2":
                        pos = square.index("H2")
                    case "R1":
                        pos = square.index("R1")
                    case "RN":
                        match square[pos]:
                            case "CC1":
                                pos = square.index("R1")
                            case "CC2":
                                pos = square.index("R3")
                            case "CC3":
                                pos = square.index("R4")
                    case "UN":
                        match square[pos]:
                            case "CC1":
                                pos = square.index("U1")
                            case "CC2":
                                pos = square.index("U2")
                    case "3B":
                        pos -= 3
                        if square[pos] == "G2J":
                            pos = 10
                    case _:
                        pass
            c_card += 1

        case "CC1" | "CC2" | "CC3":
            if h_card in ch_list:
                match ch_order[ch_list.index(h_card)]:
                    case "GO":
                        pos = 0
                    case "JL":
                        pos = 10
                    case _:
                        pass
            h_card += 1
        case "G2J":
            pos = 10
        case _:
            pass

    if rep == [1, 1, 1]:
        pos = 10
    occurance[pos] += 1


for _ in range(1000000):
    play()

s = ""
for x in sorted(occurance, reverse=True)[:3]:
    print(f"{square[occurance.index(x)]}: {x}")
    s += str(occurance.index(x))
print(s)
print(f"Time Taken: {time() - ti} seconds")
