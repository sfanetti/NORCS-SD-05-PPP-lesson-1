print("Hello from inside the file")

def hello():
    print("Hello User")

def pack(item_1, item_2, item_3):
    return [item_1, item_2, item_3]

def eat_lunch(lunch_items):
    if len(lunch_items) == 0:
        print("Ain't got no lunch!")
    else:
        for i in range(len(lunch_items)):
            if i == 0:
                print(f"First I eat {lunch_items[i]}")
            else:
                print(f"Next I eat {lunch_items[i]}")

hello()
print(pack("a", "b", "c"))
eat_lunch([])
eat_lunch(["Pork Chop"])
eat_lunch(["Pork Chop", "Tandori Chicken", "Beef Suprise", "Sprite"])