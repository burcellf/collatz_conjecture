
""" This is a recursive algorithm using the Collatz Conjecture """


starting_int = 7

# List to store each int from n -> 1
collatz_list = []

# Recursive function
def collatz_conjecture(n):
    
    # Add int to list
    collatz_list.append(int(n))
    
    # Collatz conjecture
    if n > 1:
        if n % 2 == 0:
            return collatz_conjecture(n / 2)
        else:
            return collatz_conjecture(n * 3 + 1)
    else:
        return 1


# Calling the function with chosen starting number
col = collatz_conjecture(starting_int)



""" Print statements below """


# Option 1
# —————————————————————————————————————————————————
# Uncomment this section to print the complete list

# for i in collatz_list:
#     print(f'{i}')
# —————————————————————————————————————————————————



# Option 2
# —————————————————————————————————————————————————
# Uncomment this section to print the list length

# print(f'\nlen: {len(collatz_list)}\n\n')
# —————————————————————————————————————————————————



# Option 3
# ——————————————————————————————————————————————————————————————————————
# Uncomment this section to print the list length for i in given range

# print(f'\n\n')
# for i in range(1, 30):
#     col = collatz_conjecture(i)
#     print(f'{i} len: {len(collatz_list)}')
# print(f'\n\n')
# ——————————————————————————————————————————————————————————————————————

