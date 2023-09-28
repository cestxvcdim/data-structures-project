from typing import Any, Optional, Self


class Node:
    """Класс для узла очереди"""

    def __init__(self, data: Any, next_node: Optional[Self]) -> None:
        self.data = data
        self.next_node = next_node

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(data={self.data}, next_node={self.next_node})"


class Queue:
    """Класс для очереди"""

    def __init__(self) -> None:
        self._head: Optional[Node] = None
        self._tail: Optional[Node] = None

    def __repr__(self) -> str:
        return f"Queue<{str(self._head)}>"

    def __str__(self) -> str:
        return f"{self.__class__.__name__} object, size={self.size}"

    def __len__(self) -> int:
        return self.size

    @property
    def head(self) -> Optional[Node]:
        return self._head

    @property
    def tail(self) -> Optional[Node]:
        return self._tail

    @property
    def size(self) -> int:
        size = 0
        node = self._head
        while node:
            node = node.next_node
            size += 1
        return size

    @property
    def empty(self) -> bool:
        return self._head is None

    def enqueue(self, data: Any) -> None:
        node = Node(data=data, next_node=None)
        if not self.empty:
            self._tail.next_node = node
        else:
            self._head = node
        self._tail = node

    def dequeue(self) -> Optional[Node]:
        pass
