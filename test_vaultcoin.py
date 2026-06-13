# test_vaultcoin.py
"""
Tests for VaultCoin module.
"""

import unittest
from vaultcoin import VaultCoin

class TestVaultCoin(unittest.TestCase):
    """Test cases for VaultCoin class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = VaultCoin()
        self.assertIsInstance(instance, VaultCoin)
        
    def test_run_method(self):
        """Test the run method."""
        instance = VaultCoin()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
