import unittest
from flipping_for_heads import GVCoin, flip_for_heads

class TestGVCoin(unittest.TestCase):
    def setUp(self):
        self.coin = GVCoin(15)

    def test_initial_state(self):
        self.assertTrue(self.coin.get_is_heads())
        self.assertEqual(self.coin.num_flips(), 0)
        self.assertEqual(self.coin.num_heads(), 0)
        self.assertEqual(self.coin.num_tails(), 0)

    def test_flip(self):
        self.coin.flip()
        self.assertEqual(self.coin.num_flips(), 1)
        if self.coin.get_is_heads():
            self.assertEqual(self.coin.num_heads(), 1)
            self.assertEqual(self.coin.num_tails(), 0)
        else:
            self.assertEqual(self.coin.num_heads(), 0)
            self.assertEqual(self.coin.num_tails(), 1)

    def test_set_to_heads(self):
        self.coin.set_to_heads(True)
        self.assertTrue(self.coin.get_is_heads())
        self.coin.set_to_heads(False)
        self.assertFalse(self.coin.get_is_heads())

class TestFlipForHeads(unittest.TestCase):
    def test_flip_for_heads(self):
        coin = GVCoin(15)
        result = flip_for_heads(coin, 5)
        self.assertEqual(result, coin.num_flips())
        self.assertEqual(coin.num_heads(), 5)

if __name__ == "__main__":
    unittest.main()