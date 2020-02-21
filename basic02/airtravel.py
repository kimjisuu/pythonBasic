class Flight:
    def __init__(self, number):
        print('init')
        if not number[:2].isalpha():
            raise ValueError("2文字が英文字ではない")
        if not number[:2].isupper():
            raise ValueError("2文字が大文字ではない")
        if not number[2:].isdigit():
            raise ValueError("数字でない")

        self._number = number


    # def __new__(cls, number):
    #     print('new')

    def number(self):
        return self._number
