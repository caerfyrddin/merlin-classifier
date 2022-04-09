class Utils:
    @staticmethod
    def remove_prefix(self: str, prefix: str) -> str:
        if self.startswith(prefix):
            return self[len(prefix):]
        else:
            return self[:]

    @staticmethod
    def remove_suffix(self: str, suffix: str) -> str:
        if suffix and self.endswith(suffix):
            return self[:-len(suffix)]
        else:
            return self[:]

    @staticmethod
    def int_to_16_byte_hex(i: int) -> str:
        s = hex(i)[2:].rjust(16, '0')
        return '-'.join([ s[0:4], s[4:8], s[8:12], s[12:16] ])