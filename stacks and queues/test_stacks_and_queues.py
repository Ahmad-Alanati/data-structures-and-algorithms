from stacks_and_queues import Stack,Queue

def test_stack_one():
    new_stack = Stack()
    actual = new_stack.is_empty()
    expected = True
    assert actual == expected

def test_stack_two():
    new_stack = Stack()
    new_stack.push(5)
    actual = new_stack.is_empty()
    expected = False
    assert actual == expected

def test_stack_three():
    new_stack = Stack()
    actual = new_stack.peek()
    expected = "the stack is empty"
    assert actual == expected

def test_stack_four():
    new_stack = Stack()
    new_stack.push(5)
    actual = str(new_stack.peek())
    expected = "5"
    assert actual == expected

def test_stack_five():
    new_stack = Stack()
    new_stack.push(5)
    new_stack.push(4)
    actual = str(new_stack.peek())
    expected = "4"
    assert actual == expected

def test_stack_six():
    new_stack = Stack()
    new_stack.push(5)
    new_stack.push(4)
    actual = str(new_stack.pop())
    expected = "4"
    assert actual == expected

def test_stack_seven():
    new_stack = Stack()
    new_stack.push(5)
    new_stack.push(4)
    new_stack.pop()
    actual = str(new_stack.pop())
    expected = "5"
    assert actual == expected

def test_stack_eight():
    new_stack = Stack()
    actual = new_stack.pop()
    expected = "you can't pop from an empty stack"
    assert actual == expected

# queue

def test_queue_one():
    new_queue = Queue()
    actual = new_queue.is_empty()
    expected = True
    assert actual == expected

def test_queue_two():
    new_queue = Queue()
    new_queue.enqueue(5)
    actual = new_queue.is_empty()
    expected = False
    assert actual == expected

def test_queue_three():
    new_queue = Queue()
    actual = new_queue.peek()
    expected = "the queue is empty"
    assert actual == expected

def test_queue_four():
    new_queue = Queue()
    new_queue.enqueue(5)
    actual = str(new_queue.peek())
    expected = "5"
    assert actual == expected

def test_queue_five():
    new_queue = Queue()
    new_queue.enqueue(5)
    new_queue.enqueue(4)
    actual = str(new_queue.peek())
    expected = "5"
    assert actual == expected

def test_queue_six():
    new_queue = Queue()
    new_queue.enqueue(5)
    new_queue.enqueue(4)
    actual = str(new_queue.dequeue())
    expected = "5"
    assert actual == expected

def test_queue_seven():
    new_queue = Queue()
    new_queue.enqueue(5)
    new_queue.enqueue(4)
    new_queue.dequeue()
    actual = str(new_queue.dequeue())
    expected = "4"
    assert actual == expected

def test_queue_eight():
    new_queue = Queue()
    actual = new_queue.dequeue()
    expected = "you can't dequeue form an empty queue"
    assert actual == expected