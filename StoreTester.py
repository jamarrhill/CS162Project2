import unittest
import Store

class StoreTester(unittest.TestCase):
    def test_Store(self):
        p = Store.Product(1, "iPad", "Tablet", 1200.00, 25)
        s = Store.Store()
        s.add_product(p)
        self.assertIs(p.get_title(), "iPad")
        self.assertIs(p.get_description(), "Tablet")
        self.assertTrue(p.get_price(), 1200.00)
        self.assertNotEqual(p.get_quantity(),19)
        self.assertEqual(s.searchStore("Ipad"),[1])
if __name__ == "main":
    unittest.main()
