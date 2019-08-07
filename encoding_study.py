class String:
    def __init__(self, st: str):
        self.raw = st

    def unicode_hex_string(self):
        codes = map(lambda x: x + ': ' + hex(ord(x)), self.raw)
        return '\n'.join(codes)

    def utf8_hex_string(self):
        return self._hex_string_by_encoding('utf_8')

    def utf16_hex_string(self):
        return self._hex_string_by_encoding('utf_16_be')  # 使用 big endian 使得下面的字符串打印更有可读性

    def utf32_hex_string(self):
        return self._hex_string_by_encoding('utf_32_be')

    def _hex_string_by_encoding(self, encoding):
        codes = map(lambda x: x + ': ' + '0x' + x.encode(encoding).hex(), self.raw)
        return '\n'.join(codes)


s = String('abc123知乎者也✔️🇵🇷é')

print('unicode:\n' + s.unicode_hex_string() + '\n')
print('utf-8:\n' + s.utf8_hex_string() + '\n')
print('utf-16:\n' + s.utf16_hex_string() + '\n')
print('utf-32:\n' + s.utf32_hex_string() + '\n')
