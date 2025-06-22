from code_transform import CodeTransform
from manim import *

config.background_color = "#222222"


def create_code(code_str: str) -> Code:
    c = Code(
        code_string=code_str,
        language="python",
        formatter_style="material",
        add_line_numbers=False,
        background_config={"stroke_width": 0},
    )
    print(c.default_background_config)
    return c


class CodeScene(Scene):

    def construct(self):
        code_str = create_code("def f(): ...")
        code_str_2 = create_code("def f(x): ...")
        image = ImageMobject("ellipsis.png").scale_to_fit_height(config.frame_height)
        self.add(image)
        # self.play(Write(image))
        # dots = Text("...hello").scale(1.5)
        # cursor = Rectangle(
        #     color=GREY_A,
        #     fill_color=GREY_A,
        #     fill_opacity=1.0,
        #     height=0.5,
        #     width=0.1,
        # ).move_to(dots[0])
        # #
        # self.play(TypeWithCursor(dots, cursor=cursor))
        self.wait(3)
        # code_str = """def f(): pass"""
        #
        # code_str_2 = """def f(x): pass"""
        #
        # code1 = Code(
        #     code_string=code_str,
        #     language="python",
        #     formatter_style="material",
        #     background="rectangle",
        # )
        #
        # code2 = Code(
        #     code_string=code_str_2,
        #     language="python",
        #     formatter_style="material",
        #     background="rectangle",
        # )
        #
        # self.play(CodeTransform(code_str, code_str_2), run_time=5)
        # self.wait(3)
