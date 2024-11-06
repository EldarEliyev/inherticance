# from collections import Counter
# print(Counter(['B', 'B', 'A', 'C', 'A', 'B'
#                'B', 'A', 'C']))
# print(Counter({'A':3, 'B':5, 'C':2}))
# print(Counter(A=3, B=5, C=2))


# import unittest

# def add(a, b):
#     return a + b

# class TestAddFunction(unittest.TestCase):
#     def test_add_positive_numbers(self):
#         self.assertEqual(add(1, 2), 3)

#     def test_add_negative_numbers(self):
#         self.assertEqual(add(-1, -2), -3)

#     def test_add_mixed_numbers(self):
#         self.assertEqual(add(1, -2), -1)
#         self.assertEqual(add(-1, 2), 1)

# if __name__ == '__main__':
#     unittest.main()

# import sys
# import hashlib

# def hashfile(filepath):
#     BUF_SIZE = 65536  # 64KB
#     sha256 = hashlib.sha256()
    
#     with open(filepath, 'rb') as f:
#         while True:
#             data = f.read(BUF_SIZE)
#             if not data:
#                 break
#             sha256.update(data)
    
#     return sha256.hexdigest()  # Return the hash value

# if __name__ == "__main__":
#     if len(sys.argv) < 2:
#         print("Usage: python script.py <filename>")
#         sys.exit(1)

#     file_hash = hashfile(sys.argv[1])
#     print(f"Hash: {file_hash}")


