import pytest
from src.stack import Stack, Node

stack = Stack()


def test_push():
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.top.data == 3
    assert stack.top.next_node.data == 2
    assert stack.top.next_node.next_node.data == 1
    assert stack.top.next_node.next_node.next_node is None
    assert isinstance(stack.top.next_node.next_node, Node)


def test_pop():
    stack.push(1)
    n1 = stack.pop()
    assert stack.empty is True
    assert n1 is not None
    stack.push(2)
    stack.push(3)
    assert stack.size == 2
