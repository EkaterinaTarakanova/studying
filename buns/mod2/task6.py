web_name = input("Введите доменое имя сайта")
first_dot = web_name.find(".")
third_lvl = str(web_name[:first_dot])
second_dot = web_name.find(".", first_dot + 1)
second_lvl = str(web_name[first_dot + 1:second_dot])
first_lvl = str(web_name[second_dot + 1:])
print(first_lvl, second_lvl, third_lvl, sep = "\n")
