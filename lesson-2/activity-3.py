def name_args(**kwargs):
    for key in kwargs.keys():
        print(f"{key}: {kwargs[key]}")

name_args(foo=1, bar=2, baz=3, fubar = "This is a string", foobizzle = True)

def all_true(*iterable):
    return all(iterable)

print(all_true(True, True, False))    
print(all_true(True, True, True, 0))    

def one_true(*elements):
    return any(elements)

print(one_true(0, False, False, "foo"))    


def recursive_factorial(n):
    if n <=1:
        return 1
    else:
        return n * recursive_factorial(n -1)

print(recursive_factorial(52))

def recursive_deduplicate(my_str, i=0):
    if len(my_str) <= 1 or i == len(my_str) - 1:
        return my_str
    if my_str[i] == my_str[i + 1]:
        return recursive_deduplicate(my_str[0:i] + my_str[i + 1:], i)
    else:
        return recursive_deduplicate(my_str, i + 1)

print(recursive_deduplicate("aaaaa"))        
print(recursive_deduplicate("aaaaabbbbb"))  
print(recursive_deduplicate("mississippi"))  
print(recursive_deduplicate("AABBCCDD"))  
print(recursive_deduplicate("chicken"))  

def recursive_reverse(str, i = 0):
    if len(str) == 0:
        print("in the empty string condition")
        return ""
    elif i == len(str) - 1:
        print(f"First char is {str[0]} in {str}")
        return str[0]
    else:
        print(f"First char is {str[-1 - i]} in {str} with {i}")
        return str[-1 - i] + recursive_reverse(str, i + 1) 

print(recursive_reverse("Apple")) 
print(recursive_reverse("SuperCalifragilisticExpialidocious"))        