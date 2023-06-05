from _stack import Stack

def validate_brackets(_string):
    brackets_value = {"{":"}","[":"]","(":")"}
    bracket_stack = Stack()

    for char in _string:
        if char in brackets_value.keys():
            bracket_stack.push(char)
        elif char in brackets_value.values():
            try:
                if brackets_value[str(bracket_stack.peek())] != char:
                    raise Exception()
                bracket_stack.pop()
            except:
                return False
    
    if bracket_stack.is_empty():
        return True
    else:
        return False
            
                
            

if __name__ == "__main__":
    _str1 = "{}"
    _str2 = "{}(){}"
    _str3 = "()[[Extra Characters]]"
    _str4 = "(){}[[]]"
    _str5 = "{}{Code}[Fellows](())"
    _str6 = "[({}]"
    _str7 = "(]("
    _str8 = "{(})"
    _str9 = "{"
    _str10 = ")"
    _str11 = "[}"

    print(1,validate_brackets(_str1),"TRUE")
    print(2,validate_brackets(_str2),"TRUE")
    print(3,validate_brackets(_str3),"TRUE")
    print(4,validate_brackets(_str4),"TRUE")
    print(5,validate_brackets(_str5),"TRUE")
    print(6,validate_brackets(_str6),"FALSE")
    print(7,validate_brackets(_str7),"FALSE")
    print(8,validate_brackets(_str8),"FALSE")
    print(9,validate_brackets(_str9),"FALSE")
    print(10,validate_brackets(_str10),"FALSE")
    print(11,validate_brackets(_str11),"FALSE")