import pytest
from src.queue import Queue, Node

queue = Queue()


def test_enqueue():
    queue.enqueue(1)
    assert queue.head.data == 1
    assert queue.head.next_node is None
    queue.enqueue(2)
    assert queue.tail.data == 2
    assert queue.head.data == 1
    assert isinstance(queue.head.next_node, Node)


def test_dequeue():
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    assert queue.dequeue() is None
