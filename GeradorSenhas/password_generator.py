import random
import string


class PasswordGenerator:
    def __init__(self, length=8, use_upper=True, use_lower=True, use_numbers=True, use_symbols=True):
        if not (use_upper or use_lower or use_numbers or use_symbols):
            raise ValueError("Pelo menos um critério deve ser selecionado.")

        self.length = length
        self.use_upper = use_upper
        self.use_lower = use_lower
        self.use_numbers = use_numbers
        self.use_symbols = use_symbols

    def generate(self):
        char_pools = []
        password = []

        if self.use_upper:
            char_pools.append(string.ascii_uppercase)
            password.append(random.choice(string.ascii_uppercase))
        if self.use_lower:
            char_pools.append(string.ascii_lowercase)
            password.append(random.choice(string.ascii_lowercase))
        if self.use_numbers:
            char_pools.append(string.digits)
            password.append(random.choice(string.digits))
        if self.use_symbols:
            char_pools.append('!@#$%&*')
            password.append(random.choice('!@#$%&*'))

        all_chars = ''.join(char_pools)

        if len(password) > self.length:
            raise ValueError("O tamanho é menor que a quantidade de tipos selecionados.")

        remaining_length = self.length - len(password)
        password += random.choices(all_chars, k=remaining_length)

        random.shuffle(password)
        return ''.join(password)
