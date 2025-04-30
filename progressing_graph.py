from manim import *


class ProgressingLinesGraph(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            axis_config={"include_tip": False},
            x_axis_config={"numbers_to_include": range(0, 11, 2)},
            y_axis_config={"numbers_to_include": range(0, 11, 2)},
        )

        # Add labels
        x_label = axes.get_x_axis_label("t")
        y_label = axes.get_y_axis_label("y")

        graph_group = VGroup(axes, x_label, y_label)

        # Position the graph
        self.play(Create(graph_group))

        # Define our functions
        def line1_func(x):
            return 2 * x

        def line2_func(x):
            return 5 + 0.5 * x * x

        # Create the lines with partial drawing (start with empty graphs)
        line1 = axes.plot(line1_func, x_range=[0, 0], color=BLUE)
        line2 = axes.plot(line2_func, x_range=[0, 0], color=RED)

        # Create labels for the lines
        line1_label = MathTex("y = 2t", color=BLUE).next_to(
            axes.c2p(9, line1_func(9)), UP
        )
        line2_label = MathTex("y = 5 + 0.5t^2", color=RED).next_to(
            axes.c2p(9, line2_func(9)), DOWN
        )

        # Add the initial lines and labels to the scene
        self.play(Create(line1), Create(line2))

        self.play(Write(line1_label), Write(line2_label))

        # Define the maximum x-value for our animation
        max_x = 9

        # Gradually extend the lines over time
        self.play(
            *[
                axes.animate.plot(func, x_range=[0, max_x], color=color)
                for func, color in [(line1_func, BLUE), (line2_func, RED)]
            ],
            run_time=5,
            rate_func=linear
        )

        # Highlight the intersection point if there is one
        intersect_x = 5  # Approximately where the lines intersect
        intersect_y = line1_func(intersect_x)

        # Add dot at intersection
        intersection_dot = Dot(axes.c2p(intersect_x, intersect_y), color=YELLOW)
        intersection_label = (
            MathTex("Intersection", color=YELLOW)
            .scale(0.7)
            .next_to(intersection_dot, UR, buff=0.2)
        )

        self.play(FadeIn(intersection_dot), Write(intersection_label))

        # Wait a moment before ending
        self.wait(2)
