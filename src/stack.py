from typing import Any, Optional, Self


class Node:
    """Класс для узла стека"""

    def __init__(self, data: Any, next_node: Optional[Self]) -> None:
        self.data = data
        self.next_node = next_node

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(data={self.data}, next_node={self.next_node})"


class Stack:
    """Класс для стека"""

    def __init__(self) -> None:
        self._top: Optional[Node] = None

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}<{str(self._top)}>"

    def __str__(self) -> str:
        return f"{self.__class__.__name__} object, size={self.size}"

    def __len__(self) -> int:
        return self.size

    @property
    def top(self) -> Optional[Node]:
        return self._top

    @property
    def size(self) -> int:
        size = 0
        node = self._top
        while node:
            node = node.next_node
            size += 1
        return size

    @property
    def empty(self) -> bool:
        return self._top is None

    def push(self, data: Any) -> None:
        self._top = Node(data=data, next_node=self._top)

    def pop(self) -> Optional[Any]:
        node = self._top
        if node is None:
            return
        self._top = node.next_node
        return node.data
