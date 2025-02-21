import re

class EmailAddressParser:
    def __init__(self, emails):
        self.emails = emails

    def parse(self):
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        email_list = re.findall(email_pattern, self.emails)

        return sorted(set(email_list))
