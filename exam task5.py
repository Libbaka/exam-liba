from exam_lib import Book

class EBook(Book):
    def __init__(self, title, author, page_count, size, registration_code):
        super().__init__(title, author, page_count)
        self.size = size
        self._registration_code = None
        if self.check_code(registration_code):
            self._registration_code = registration_code

    @staticmethod
    def check_code(registration_code):
        if isinstance(registration_code, str) and len(registration_code) == 16 and registration_code.isdigit():
            return True
        return False

    @property
    def registration_code(self):
        return self._registration_code

    @registration_code.setter
    def registration_code(self, code):
        if self.check_code(code):
            self._registration_code = code
