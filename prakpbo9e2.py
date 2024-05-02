class P9E2:
    @staticmethod
    def methodTambah(x, y=None):
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            return x + y
        elif isinstance(x, float) or isinstance(y, float):
            return x + y
        else:
            raise TypeError("Tipe data tidak valid")

myNum1 = P9E2.methodTambah(8, 5)
myNum2 = P9E2.methodTambah(4.5, 6.5)
print("int:", myNum1)
print("float:", myNum2)
