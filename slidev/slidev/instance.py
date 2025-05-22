class A:
    _a = None
    _connection = None

    def __new__(cls, *args, **kwargs):
        if cls._a is None:
            cls._a = super().__new__(cls)
            cls._a._connection = cls._a.connect()
            print("cls created")
        else:
            print("connection already created reusing")
        return cls._a

    def __init__(self, name) -> None:
        self.name = name
        print(f"{name} initalised")
        print(self._connection)

    def connect(self):
        if self._connection:
            print("reusing connection")
        else:
            print("connected successfully")
        return "connection"


a = A("a")
b = A("b")


class Singleton:
    def __new__(cls, *args, **kwargs):
        print(f"args from new method: {args}")
        return super().__new__(cls)

    def __init__(self, *args):
        print(f"args from init method: {args}")


s = Singleton("hello world")
