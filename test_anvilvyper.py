# test_anvilvyper.py
"""
Tests for AnvilVyper module.
"""

import unittest
from anvilvyper import AnvilVyper

class TestAnvilVyper(unittest.TestCase):
    """Test cases for AnvilVyper class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AnvilVyper()
        self.assertIsInstance(instance, AnvilVyper)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AnvilVyper()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
