


# Input lists
C = [2, 5, 9, 12, 13, 15, 16, 17, 18, 19]
F = [2, 4, 5, 6, 7, 9, 13, 16]
H = [1, 2, 5, 9, 10, 11, 12, 13, 15]

# Convert the lists to sets for faster membership checking
C_set = set(C)
F_set = set(F)
H_set = set(H)

# Students who play all three sports
all_sports_players = sorted(list(C_set & F_set & H_set))

# Students who play both cricket and football but not hockey
cf_not_h = sorted(list((C_set & F_set) - H_set))

# Students who play exactly two sports
exactly_two_sports = sorted(list(((C_set & F_set) | (C_set & H_set) | (F_set & H_set)) - set(all_sports_players)))

# Students who don't play any of the three sports
no_sports = sorted(list(set(range(1, 21)) - (C_set | F_set | H_set)))

# Print the results
print("Students who play all three sports:", all_sports_players)
print("Students who play both cricket and football but don’t play hockey:", cf_not_h)
print("Students who play exactly two of the sports:", exactly_two_sports)
print("Students who don’t play any of the three sports:", no_sports)
