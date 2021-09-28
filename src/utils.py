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
    def log(function_name: str, text: str):
        print('log -', function_name + ':', text)