from stack_queue_pseudo.stack_queue_pseudo import PseudoQueue
from stack_queue_pseudo.stack_queue_pseudo import Node
import pytest

def test_queue_one():
    new_queue_pseudo = PseudoQueue()
    new_queue_pseudo.enqueue(20)
    new_queue_pseudo.enqueue(15)
    new_queue_pseudo.enqueue(10)
    actual = str(new_queue_pseudo)
    expected = "10 -> 15 -> 20 -> None"
    assert actual == expected

def test_queue_two():
    new_queue_pseudo = PseudoQueue()
    new_queue_pseudo.enqueue(20)
    new_queue_pseudo.enqueue(15)
    new_queue_pseudo.enqueue(10)
    new_node = Node(5)
    new_queue_pseudo.enqueue(new_node)
    actual = str(new_queue_pseudo)
    expected = "5 -> 10 -> 15 -> 20 -> None"
    assert actual == expected

def test_queue_three():
    new_queue_pseudo = PseudoQueue()
    new_queue_pseudo.enqueue(20)
    new_queue_pseudo.enqueue(15)
    new_queue_pseudo.enqueue(10)
    actual = str(new_queue_pseudo.dequeue())
    expected = "20"
    assert actual == expected

def test_queue_four():
    new_queue_pseudo = PseudoQueue()
    with pytest.raises(Exception):
        new_queue_pseudo.dequeue()
