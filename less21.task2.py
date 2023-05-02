import unittest
import tempfile
import os

class TestFileManager(unittest.TestCase):

    def test_file_manager_with_existing_file(self):
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(b'test data')
            file_path = temp_file.name
        with FileManager(file_path, 'r') as file:

            self.assertEqual(file.read(), 'test data')

        os.unlink(file_path)

    def test_file_manager_with_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            with FileManager('nonexistent_file.txt', 'r') as file:
                pass

    def test_file_manager_context_count(self):
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            file_path = temp_file.name

        with FileManager(file_path, 'r') as file1:
            with FileManager(file_path, 'r') as file2:
                self.assertEqual(file1.counter, 2)

        with FileManager(file_path, 'r') as file:
            self.assertEqual(file.counter, 0)

        os.unlink(file_path)

if __name__ == '__main__':
    unittest.main()
