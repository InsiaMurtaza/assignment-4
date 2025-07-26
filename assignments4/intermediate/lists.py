def add_item():
    fruits_list:list = ["apple","banana","orange","grape","pineapple"]
    print(len(fruits_list))
    fruits_list.append("mango")
    print(fruits_list)

# lst = ["hawk","eagle","parrot","pigeon","flamingo","sparrow"]
# lst = ["laughing toy",45,"The Great Bay",9011,"life forever",74,"goodbye"]

def get_item(lst:list,index:int):
    if index <= len(lst):
        return lst[index]
    else:
        return "No item exists on this index no."
    
def replace_item(lst:list,index:int,item:str):
    if index <= len(lst):
        lst[index] = item
        return lst
    else:
        return "This index no. does not exist"

def slice_lst(lst:list,index:int,endindex:int):
    if index <= len(lst) and endindex <= len(lst):
        return lst[index:endindex]
    else:
        return "The index number/s you have entered does/do not exist"
    
def main():
    lst = ["laughing toy",45,"The Great Bay",9011,"life forever",74,"goodbye"]
    ask_user = int(input(f"""What do ypu want to do? Select by number: 
                     1.Access
                     2.Modify
                     3.Slice
                    """))
    if ask_user == 1:
        again_ask = int(input("Enter the index no. "))
        access = get_item(lst,again_ask)
        print(access)
    elif ask_user == 2:
        ask_index = int(input("Enter the index no. "))
        ask_item = input("Enter the new item to be replaced: ")
        modify = replace_item(lst,ask_index,ask_item)
        print(modify)
    elif ask_user == 3:
        ask_starting_index = int(input("Enter the starting index no. "))
        ask_end_index = int(input("Enter the ending index no. "))
        slice = slice_lst(lst,ask_starting_index,ask_end_index)
        print(slice)
    else:
        print("Invalid Choice!!")

if __name__ == '__main__':
    main()

