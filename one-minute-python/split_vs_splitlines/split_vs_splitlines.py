from manim import *
from manim_voiceover import VoiceoverScene

from _eleven_voiceover import ElevenLabsService
from _utils import create_code_scene

manager = ElevenLabsService(voice="Markus - Mature and Chill")
dev = ElevenLabsService(voice="Ryan Kurk")
voiceover = ElevenLabsService(voice="Knightley - dapper and deep narrator")

image_dir = "./one-minute-python/split_vs_splitlines/"
example_string = '''
example_string = """
I have this string 


that I need to split
on new lines character

but it's creating blank characters
"""

example_string.split("\\n")
# [
#     '', 
#     'I have this string ',
#     '', 
#     '',
#     'that I need to split',
#     'on new lines character',
#     '',
#     "but it's creating blank characters",
#     ''
# ]
'''
splitlines_string_1 = """
'ab c\\n\\nde fg\\rkl\\r\\n'.splitlines()
# ['ab c', '', 'de fg', 'kl']
"""

splitlines_string_2 = """
''.split('\\n')
# ['']

''.splitlines()
# []

'abc\\n'.split('\\n')
# ['abc', '']

'abc\\n'.splitlines()
# ['abc']
"""

splitlines_string = ''' 
example_string = """I have this string 


that I need to split
on new lines character
"""

example_string.splitlines()
# [
#     'I have this string ',
#     '', 
#     '',
#     'that I need to split',
#     'on new lines character',
# ]

list(filter(bool, example_string.splitlines()))
# [
#     'I have this string ',
#     'that I need to split',
#     'on new lines character',
# ]
'''


class JuniorSenior(VoiceoverScene):
    def construct(self):
        junior = ImageMobject(image_dir + "junior.jpeg")
        junior.scale(0.5).to_edge(RIGHT)
        senior = ImageMobject(image_dir + "senior.webp")
        senior.scale(0.5).to_edge(LEFT)
        self.add(junior, senior)
        one_minute_python = Text("#oneminutepython")

        # add voiceover: welcome to one minute python
        self.set_speech_service(voiceover)
        with self.voiceover("Welcome to one minute python"):
            self.play(Write(one_minute_python))
        self.wait(1)

        with self.voiceover("Today we have - "):
            ...

        with self.voiceover("A junior engineer - "):
            self.play(Indicate(junior))

        with self.voiceover("and a senior engineer helping him out -"):
            self.play(Indicate(senior))
        self.remove(one_minute_python)
        # add voiceover: I need help
        self.set_speech_service(dev)
        with self.voiceover("Hey...I need your help"):
            self.play(junior.animate.scale(1.3), senior.animate.scale(0.8))

        junior_code = create_code_scene(example_string).scale(0.5)
        # self.add(junior_code)
        self.play(Write(junior_code))

        # self.play(code_string.animate.to_edge(UP).scale(0.5))
        # add voiceover: I have this example string
        with self.voiceover(
            "I have this string. I am trying to split it on new lines, but it is not working. - "
        ):
            example_string_vgroup = junior_code.code[:10]
            self.play(Indicate(example_string_vgroup))

        # add voiceover when I use split
        with self.voiceover("When i use split -"):
            split_string = junior_code.code[10]
            self.play(Indicate(split_string))

        # add voiceover it creates blank lines
        with self.voiceover("it adds empty strings to the list. - "):
            output_string = junior_code.code[11:]
            self.play(Indicate(output_string))
            self.play(Circumscribe(output_string[3:5]))
            self.play(Circumscribe(output_string[7]))
            self.play(Circumscribe(output_string[9]))

        self.wait(1)

        # add voiceover: you should use splitlines
        self.set_speech_service(manager)
        with self.voiceover("You should use split lines..."):
            self.play(
                FadeOut(junior_code),
                senior.animate.scale(1.2 / 0.8),
                junior.animate.scale(0.8 / 1.3),
            )

        # here's an example. It not only handles new line charactes but also carriage
        # returns.

        self.remove(junior_code)

        split_lines_ex1 = create_code_scene(splitlines_string_1).scale(0.6)
        with self.voiceover(
            "Here I will explain with some examples...It not only handles new line characters but also carriage returns..."
        ):
            self.play(Write(split_lines_ex1))

        self.wait(2)
        # split_lines_ex1.generate_target()
        # here's another example.
        split_lines_ex2 = create_code_scene(splitlines_string_2)
        # split_lines_ex1.target.become(split_lines_ex2)
        self.play(FadeOut(split_lines_ex1))
        with self.voiceover("Here are some more examples - "):
            self.play(Write(split_lines_ex2))
        # self.add(split_lines_ex2)
        # example 1 voiceover and explaination
        # self.remove(split_lines_ex1)
        ex1_code = split_lines_ex2.code[:3]
        ex2_code = split_lines_ex2.code[3:5]
        ex3_code = split_lines_ex2.code[6:8]
        ex4_code = split_lines_ex2.code[9:]
        with self.voiceover(
            "In the first example, when you use split with new line characters - "
        ):
            self.play(Indicate(ex1_code))
        with self.voiceover(
            " - instead of empty list - It returns a list with empty string"
        ):
            self.play(Circumscribe(ex1_code[1]))

        with self.voiceover("But if use splitlines - It will return an empty list -"):
            self.play(Indicate(ex2_code))
            self.play(Circumscribe(ex2_code[1]))

        with self.voiceover(
            "Likewise, if you line terminates with a new line character. - "
        ):
            self.play(Indicate(ex3_code))
        with self.voiceover(
            "Using split, will add an  additional blank string to the list - "
        ):
            self.play(Circumscribe(ex3_code[1]))

        with self.voiceover("But it's not the case with splitlines -"):
            self.play(Indicate(ex4_code))
            self.play(Circumscribe(ex4_code[1]))

        # self.remove(split_lines_ex2)
        # self.remove(split_lines_ex1)
        self.play(FadeOut(split_lines_ex2))
        splitlines_code = create_code_scene(splitlines_string).scale(0.5)
        with self.voiceover("Coming back to your example -"):
            self.play(Write(splitlines_code))
        self.wait(2)
        output1 = splitlines_code.code[9:16]
        with self.voiceover("One thing you will notice - "):
            self.play(Indicate(output1))
        with self.voiceover(
            " - that there are blank strings even after using splitlines - "
        ):
            self.play(Circumscribe(output1[2:4]))

        filter_code = splitlines_code.code[16]
        filter_code_output = splitlines_code.code[17:]
        with self.voiceover("To remove them - you can use the following expression"):
            # self.play(Circumscribe(filter_code, scale_factor=1.2, color=GREEN))
            self.play(Indicate(filter_code_output))

        self.wait(2)
        self.play(FadeOut(splitlines_code))

        thanks_for_watching = Text("Thanks for watching")
        like = Text("If you like the video")
        subscribe = Text("Please like and subscribe").shift(RIGHT * 0.5)

        self.set_speech_service(voiceover)
        with self.voiceover("Thanks for watching -"):
            self.play(Write(thanks_for_watching))
        thanks_for_watching.generate_target()
        thanks_for_watching.target.become(like)

        with self.voiceover("If you like the video -"):
            self.play(MoveToTarget(thanks_for_watching))

        thanks_for_watching.target.become(subscribe)
        with self.voiceover("Please like and subscribe"):
            self.play(MoveToTarget(thanks_for_watching))
        self.wait(2)
