# import keyword
# import random
# import string
#
#
# def generate_random_words(length: int) -> str:
#     characters = string.ascii_letters
#     return "".join(random.choice(characters) for _ in range(length))
#
#
# # Create a python file with attributes
# attribute_names = []
# for i in range(1, 100):
#     for _ in range(100):
#         word = generate_random_words(i)
#         if word not in keyword.kwlist:
#             attribute_names.append(word)
#         else:
#             continue
#
#
# attribute_names.append("abc123")
#
# class_attributes = "\n        ".join(
#     ["self." + name + " = 1" for name in attribute_names]
# )
#
# time_calculation_string = """
# if __name__ == "__main__":
#     import timeit
#     access_time = timeit.timeit(
#         stmt = 's.abc123',
#         setup = 'from __main__ import Abc; s = Abc();',
#         number = 1,
#         # repeat = 1
#     )
#     print(access_time)
# """
# no_slot_strings = f"""
#
# class Abc:
#     def __init__(self):
#         {class_attributes}
#
# {time_calculation_string}
# """
#
# slot_strings = f"""
#
# class Abc:
#     __slots__ = {attribute_names}
#     def __init__(self):
#         {class_attributes}
#
# {time_calculation_string}
# """
# with open("no_slots.py", "w") as f:
#     f.write(no_slot_strings)
#
# with open("slots.py", "w") as f:
#     f.write(slot_strings)


class A:
    def __init__(self):
        self.a = "A"


class B:
    __slots__ = ["a"]

    def __init__(self):
        self.a = "A"


if __name__ == "__main__":
    from timeit import timeit

    no_slot = timeit(
        stmt="A()",
        setup="from __main__ import A;",
        number=1_000_000,
    )
    slot = timeit(
        stmt="B()",
        setup="from __main__ import B;",
        number=1_000_000,
    )

    print(f"Time taken by no slot instances: {no_slot}")
    print(f"Time taken by slot instances: {slot}")
