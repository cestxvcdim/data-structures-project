from src.queue import Queue

if __name__ == '__main__':
    queue = Queue()

    # Магический метод __str__ возвращает строку с размером очереди
    assert str(Queue()) == "Queue object, size=0"

    # Добавляем данных в очередь
    queue.enqueue('data1')
    queue.enqueue('data2')
    queue.enqueue('data3')

    # Проверяем очередность хранения данных
    n1 = queue.head
    assert n1.data == 'data1'
    n2 = queue.head.next_node
    assert n2.data == 'data2'
    n3 = queue.tail
    assert n3.data == 'data3'
    dn = queue.tail.next_node
    assert dn is None
    try:
        print(queue.tail.next_node.data)  # AttributeError: 'NoneType' object has no attribute 'data'
    except AttributeError as e:
        print(e)

    # Проверяем магический метод __str__
    assert str(queue) == "Queue object, size=3"
