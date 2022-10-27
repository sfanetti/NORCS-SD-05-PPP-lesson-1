def arb_args(*args):
    for a in args:
        print(a)

arb_args(5, 4, 2, "pickles", True)

def inner_func(a, b):
    def inner_1():
        print("inside function inner_1")
        return a * b
    def inner_2():
        print("inside function inner_2")
        return a % b
    print(int(inner_1()) + int(inner_2()))

inner_func(50, 420)

def lunch_lady(student_name, meal="Mystery Meat"):
    print(f"The student {student_name} likes to eat {meal}")

lunch_lady("Scott", "Cafeteria Pizza")
lunch_lady("Derek", "Hot Dogs")
lunch_lady("Joe")

def sum_n_product(a,b):
    return a + b, a * b

_sum, _product = sum_n_product(5, 10)

print(sum_n_product(5, 10))
print(_sum)
print(_product)

alias_arb_args = arb_args

alias_arb_args(4, 6, 7, "monkeys")

def arb_mean(*args):
    total = 0
    for a in args:
        total += a
    print(total/len(args))

arb_mean(100, 100, 100, 80, 78, 100, 30)

def arb_longest_string(*strings):
    cur_length = 0
    longest_str = ""
    for s in strings:
        if len(s) > cur_length:
            longest_str = s
            cur_length = len(s)
    return longest_str

print(arb_longest_string("Foo", "bar", "baz")) 
print(arb_longest_string("Pickles", "Polymer", "zippity-doo-dah"))      
