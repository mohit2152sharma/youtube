from manim import *

from code_transform import CodeTransform


class MacOSScene(MovingCameraScene):
    def construct(self):
        # Create a colorful gradient background
        background = Rectangle(
            width=config.frame_width,
            height=config.frame_height,
            fill_opacity=1,
            stroke_width=0,
        )
        colors = ["#706D54", "#A08963", "#C9B194", "#DBDBDB"]
        background.set_color_by_gradient(colors)

        # Create macOS-style window
        window_width = config.frame_width - 1
        window_height = config.frame_height - 1
        window = RoundedRectangle(
            width=window_width,
            height=window_height,
            corner_radius=0.3,
            fill_color="#FFFFFF",
            fill_opacity=0.9,
            stroke_color="#DDDDDD",
            stroke_width=1,
        )

        # Create window top bar
        top_bar = RoundedRectangle(
            width=window_width,
            height=0.7,
            corner_radius=[0.3, 0, 0, 0.3],
            fill_color="#E1DFE1",
            fill_opacity=1,
            stroke_width=0,
        )
        top_bar.align_to(window, UP)

        # Create window buttons (traffic lights)
        close_button = Circle(
            radius=0.13, fill_color="#FF5F57", fill_opacity=1, stroke_width=0
        )
        minimize_button = Circle(
            radius=0.13, fill_color="#FFBD2E", fill_opacity=1, stroke_width=0
        )
        maximize_button = Circle(
            radius=0.13, fill_color="#28CA42", fill_opacity=1, stroke_width=0
        )

        buttons = VGroup(close_button, minimize_button, maximize_button).arrange(
            RIGHT, buff=0.2
        )
        buttons.move_to(top_bar)
        buttons.align_to(top_bar, LEFT)
        buttons.shift(-LEFT * 0.2)

        # Create window dock bar at the bottom of the screen
        mac_ui = VGroup(
            background,
            window,
            top_bar,
            buttons,
        )

        # Add everything to the scene at once as the background
        self.add(mac_ui)

        # Create code block with the function
        code_str = """def foo(value, a = []): 
    return a.append(value)
    """

        code_block = Code(
            code_string=code_str,
            tab_width=4,
            language="python",
            add_line_numbers=False,
            background_config={
                "color": "#000000",
                "stroke_color": "#000000",
                "background_stroke_width": 0,
            },
            formatter_style="material",
        )

        # Place the code in the center of the window
        code_block.move_to(mac_ui.get_center())
        print(Code.get_styles_list())

        # Add the code block to the scene with animation
        fade_in = FadeIn(code_block)
        self.play(fade_in)
        self.wait(1)

        # Move the code to the top left corner
        # target_position = window.get_corner(UL) + RIGHT * 0.25 + DOWN * 0.95
        # # self.add(Circle(radius=1).move_to(target_position, aligned_edge=UL))
        # self.play(code_block.animate.move_to(target_position, aligned_edge=UL), run_time=1.5)
        # print(code_block.get_styles_list())

        code2 = """foo(1)"""
        code_block2 = Code(
            code_string=code2,
            tab_width=4,
            language="python",
            add_line_numbers=False,
        )

        self.play(CodeTransform(code_block, code_block2))

        self.wait(2)
