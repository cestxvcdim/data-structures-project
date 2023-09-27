from typing import Any, Optional, Self, List


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
        """Конструктор класса Stack"""
        self.__stack: List[Node] = []

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} object, size={self.size}"

    @property
    def top(self) -> Optional[Node]:
        try:
            return self.__stack[-1]
        except IndexError:
            return

    @property
    def size(self) -> int:
        return len(self.__stack)

    @property
    def empty(self) -> bool:
        return self.size < 1

    def push(self, data: Any) -> None:
        self.__stack.append(Node(data=data, next_node=self.top))

    def pop(self) -> Optional[Node]:
        node = self.__stack.pop()
        return node.data
