guests = ["William", "Logan", "James", "Emily"]
employees = ["Theresa", "Elsie", "Bernard", "Ashley"]
hosts = ["Dolores", "Hector", "Teddy", "Peter"]

the_first_two_guests = guests[0:2] #this is called "Slicing"
print("The first two guests are: ", the_first_two_guests)

the_middle_two_guests = guests[1:3]
print("The middle two guests are: ", the_middle_two_guests)

first_two_employees = employees[:2]
print("The first two employees: ", first_two_employees)

the_last_2_emoloyees = employees[2:]
print("The last two employees: ", the_last_2_emoloyees)

the_last_3_hosts = hosts[-3:]
print("The last three hosts: ", the_last_3_hosts)