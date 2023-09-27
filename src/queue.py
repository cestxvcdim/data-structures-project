from typing import Any, Optional, Self, List


class Node:
    """Класс для узла очереди"""

    def __init__(self, data: Any, next_node: Optional[Self]) -> None:
        self.data = data
        self.next_node = next_node

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(data={self.data}, next_node={self.next_node})"


class Queue:
    """Класс для очереди"""

    def __init__(self):
        self.__queue: List[Node] = []

    def __repr__(self):
        return f"{self.__class__.__name__} object, size={self.size}"

    @property
    def head(self) -> Optional[Node]:
        try:
            return self.__queue[0]
        except IndexError:
            return

    @property
    def tail(self) -> Optional[Node]:
        try:
            return self.__queue[-1]
        except IndexError:
            return

    @property
    def size(self) -> int:
        return len(self.__queue)

    @property
    def empty(self) -> bool:
        return self.size < 1

    def enqueue(self, data: Any) -> None:
        node = self.tail
        self.__queue.append(Node(data=data, next_node=None))
        if len(self.__queue) > 1:
            node.next_node = self.tail

    def dequeue(self) -> Optional[Node]:
        pass
