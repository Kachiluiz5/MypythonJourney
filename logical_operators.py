# we use these operators in a situation where we have multiple
# condition
has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:  #and operator we can also use the or operator
    print("You are eligible")

have_high_income = True
have_good_credit = True

if have_high_income or have_good_credit:  #and operator we can also use the or operator
    print("You are eligible")

# using the not operator
had_good_credit = True
had_criminal_case = False

if had_good_credit and not had_criminal_case:
    print("Eligible")
