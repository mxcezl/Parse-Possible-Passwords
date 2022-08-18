import re

class PasswordMatcher:
    def __init__(self, min_length, max_length) -> None:
        self.min_length = min_length
        self.max_length = max_length
        self.BASE_PATTER = '^(?=.*[A-Z])(?=.*[!@#$&*])(?=.*[0-9])(?=.*[a-z]).{%1,%2}$'
        self.pattern = None

        self.check_min_max()
        self.create_pattern()

    def check_min_max(self) -> bool:
        if not self.min_length or self.min_length <= 0:
            self.min_length = ''
        if not self.max_length or self.max_length < self.min_length:
            self.max_length = ''

    def create_pattern(self) -> None:
        self.pattern = self.BASE_PATTER
        self.pattern = self.pattern.replace('%1', str(self.min_length))
        self.pattern = self.pattern.replace('%2', str(self.max_length))
        self.pattern = re.compile(self.pattern)

    def isPasswordValid(self, password: str) -> bool :
        return None != self.pattern.match(password)