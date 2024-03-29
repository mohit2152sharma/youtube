from manim import *


class ThreeBodyLogo(MovingCameraScene):

    def construct(self):

        background = ImageMobject("./three_body_problem_background.jpeg")
        background.stretch_to_fit_width(width=config.frame_width)
        background.stretch_to_fit_height(height=config.frame_height)
        self.add(background)

        def create_circle_animation(
            radius: int,
            scale_to,
            align: bool = False,
            align_dir=LEFT,
            prev_circle=None,
            **kwargs,
        ):
            fill_color = kwargs.get("fill_color", None)
            color = kwargs.get("color", None)
            opacity = kwargs.get("fill_opacity", None)
            c1 = Circle(
                radius=radius,
                fill_color=fill_color,
                color=color,
                fill_opacity=0,
                stroke_opacity=0,
            ).shift(UP)
            c2 = c1.copy().scale(scale_to).set_opacity(opacity)
            if align:
                c2.align_to(prev_circle, align_dir)
            return Transform(c1, c2), c2

        animation1, c2 = create_circle_animation(
            4, 0.15, fill_color="#bc8455", color="#bc8455", fill_opacity=1
        )
        animation2, c3 = create_circle_animation(
            4,
            0.3,
            True,
            RIGHT,
            c2,
            fill_color="#cc9c67",
            color="#cc9c67",
            fill_opacity=1,
        )
        animation3, c4 = create_circle_animation(
            4,
            0.6,
            True,
            LEFT,
            c3,
            fill_color="#fee4b2",
            color="#fee4b2",
            fill_opacity=1,
        )

        title = Text(
            "3    BODY\nPROBLEM",
            font="HaymerW01-Bold",
            t2c={"[:5]": WHITE, "[5:9]": RED, "[:-1]": WHITE},
            line_spacing=0.6,
        )
        title.next_to(c4, DOWN, buff=0.8)

        animations = AnimationGroup(animation3, animation2, animation1, lag_ratio=0.3)
        self.play(animations, run_time=20)
        self.play(AddTextLetterByLetter(title), run_time=10)
        self.wait(3)
