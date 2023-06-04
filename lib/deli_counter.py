def line(list):
    if len(list) == 0:
        print("The line is currently empty.")
    else:
        line = [f"{list.index(n) + 1}. {n}" for n in list]
        print(f"The line is currently: {' '.join(line)}")

def take_a_number(list, name):
    list.append(name)
    print(f"Welcome, {name}. You are number {list.index(name) + 1} in line.")

def now_serving(list):
    if len(list) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {list[0]}.")
        del list[0]