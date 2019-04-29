#!python
from redact_problem import redact
import unittest

class RedactTest(unittest.TestCase):
    def test_redact_valid_inuts(self):
        w = ["one", "fish", "two", "fish", "red", "fish", "blue", "fish"]
        # test one input
        b = ["fish"]
        assert redact(w, b) == ["one", "two", "red", "blue"]
        # test multiple inputs
        b = ["fish", "one"]
        assert redact(w, b) == ["two", "red", "blue"]
        # test no input
        b = []
        assert redact(w, b) == w
        # test inputs are same 
        b = w
        assert redact(w, b) == []
