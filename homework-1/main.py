from src.stack import Node, Stack

if __name__ == '__main__':
    n1 = Node(5, None)
    n2 = Node('a', n1)
    print(n1.data)  # 5
    print(n2.data)  # a
    print(n1)  # Node(data=5, next_node=None)
    print(n2.next_node)  # Node(data=5, next_node=None)

    stack = Stack()
    stack.push('data1')
    stack.push('data2')
    stack.push('data3')
    print(stack.top.data)  # data3
    print(stack.top.next_node.data)  # data2
    print(stack.top.next_node.next_node.data)  # data1
    print(stack.top.next_node.next_node.next_node)  # None
    try:
        print(stack.top.next_node.next_node.next_node.data)  # AttributeError: 'NoneType' object has no attribute 'data'
    except AttributeError as e:
        print(e)
