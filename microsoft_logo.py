from manim import *

rect_colors = ["#F25022", "#7FBA00", "#00A4EF", "#FFB900"]


class MicrosoftLogo(MovingCameraScene):
    def construct(self):
        line = Line((0, -1, 0), (0, 1, 0), color=BLACK)
        self.add(line)
        text = Text("Microsoft", font="Segoi UI", color=WHITE)
        text.next_to(line, RIGHT, buff=0.125)
        text.set_opacity(0)
        text.save_state()
        self.add(text)
        big_rect = Rectangle(
            height=4.25, width=4.25, color=BLACK, fill_color=BLACK, fill_opacity=1
        )
        biggies = [Rectangle(color, width=2) for color in rect_colors]

        biggies[0].align_to(big_rect, UL)
        big_rectangles = [
            biggies[i + 1].next_to(biggies[i], pos)
            for i, pos in enumerate([RIGHT, DOWN, LEFT])
        ]
        big_rectangles = [biggies[0]] + big_rectangles
        big_vgroup = VGroup(big_rect, *big_rectangles)

        big_vgroup.save_state()
        small_rect = Rectangle(
            height=2.125, width=2.125, color=BLACK, fill_color=BLACK, fill_opacity=1
        )
        smallies = [
            Rectangle(color, width=1, height=1, fill_color=color, fill_opacity=1)
            for color in rect_colors
        ]
        smallies[0].align_to(small_rect, UL)
        small_rectangles = [
            smallies[i + 1].next_to(smallies[i], pos, buff=0.125)
            for i, pos in enumerate([RIGHT, DOWN, LEFT])
        ]
        small_rectangles = [smallies[0]] + small_rectangles
        small_vgroup = VGroup(small_rect, *small_rectangles)
        small_vgroup.scale(0.5)
        small_vgroup.save_state()

        for _ in range(5):
            self.play(
                ReplacementTransform(big_vgroup, small_vgroup),
            )
            self.play(
                small_vgroup.animate.next_to(line, LEFT, buff=0.125),
                text.animate.set_opacity(1).set_rate_func(rush_into),
            )
            self.wait(3)
            self.play(Restore(small_vgroup), Restore(text))
            self.play(Restore(big_vgroup))
