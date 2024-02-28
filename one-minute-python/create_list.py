"""This is a script for one minute video on python, showing all the ways of how to create a list"""

import pygments.styles as code_styles
from manim import *
from manim_voiceover import VoiceoverScene

from _eleven_voiceover import ElevenLabsService


def create_code_scene(code: str):
    code_style = code_styles.get_style_by_name("monokai")
    return Code(
        code=code,
        language="python",
        line_spacing=1.15,
        insert_line_no=False,
        background="window",
        font="Hack Nerd Font Mono",
        style=code_style,
    )


class PythonList(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            ElevenLabsService(model="eleven_monolingual_v1", voice="Ryan Kurk")
        )

        title = Text("So you think you know lists?")
        with self.voiceover("So you think you know lists?"):
            self.add(title)

        self.wait(1)

        self.remove(title)

        one_minute_python = Text("#oneminutepython")
        with self.voiceover(
            "Welcome to one minute python video series! through which I share python tips and tricks"
        ):
            self.play(Write(one_minute_python))

        with self.voiceover(
            "Today I am going to cover all the ways you can create a list in python"
        ):
            self.play(FadeOut(one_minute_python))

        code1 = create_code_scene(code="my_list = [1, 2, 3, 4, 5]")

        with self.voiceover(
            "Here's the first one, the simplest one, using square brackets"
        ):
            self.play(FadeIn(code1))

        code2 = create_code_scene(
            code="""
            x = list((1, 2, 3, 4))
            print(x)
            # [1, 2, 3, 4]

            y = list("abc")
            print(y)
            # ['a', 'b', 'c']
            """
        )

        code1.generate_target()
        code1.target.become(code2)

        with self.voiceover(
            "Second is using list function. This function is mostly used to convert a sequence of elements like tuple or string to list"
        ):
            self.play(MoveToTarget(code1))
            self.add(code2)
            self.remove(code1)

        self.wait(1)
        code3 = create_code_scene(
            code="""
            my_list = [ x for x in range(6) ]
            """
        )

        code2.generate_target()
        code2.target.become(code3)

        with self.voiceover(
            "Third is using list comprehension. They are particularly useful when you want to apply an operation to each item in an iterable (such as a list, tuple, or range) and collect the results into a new list"
        ):
            self.play(MoveToTarget(code2))
            self.add(code3)
            self.remove(code2)

        self.play(FadeOut(code3))
        self.wait(1)

        with self.voiceover(
            "Thanks for watching, be sure to like and subscribe for more one minute python!"
        ):
            self.play(Write(Text("Please like and subscribe!")))
