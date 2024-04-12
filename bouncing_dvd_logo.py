import random

from manim import *

colors = [
    BLUE_A,
    BLUE_C,
    BLUE_E,
    GOLD,
    GREEN,
    MAROON,
    ORANGE,
    RED,
    YELLOW,
    PURPLE,
    TEAL,
    PINK,
    WHITE,
    DARK_BROWN,
]


class BouncingDVDLogo(MovingCameraScene):
    def construct(self):
        dvd_logo = ImageMobject("dvd_logo.png").scale(0.1).set_color(WHITE)

        dvd_logo.move_to([1.5, 0, 0])
        velocity = 0.03 * UR

        right_most, top_most, _ = self.camera.frame.get_corner(UR)
        left_most, bottom_most, _ = self.camera.frame.get_corner(DL)

        def update_logo(obj, velocity):

            if (
                obj.get_corner(UR)[0] >= right_most
                or obj.get_corner(DL)[0] <= left_most
            ):
                velocity[0] = -velocity[0]
                obj.set_color(random.choice(colors))

            if (
                obj.get_corner(UR)[1] >= top_most
                or obj.get_corner(DL)[1] <= bottom_most
            ):
                velocity[1] = -velocity[1]
                obj.set_color(random.choice(colors))

            obj.shift(velocity)

        self.add(dvd_logo)
        self.play(
            UpdateFromFunc(dvd_logo, lambda x: update_logo(x, velocity)), run_time=60
        )
