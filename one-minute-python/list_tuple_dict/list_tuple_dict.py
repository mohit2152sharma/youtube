"""List, tuple and dictionary walks into a bar"""


from manim import *
from manim_voiceover import VoiceoverScene

from _eleven_voiceover import ElevenLabsService
from _utils import create_code_scene

image_dir = "./one-minute-python/list_tuple_dict/"


class ListTupleDict(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            ElevenLabsService(model="eleven_monolingual_v1", voice="Ryan Kurk")
        )

        with self.voiceover("List, tuple and dictionary walks into a bar"):
            img = ImageMobject(image_dir + "list_tuple_dict_on_a_table.png")
            self.add(img)

        self.wait(1)
        self.play(FadeOut(img))
        one_minute_python = Text("#oneminutepython")
        with self.voiceover("Welcome to one minute python video series!"):
            self.play(Write(one_minute_python))

        self.wait(1)
        self.remove(one_minute_python)

        with self.voiceover(
            "So what would you guys like to order? We have a faboulous drinks menu"
        ):
            waiter = ImageMobject(image_dir + "waiter.jpeg")
            self.add(waiter)

        self.wait(1)
        self.play(FadeOut(waiter))
        # self.play(FadeOut(one_minute_python))

        with self.voiceover("I would like to order 0th drink"):
            img3 = ImageMobject(image_dir + "2.png")
            self.add(img3)

        self.wait(1)
        self.play(FadeOut(img3))

        with self.voiceover("Same, I would also like to order 0th drink"):
            img4 = ImageMobject(image_dir + "tuple_drink.png")
            self.add(img4)

        self.wait(1)
        self.play(FadeOut(img4))

        with self.voiceover("I would like to order gin and tonic"):
            img5 = ImageMobject(image_dir + "dict_drink.png")
            self.add(img5)

        self.wait(1)
        self.play(FadeOut(img5))

        with self.voiceover("Thank you gentlemen, I will get your order right way"):
            self.add(waiter)

        self.remove(waiter)

        with self.voiceover("Wait, can I modify my order"):
            img6 = ImageMobject(image_dir + "tuple_modify.png")
            self.add(img6)

        self.remove(img6)

        with self.voiceover(
            "I am sorry sir, you are not allowed to do that. However I can get you a new order"
        ):
            self.add(waiter)

        self.wait(1)
        self.play(FadeOut(waiter))

        code = create_code_scene(
            code="""
            lst = ["gin", "tonic", "scotch"]
            lst[0]
            # gin 

            tupl = ("gin", "tonic", "scotch")
            tupl[0]
            # gin 

            dict = {"gin": "gin", "tonic": "tonic", "scotch": "scotch"}
            dict["gin"]
            # gin

            tupl[0] = "new_order"
            # TypeError: 'tuple' object does not support item assignment
            """,
        ).scale(0.75)
        script = "So what did we learn? Lists and Tuples in python are zero indexed. While dictionaries can be indexed with \
        keys. Tuples are immutable, once created you cannot change it's elements. However you can create a new tuple and reassign \
        it to older one. Lists and dictionaries are mutable, you can change their elements"
        with self.voiceover(script):
            self.play(Write(code))

        self.play(FadeOut(code))
        outro = "Please like and subscribe for more one minute python"
        with self.voiceover(outro):
            self.play(Write(Text(outro)))
        self.wait(1)
