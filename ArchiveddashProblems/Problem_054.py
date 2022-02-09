from time import time
values = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']

def sumcard(cards):
    l = [i[0] for i in cards]
    j = 0
    for a in range(len(values)):
        if values[a] in l:
            j += a
    return(j)

def lis_to_values(list):
    l = [i[0] for i in list]
    p = []
    for a in l:
        for r in range(len(values)):
            if values[r] == a:
                p.append(r)
    return(p)

def one_pair(cards):
    l = [i[0] for i in cards]
    lset = set([i[0] for i in cards])
    j = 0
    for r in lset:
        if l.count(r) > j:
            j = l.count(r)
    if j == 2:
        return(True)
    else:
        return(False)

def two_pairs(cards):
    l = [i[0] for i in cards]
    lset = set([i[0] for i in cards])
    j = 0
    for r in lset:
        if l.count(r) == 2:
            j += 1
    if j == 2:
        return(True)
    else:
        return(False)

def three_of_a_kind(cards):
    l = [i[0] for i in cards]
    lset = set([i[0] for i in cards])
    j = 0
    for r in lset:
        if l.count(r) == 3:
            j += 1
    if j == 1:
        return(True)
    else:
        return(False)

def straight(cards):
    l = [i[0] for i in cards]
    for a in range(len(values)-4):
        if all(values[a+r] in l for r in range(5)):
            return(True)
        else:
            return False

def flush(cards):
    l = [i[1] for i in cards]
    if len(set(l)) == 1:
        return(True)
    else:
        return False

def full_house(cards):
    l = set([i[0] for i in cards])
    if three_of_a_kind(cards) and len(l) == 2:
        return(True)
    return False

def four_of_a_kind(cards):
    l = [i[0] for i in cards]
    lset = set([i[0] for i in cards])
    for r in lset:
        if l.count(r) == 4:
            return(True)
    return False

def straight_flush(cards):
    if straight(cards) and flush(cards):
        return(True)
    return False

def royal_flush(cards):
    l = [i[0] for i in cards]
    if set(l) == set(values[-5:]) and flush(cards):
        return(True)
    return False

def tiebreaker(list,n):
    l = [i[0] for i in list]
    for r in l:
        if l.count(r) == n:
            for a in range(len(values)):
                if r == values[a]:
                    r = a
                    return(a)

def moretiebreaker(list1,r1,list2,r2):
    l1 = set([i[0] for i in list1]) - {r1}
    l2 = set([i[0] for i in list2]) - {r2}
    if max(l1) == max(l2):
        if max(l1 - {max(l1)}) == max(l2 - {max(l2)}):
            return(min(l1) > min(l2))
        else:
            return(max(l1 - {max(l1)}) > max(l2 - {max(l2)}))
    else:
        return(max(l1) > max(l2))

def tie(list1,list2):
    l1 = set([i[0] for i in list1])
    l2 = set([i[0] for i in list2])
    for a in range(5):
        if max(l1) == max(l2):
            l1 = l1 - {max(l1)}
            l2 = l2 - {max(l2)}
        else:
            return(max(l1) > max(l2))


def winner(A_cards,B_cards):
    lis1 = lis_to_values([i[0] for i in A_cards])
    lis2 = lis_to_values([i[0] for i in B_cards])
    if royal_flush(A_cards) or royal_flush(B_cards):
        return(royal_flush(A_cards))
    elif straight_flush(A_cards) or straight_flush(B_cards):
        return(straight_flush(A_cards))
    elif four_of_a_kind(A_cards) or four_of_a_kind(B_cards):
        return(four_of_a_kind(A_cards))
    elif full_house(A_cards) or full_house(B_cards):
        return(full_house(A_cards))
    elif flush(A_cards) or flush(B_cards):
        return(flush(A_cards))
    elif straight(A_cards) or straight(B_cards):
        return straight(A_cards)
    elif three_of_a_kind(A_cards) or three_of_a_kind(B_cards):
        return(three_of_a_kind(A_cards))
    elif two_pairs(A_cards) or two_pairs(B_cards):
        return(two_pairs(A_cards))
    elif one_pair(A_cards) and one_pair(B_cards):
        if tiebreaker(A_cards,2) == tiebreaker(B_cards,2):
            return(moretiebreaker(A_cards,tiebreaker(A_cards,2),B_cards,tiebreaker(B_cards,2)))
        else:
            return(tiebreaker(A_cards,2) > tiebreaker(B_cards,2))
    elif one_pair(A_cards) or one_pair(B_cards):
        return(one_pair(A_cards))
    elif sumcard(A_cards) == sumcard(B_cards):
        return(tie(A_cards,B_cards))
    else:
        return max(lis1)>max(lis2)

t = time()
with open(r"D:\utkarsh\Github_Directories\Repo_Archived_Problems\ArchiveddashProblems\read_from_here\p054_poker.txt",'r') as f:
    stuff = f.readlines()
    ans = []
    for ele in stuff:
        j = 0
        temp = ele[:-1]
        lo = temp.split()
        lo1 = lo[:5]
        lo2 = lo[-5:]
        if winner(lo1,lo2):
            ans.append('A')
        else:
            ans.append('B')
    print((ans.count('A')), time() - t)