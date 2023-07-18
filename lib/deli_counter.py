def line(list_list):
    if len(list_list) == 0:
        print("The line is currently empty.")
    else:
        order_list = [f"{index+1}. {name}" for index, name in enumerate(list_list)]
        order = " ".join(order_list)
        print("The line is currently: " + order)
def take_a_number(list_list, str_person):
    list_list.append(str_person)
    position = len(list_list)
    print(f"Welcome, {str_person}. You are number {position} in line.", end="\n")
    #for index, person in enumerate(list_list, start = 1):
        #print(f"Welcome, {person}. You are number {index} in line.")
    
def now_serving(list_list):
    if len(list_list) == 0:
        print("There is nobody waiting to be served!")
    else:
        next_person = list_list[0]
        print(f"Currently serving {next_person}.")
        list_list.pop(0)

