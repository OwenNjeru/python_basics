# list datastructure (Ordered)
# lists are mutable /changeable
my_list = ["Banana", "Mangoes", "Oranges", "Apples"]
my_list.sort()
print(my_list)
# changeable
my_list[1] = "berry"
print(f"I love eating {my_list[1]}")


my_numlist = [1, 3, 8, 5, 7]
my_numlist.sort()
my_numlist.append(45)
print(my_numlist)

# tuple datastructure (ordered)
# tuples are immutable/ unchangeable and

my_tuple = ("toyota","range","subaru""mercedes", "bmw")
print(f"{my_tuple[3]} is manufactured in Japan")


# set_datastructure

my_set = {"Kenya", "Uganda", "Tanzania", "Mozambique", "Djibouti"}
my_set.add("Morocco")
print(my_set)

# dictionaries

my_dic = {"Name":"Owen","Age":"18","Gender":"Male","Profession":"Web developer"}
print(my_dic)
print(f"My name is {my_dic['Name']}")
print(f"My name is {my_dic['Name']}, {my_dic['Age']} years of age and am currently a {my_dic['Profession']}")