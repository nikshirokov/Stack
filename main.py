from data import comparison_dict, unballanced_list, ballanced_list


class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.stack == []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        else:
            result = self.stack.pop()
            return result

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def size(self):
        return len(self.stack)


def check_balance(braket_string):
    stack = Stack()
    for elem in braket_string:
        if elem in comparison_dict:
            stack.push(elem)
        elif elem == comparison_dict.get(stack.peek()):
            stack.pop()
        else:
            return 'Несбалансировано'
    if stack.is_empty():
        return 'Сбалансировано'


if __name__ == '__main__':
    s = Stack()
    print(f'функция is_empty - {s.is_empty()}')
    s.push(1)
    s.push(2)
    s.push(6)
    print(f'функция size - {s.size()}')
    print(f'функция peek - {s.peek()}')
    print(f'функция pop - {s.pop()}')
    print(f'функция pop - {s.pop()}')
    print(f'функция size - {s.size()}')
    print(f'функция pop - {s.pop()}')
    print(f'функция pop - {s.pop()}')
    print()
    for row in unballanced_list:
        print(check_balance(row))
    print()
    for row in ballanced_list:
        print(check_balance(row))
