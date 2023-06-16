"""
https://projecteuler.net/problem=68
"""

# IMPORTS
from itertools import permutations
from Timer import Timer


# FUNCTIONS
def get_is_sol(lst):
    """Function returning the list that is a solution, in the right order"""
    ind = 2 # index
    a, b, c = lst[0], lst[1], lst[2]
    tot = a + b + c
    lst_sol = [[a, b, c]]
    while ind <= len(lst) - 2:
        a, b = lst[ind+1], c
        if ind + 2 < len(lst):
            c = lst[ind+2]
        else :
            c = lst[1]
        ind += 2
        if a + b + c != tot:
            return None
        else :
            lst_sol.append([a, b, c])
    return lst_sol


def in_sols(lst):
    for i in range(len(lst)):
        new_lst1 = []
    return False


def find_solution(n):
    nb_lst = [lst for lst in permutations([i for i in range(1, n+1)])]
    sols = []
    sols_explored = []
    for lst in nb_lst:
        sol = get_is_sol(lst)
        if sol and sorted(sol) not in sols_explored:
            sols_explored.append(sorted(sol))
            sols.append(sol)


    sols_as_nb = [int("".join("".join(str(n) for n in l) for l in lst)) for lst in sols]
    sols_as_nb = [n for n in sols_as_nb if len(str(n)) < 17]

    return(max(sols_as_nb))



# TESTS
def test_sol_is_found_for_6():
    return find_solution(6) == 432621513


def test_sol_for_10_not_in_wrong_ans():
    wrong_ans = [28797161103104548, ]
    if find_solution(10) in wrong_ans:
        return True
    return False

# MAIN
if __name__ == "__main__":
    t1 = Timer()
    t1.start()
    print(find_solution(10))
    t1.stop()
    print(t1.elapsed)

