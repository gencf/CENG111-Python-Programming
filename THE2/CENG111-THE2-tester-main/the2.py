for _ in range(160000):
    id = input()
    qmark = id.find("?")

    id = list(id)

    if id[5] == "X":
        check_digit = 10
    elif id[5] != "?":
        check_digit = int(id[5])

    if qmark == -1:
        if (2 * int(id[0]) + 3 *  int(id[1]) + 5 * int(id[2]) + 7 * int(id[3])) % 11 == check_digit:
            print("VALID")
        else:
            print("INVALID")

    elif qmark == 5:
        check_digit = (2 * int(id[0]) + 3 *  int(id[1]) + 5 * int(id[2]) + 7 * int(id[3])) % 11
        if check_digit == 10:
            id[5] = "X"
        else:
            id[5] = str(check_digit)
        print("".join(id))

    else:
        if qmark == 0:
            x = (6 * (check_digit - (3 * int(id[1]) + 5 * int(id[2]) + 7 * int(id[3])))) % 11
            
        if qmark == 1:
            x = (4 * (check_digit - (2 * int(id[0]) + 5 * int(id[2]) + 7 * int(id[3])))) % 11

        if qmark == 2:
            x = (20 * (check_digit - (2 * int(id[0]) + 3 * int(id[1]) + 7 * int(id[3])))) % 11

        if qmark == 3:
            x = (8 * (check_digit - (2 * int(id[0]) + 3 * int(id[1]) + 5 * int(id[2])))) % 11
        
        if x == 10:
            id[qmark] = "X"  
            
        else:
            id[qmark] = str(x)

        print("".join(id))

