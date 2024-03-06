from manim import *

config.background_color = WHITE


class Props:
    blue = "#4285F4"
    red = "#DB4437"
    yellow = "#F4B400"
    green = "#0F9D58"

    dot_radius = 0.5

    arc_inner_radius = 1
    arc_outer_radius = 1.5
    arc_angle = PI / 2

    blue_start_angle = -PI / 4
    red_start_angle = -7 * PI / 4
    yellow_start_angle = -5 * PI / 4
    green_start_angle = -3 * PI / 4


class GoogleLogo(Scene):
    def create_dot(self, color, radius, **kwargs):
        return Dot(color=color, radius=radius, **kwargs)

    def arrange_dots(self, blue, red, yellow, green):
        blue.move_to((-3, 0, 0))
        red.move_to((-1, 0, 0))
        yellow.move_to((1, 0, 0))
        green.move_to((3, 0, 0))

    def annulus_sector(
        self,
        color,
        start_angle,
        angle=PI / 2,
        inner_radius=Props.arc_inner_radius,
        outer_radius=Props.arc_outer_radius,
    ):
        return AnnularSector(
            inner_radius=inner_radius,
            outer_radius=outer_radius,
            color=color,
            fill_opacity=1.0,
            start_angle=start_angle,
            angle=angle,
            stroke_width=0,
        )

    def construct(self):
        blue, red, green, yellow = [
            self.create_dot(c, Props.dot_radius)
            for c in (Props.blue, Props.red, Props.green, Props.yellow)
        ]

        self.arrange_dots(blue, red, yellow, green)

        dots = VGroup(blue, red, yellow, green)
        dots.save_state()

        bounce_animation = [
            AnimationGroup(
                x.animate(rate_func=there_and_back).shift(UP * 0.5),
                x.animate(rate_func=there_and_back).shift(DOWN * 0.5),
            )
            for x in dots
        ]

        # transform dots to letter G
        blue_annulus, red_annulus, yellow_annulus, green_annulus = [
            self.annulus_sector(c, a, ang)
            for c, a, ang in zip(
                [Props.blue, Props.red, Props.yellow, Props.green],
                [
                    Props.blue_start_angle,
                    Props.red_start_angle,
                    Props.yellow_start_angle,
                    Props.green_start_angle,
                ],
                [PI / 4] + [PI / 2] * 3,
            )
        ]
        dots_minus_blue = VGroup(red, yellow, green)
        sectors_minus_blue = VGroup(red_annulus, yellow_annulus, green_annulus)

        transformations = [
            ReplacementTransform(
                dot,
                sect,
                path_func=utils.paths.path_along_circles(
                    -2 * PI / 5, yellow.get_center()
                ),
            )
            for dot, sect in zip(dots_minus_blue, sectors_minus_blue)
        ]

        blue_slab = Rectangle(height=0.5, width=1.5, color=Props.blue, fill_opacity=1)
        blue_slab.next_to(blue_annulus, UP, aligned_edge=UR, buff=0)
        blue_slab.set_stroke(width=0)
        blue_annulus.set_stroke(width=0)
        dot_to_slab = ReplacementTransform(blue, blue_slab)

        blue_slab_copy = blue_slab.copy().set_opacity(0)
        slab_to_annulus = ReplacementTransform(blue_slab_copy, blue_annulus)

        # play animations together
        for i in range(1, 20):
            self.play(LaggedStart(*bounce_animation, lag_ratio=0.1))
            if i % 5 == 0:
                self.play(
                    LaggedStart(
                        *transformations, *(dot_to_slab, slab_to_annulus), lag_ratio=0.1
                    )
                )
                self.wait(1)
                self.remove(
                    *sectors_minus_blue, blue_annulus, blue_slab_copy, blue_slab
                )
                self.play(Restore(dots))
        self.wait(3)
