import logging

class FileManager:
    def __init__(self, file_path, mode):
        self.file_path = file_path
        self.mode = mode
        self.file = None
        self.counter = 0

    def __enter__(self):
        self.file = open(self.file_path, self.mode)
        self.counter += 1
        logging.info(f"Opened file {self.file_path}. Counter is now {self.counter}.")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        self.counter -= 1
        logging.info(f"Closed file {self.file_path}. Counter is now {self.counter}.")
        return False
