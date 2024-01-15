#This is a grocery list tracker
#initialize an empty list to store the data
grocery_list = []

#Create a loop such that you can input your desire no. of inputs and pressing "n" stops the loop
while True:
    item_to_add = input("Add an item to your list(or type N to stop): ")
    if item_to_add.upper() == "N":
        break
      
    # items = item_to_add.split(",")
    # added_item_string += item_to_add + ", "
    grocery_list.append(item_to_add)

    print(grocery_list)

print(grocery_list)


removed_items_list = []

while True:
    items_to_remove=input("Enter items you would like to remove.(N to quit):")
    if items_to_remove.upper() == "N":
        break

    removed_items_list.append(items_to_remove)

    print(removed_items_list)

#Iterate through the removed item list and if the item is in the grocery list remove it 
for item in removed_items_list:
    if item in grocery_list:
        grocery_list.remove(item)
    else:
        print(f"{item} is not in your list.")

#display the new updated list where items have been removed
updated_grocery_list = print(grocery_list)


#I should  display the list as a numbered list from top to bottom and not in []

