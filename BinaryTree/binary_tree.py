class Node:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.data = val

def binary_insert(root, node):
    if root is None:
        return node
    if root.data > node.data:
        root.l_child = binary_insert(root.l_child, node)
    else:
        root.r_child = binary_insert(root.r_child, node)
    return root

def binary_search(root, key):
    if root is None:
        return None
    elif root.data == key:
        return root.data
    elif root.data < key:
        return binary_search(root.r_child,key)
    else:
        return binary_search(root.l_child,key)

def print_tree(root):
    if not root:
        return

    print(root.data)
    print_tree(root.l_child)
    print_tree(root.r_child)

def check_key():
    print('\n Введите ключ, по которому хотите найти элемент:')
    input_key = input()
    if binary_search(r,input_key):
        print("Вершина дерева с ключом",input_key,"найдена!")
    elif binary_search(r,input_key) is None:
        print("Вершина дерева с ключом", input_key, "не найдена!")

def interval_search(root):
    print('\n Введите нижнюю границу: ')
    down = int(input())
    print('\n Введите верхнюю границу: ')
    up = int(input())
    print("Из интервала [",down,",",up,"] найдены ключи:")
    for i in range(down,up+1):
        if binary_search(root, str(i)) is not None:
            print(binary_search(root, str(i)))

 # main
f = open("keys for tree.txt")
keys_ = f.readlines()
keys = [i.strip() for i in keys_]
r = Node(keys[0])

for i in range(1,len(keys)):
    binary_insert(r, Node(keys[i]))

print_tree(r)
## dialogue with user
while(1):
    print("\nЧто вы хотите сделать с этим прекрасным деревом? Введите код:\n1 - Добавить элемент\n2 - Произвести поиск ключа\n3 - Произвести поиск по интервалу\n4 - Выйти из программы")
    choice = input()
    if choice == '1':
        print("Элемент с каким ключом вы хотите добавить?")
        input_key = input()
        if binary_search(r,input_key) is None:
            binary_insert(r,Node(input_key))
            print_tree(r)
            print("Элемент",input_key,"успешно добавлен!")
        else:
            print("Элемент с таким ключом уже существует!")

    elif choice == '2':
        check_key()
    elif choice == '3':
        interval_search(r)
    elif choice == '4':
        print("Программа завершена.")
        break
    else:
        print("Что-то вы написали не то...")