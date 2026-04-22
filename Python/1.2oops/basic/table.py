from prettytable import PrettyTable

table = PrettyTable()

#Access Method
table.add_column("Pokemon name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])

#Access Attribute
table.align = "l"


print(table)