import pygments.styles as code_styles
from manim import *


def create_code(code_str):
    code_style = code_styles.get_style_by_name("material")
    return Code(
        code=code_str,
        language="python",
        line_spacing=1.15,
        insert_line_no=False,
        background="window",
        font="Hack Nerd Font Mono",
        style=code_style,
    )


class AnimationsScene(Scene):
    def construct(self):
        title = MarkupText(
            f"Text <b><i>Animations</i></b> in <span foreground='{BLUE}'><b><u>Manim</u></b></span>",
        )

        self.play(Write(title))

        self.play(title.animate.to_edge(UP), run_time=3)

        example_str = """
        This is a multiline line string with multiple words
        to show text animations in manim
        """

        code_strs = [
            "self.play(AddTextLetterByLetter(string), run_time=5)",
            "self.play(SpiralIn(string), run_time=5)",
            "self.play(DrawBorderThenFill(string), run_time=5)",
            "self.play(ShowIncreasingSubsets(string), run_time=5)",
            "self.play(ShowSubmobjectsOneByOne(string), run_time=5)",
            "self.play(AddTextWordByWord(string), run_time=5)",
            "self.play(Unwrite(string), run_time=5)",
        ]

        code_objs = [create_code(code_str) for code_str in code_strs]
        animations = [
            AddTextLetterByLetter,
            SpiralIn,
            DrawBorderThenFill,
            ShowIncreasingSubsets,
            ShowSubmobjectsOneByOne,
            AddTextWordByWord,
            Unwrite,
        ]
        words = [
            "AddTextLetterByLetter",
            "SpiralIn",
            "DrawBorderThenFill",
            "ShowIncreasingSubsets",
            "ShowSubmobjectsOneByOne",
            "AddTextWordByWord",
            "Unwrite",
        ]
        word_locations = [
            (string.find(word), string.find(word) + len(word))
            for string, word in zip(code_strs, words)
        ]
        example = Text(example_str)
        RUN_TIME = 8

        for code, animation, locs in zip(code_objs, animations, word_locations):
            self.play(Write(code))
            self.play(code.animate.next_to(title, DOWN))

            text_to_indicate = code.code[0][locs[0] : locs[1]]
            self.play(
                animation(example),
                Circumscribe(code.code[0]),
                Indicate(text_to_indicate),
                run_time=RUN_TIME,
            )

            self.wait(2)
            self.play(FadeOut(code), FadeOut(example))
