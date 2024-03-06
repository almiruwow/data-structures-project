"""Здесь надо написать тесты с использованием unittest для модуля stack."""
from src.stack import Stack
import unittest

stack = Stack()
stack.push('data1')
stack.push('data2')
stack.push('data3')


class TestStack(unittest.TestCase):
    def test_stack(self):
        self.assertEquals(stack.top.data, 'data3')
        self.assertEquals(stack.top.next_node.data, 'data2')
        self.assertEquals(stack.top.next_node.next_node.data, 'data1')
        self.assertEquals(stack.top.next_node.next_node.next_node, None)

    def test_errors(self):
        with self.assertRaises(AttributeError):
            stack.top.next_node.next_node.next_node.data


pop = Stack()
pop.push('data1')
pop.push('data2')
remove = pop.pop()
pop.push('data3')


class TestPop(unittest.TestCase):
    def test_pop(self):
        self.assertEquals(pop.top.data, 'data3')
        self.assertEquals(pop.top.next_node.data, 'data1')
        self.assertEquals(remove, 'data2')