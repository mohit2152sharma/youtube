from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.elevenlabs import ElevenLabsService

from _utils import create_code_scene


class ManimPositions(VoiceoverScene):

    def construct(self):
        self.set_speech_service(ElevenLabsService(voice_name="Rylan - calming male"))

        rectangle = Rectangle()
        text = Circle().scale(0.5)
        with self.voiceover(
            """
            You created a rectangle...<bookmark mark='a'/>
            . Now, you want to move the rectangle to upper right corner of the screen...<bookmark mark='b'/>
            Now you also want to add some object to inside the upper right corner of the rectangle ... <bookmark mark='c'/>
            """
        ) as tracker:
            self.play(
                Create(rectangle),
                run_time=tracker.time_until_bookmark(mark="a", limit=1),
            )
            rectangle.save_state()

            self.play(
                rectangle.animate.to_edge(UR),
                run_time=tracker.time_until_bookmark(mark="b"),
            )

            text.align_to(rectangle, UR)

            self.play(Create(text), run_time=tracker.time_until_bookmark(mark="c"))

        self.wait(2)
        with self.voiceover("How do you do all these things?"):
            self.play(Unwrite(text))
            self.play(Restore(rectangle))
            self.play(Uncreate(rectangle))

        video_title = Text("How to position objects in manim?")

        self.wait(2)
        with self.voiceover(
            "Hello ... in today's video I am going to cover <bookmark mark='d'/>, How to position objects in manim? ... <bookmark mark='e'/>"
        ) as tracker:
            self.wait_until_bookmark(mark="d")
            self.play(
                Write(video_title), run_time=tracker.time_until_bookmark(mark="e")
            )

        with self.voiceover(
            """
            But before, I jump into the video, disclaimer ...
            The voiceover of this video is generated by eleven labs and the source code of this video is mentioned in the description ...
            """
        ) as tracker:
            self.play(Unwrite(video_title), run_time=tracker.duration)

        self.wait(2)
        with self.voiceover(
            """
            Whenever you create an <bookmark mark='f'/> 
            object, by default manim places it <bookmark mark='g'/> 
            at the center of the screen <bookmark mark='h'/>
            """
        ) as tracker:
            rect2 = Rectangle(height=6, width=6)
            origin_dot = Dot()
            coordinates = MathTex("(0, 0, 0)").scale(0.5)
            coordinates.next_to(origin_dot, UP, buff=0.1)
            self.wait_until_bookmark("f")

            self.play(
                Create(rect2),
                run_time=tracker.time_until_bookmark("g"),
            )

            self.add(origin_dot)
            self.play(Write(coordinates), run_time=tracker.time_until_bookmark("h"))

        with self.voiceover(
            """
            Manim also has some constant vectors like <bookmark mark='i'/> 
            up ... upper  right - right - down right - down - down left - left - upper left ... <bookmark mark='j'/> 
            These constants help to easily move around the objects <bookmark mark='k'/>.
            """
        ) as tracker:

            position_vectors = [UP, UR, RIGHT, DR, DOWN, DL, LEFT, UL]
            position_vectors_str = [
                "UP",
                "UR",
                "RIGHT",
                "DR",
                "DOWN",
                "DL",
                "LEFT",
                "UL",
            ]
            dots = [Dot() for _ in position_vectors]
            dot_labels = [MathTex(string).scale(0.5) for string in position_vectors_str]
            dot_group = []
            for dot, position, dot_label in zip(dots, position_vectors, dot_labels):

                dot_label.next_to(dot, position, buff=0.05)
                dot_label.add_updater(
                    lambda m, d=dot, p=position: m.next_to(d, p, buff=0.05)
                )
                dot_group.append(
                    AnimationGroup(
                        dot.animate.move_to(position), Write(dot_label), lag_ratio=1
                    ),
                )

            animation_group = AnimationGroup(*dot_group, lag_ratio=0.3)

            self.wait_until_bookmark("i")
            self.play((animation_group), run_time=tracker.time_until_bookmark("j"))

            self.play(
                rect2.animate.move_to(UR), run_time=tracker.time_until_bookmark("k")
            )
            self.play(rect2.animate.move_to(ORIGIN))

        self.play(*[Uncreate(dot) for dot in dots])
        self.play(*[Uncreate(label) for label in dot_labels])
        self.play(Uncreate(coordinates))
        self.play(Uncreate(origin_dot))

        self.play(rect2.animate.stretch_to_fit_height(config.frame_height - 1))
        self.play(rect2.animate.stretch_to_fit_width(config.frame_width - 1))

        with self.voiceover(
            """
            There are two ways position objects in manim. First is <bookmark mark='l'/> 
            absolute positioning <bookmark mark='m'/> 
            ... and second is <bookmark mark='n'/> relative positioning ...<bookmark mark='o'/>
            """
        ) as tracker:

            absolute_positioning = MathTex("1.\;Absolute\;Positioning")
            relative_positioning = MathTex("2.\;Relative\;Positioning")
            relative_positioning2 = relative_positioning.copy()
            relative_positioning.next_to(absolute_positioning, DOWN, buff=0.5)
            self.wait_until_bookmark("l")
            self.play(Create(absolute_positioning))

            self.wait_until_bookmark("n")
            self.play(Create(relative_positioning))

        sq = Square()

        self.play(
            absolute_positioning.animate.to_edge(UP),
            AnimationGroup(
                Uncreate(relative_positioning), Transform(rect2, sq), lag_ratio=1
            ),
        )

        with self.voiceover(
            """
            Absolute Positioning is relative to origin ... 
            There are bunch of methods which help to move an object relative to origin.<bookmark mark='p'/> 
            Starting with move to ... <bookmark mark='q'/> 
            All m objects have this method, and this method requires a three dimensional array to move the object
            to that position <bookmark mark='r'/>
            . Remember move to method moves object relative to origin.
            """
        ) as tracker:

            code_str = "rectangle.animate.move_to([3, -3, 0])"
            strt, end = code_str.find("move_to([3, -3, 0])"), code_str.find(
                "move_to([3, -3, 0])"
            ) + len("move_to([3, -3, 0])")
            code = create_code_scene(code_str)
            code.next_to(absolute_positioning, DOWN, buff=0.5)
            self.wait_until_bookmark("p")
            self.play(Create(code), run_time=tracker.time_until_bookmark("q"))

            self.play(
                rect2.animate.move_to([3, -3, 0]),
                Indicate(code.code[0][strt:end]),
                run_time=tracker.time_until_bookmark("r"),
            )

        with self.voiceover(
            """
            Next methods are to edge and to corner... like the name suggests <bookmark mark='s'/> 
            to edge method moves the object to the edge of the screen <bookmark mark='t'/> 
            ... It takes a one dimensional vector as an argument and moves the object in that direction ... <bookmark mark='u'/>
            """
        ) as tracker:

            code_str = "rectangle.animate.to_edge(LEFT)"
            strt, end = code_str.find("to_edge(LEFT)"), code_str.find(
                "to_edge(LEFT)"
            ) + len("to_edge(LEFT)")
            code2 = create_code_scene(code_str)
            code2.next_to(absolute_positioning, DOWN, buff=0.5)
            self.wait_until_bookmark("s")
            self.play(
                ReplacementTransform(code, code2),
                run_time=tracker.time_until_bookmark("t"),
            )

            code_txt_indicate = code2.code[0][strt:end]
            self.play(
                rect2.animate.to_edge(LEFT),
                Indicate(code_txt_indicate),
                run_time=tracker.time_until_bookmark("u"),
            )

        with self.voiceover(
            """
            to corner method ... requires a two dimentional vector as an argument ... <bookmark mark='v'/> 
            and moves the object in that direction ... <bookmark mark='w'/>
            """
        ) as tracker:
            code_str = "rectangle.animate.to_corner(UR)"
            strt, end = code_str.find("to_corner(UR)"), code_str.find(
                "to_corner(UR)"
            ) + len("to_corner(UR)")
            code3 = create_code_scene(code_str)
            code3.next_to(absolute_positioning, DOWN, buff=0.5)
            self.play(
                ReplacementTransform(code2, code3),
                run_time=tracker.time_until_bookmark("v"),
            )

            code_txt_indicate = code3.code[0][strt:end]
            self.play(
                rect2.animate.to_corner(UR),
                Indicate(code_txt_indicate),
                run_time=tracker.time_until_bookmark("w"),
            )

        self.play(Uncreate(absolute_positioning), Uncreate(code3))

        with self.voiceover(
            "Next up we have relative positioning ... Relative positioning ... like the name suggests ... move objects relative to one another ..."
        ):
            self.play(Create(relative_positioning2))
            self.play(relative_positioning2.animate.to_edge(UP))

        with self.voiceover(
            """
            The shift method moves the object relative to its current position ... In the current scene ... 
            the rectangle is in the <bookmark mark='x'/> 
            upper right corner <bookmark mark='y'/> 
            ... If I want to move it to the <bookmark mark='ae'/> 
            center of the screen ... I cannot use <bookmark mark='z'/>
            ... origin with shift method ... <bookmark mark='aa'/> 
            because it means shift to the origin or center of the rectangle and it is already there ... <bookmark mark='ab'/> 
            To move it to the center of the screen with shift method ... <bookmark mark='ac'/> 
            I need to use the relative position of the center ... <bookmark mark='ad'/>
            """
        ) as tracker:
            self.wait_until_bookmark("x")
            self.play(Indicate(rect2), run_time=tracker.time_until_bookmark("y"))

            d = Dot()
            origin_text = MathTex("Origin")
            origin_text.next_to(d, UP, buff=0.25)
            self.play(
                Create(VGroup(d, origin_text)),
                run_time=tracker.time_until_bookmark("ae"),
            )

            code_str = "rectangle.animate.shift(ORIGIN)"
            strt, end = code_str.find("shift(ORIGIN)"), code_str.find(
                "shift(ORIGIN)"
            ) + len("shift(ORIGIN)")
            code4 = create_code_scene(code_str)
            code4.next_to(relative_positioning2, DOWN, buff=0.5)
            self.play(
                Create(code4),
                run_time=tracker.time_until_bookmark("z"),
            )

            code_txt_indicate = code4.code[0][strt:end]
            self.play(
                rect2.animate.shift(ORIGIN),
                Indicate(code_txt_indicate),
                run_time=tracker.time_until_bookmark("aa"),
            )

            code_str = "rectangle.animate.shift(-1 * rectangle.get_center())"
            strt, end = code_str.find(
                "shift(-1 * rectangle.get_center())"
            ), code_str.find("shift(-1 * rectangle.get_center())") + len(
                "shift(-1 * rectangle.get_center())"
            )
            code5 = create_code_scene(code_str).scale(0.8)
            code5.next_to(relative_positioning2, DOWN, buff=0.5)
            self.wait_until_bookmark("ab")
            self.play(
                ReplacementTransform(code4, code5),
                run_time=tracker.time_until_bookmark("ac"),
            )

            code_txt_indicate = code5.code[0][strt:end]
            self.play(
                rect2.animate.shift(-1 * rect2.get_center()),
                Indicate(code_txt_indicate),
                run_time=tracker.time_until_bookmark("ad"),
            )

        self.play(Uncreate(origin_text), Uncreate(d))
        with self.voiceover(
            """
            Next method is ... next to method ... <bookmark mark='af'/>. 
            As the name suggests ... it moves the object next to another object ... <bookmark mark='ag'/> 
            The method takes two argument, first is the object, next to which you want to move your object ... <bookmark mark='ah'/> 
            next is which side or direction you want to place your object ... <bookmark mark='ai'/>
            """
        ) as tracker:

            code_str = "rectangle.animate.next_to(circle, UP)"
            strt, end = code_str.find("next_to(circle, UP)"), code_str.find(
                "next_to(circle, UP)"
            ) + len("next_to(circle, UP)")
            code6 = create_code_scene(code_str)
            code6.next_to(relative_positioning2, DOWN, buff=0.5)
            circle = Circle()
            circle.to_corner(DR)
            self.play(
                Create(circle),
                ReplacementTransform(code5, code6),
                run_time=tracker.time_until_bookmark("af"),
            )

            code_txt_indicate = code6.code[0][strt:end]
            self.play(
                rect2.animate.next_to(circle, UP),
                Indicate(code_txt_indicate),
                run_time=tracker.time_until_bookmark("ag"),
            )

            strt, end = code_str.find("circle"), code_str.find("circle") + len("circle")
            code_txt_indicate = code6.code[0][strt:end]
            self.play(
                Indicate(circle),
                Indicate(code_txt_indicate),
                run_time=tracker.time_until_bookmark("ah"),
            )

            code_str = "rectangle.animate.next_to(circle, LEFT)"
            code7 = create_code_scene(code_str)
            code7.next_to(relative_positioning2, DOWN, buff=0.5)
            self.play(
                ReplacementTransform(code6, code7),
            )

            strt, end = code_str.find("LEFT"), code_str.find("LEFT") + len("LEFT")
            code_txt_indicate = code7.code[0][strt:end]
            self.play(
                rect2.animate.next_to(circle, LEFT),
                Indicate(code_txt_indicate),
                run_time=tracker.time_until_bookmark("ai"),
            )

        with self.voiceover(
            """
            Next up ... we have align to method ...<bookmark mark='aj'/>
            Just like next to method, this method also takes two argument ... <bookmark mark='ak'/>
            first argument is the object to which you want to align your object ... <bookmark mark='al'/>
            and second argument is which side your want to align your object ... <bookmark mark='am'/>
            This method will align the circle to the upper side of the rectangle ... <bookmark mark='an'/>
            Here's another example ... <bookmark mark='ao'/>
            Using this method ... I can place circle inside each corner of rectangle ...
            """
        ) as tracker:

            code_str = "rectangle.animate.align_to(circle, UP)"
            code8 = create_code_scene(code_str)
            code8.next_to(relative_positioning2, DOWN, buff=0.5)
            self.play(
                ReplacementTransform(code7, code8),
                circle.animate.scale(0.2),
                run_time=tracker.time_until_bookmark("aj"),
            )

            self.wait_until_bookmark("ak")

            strt, end = code_str.find("circle"), code_str.find("circle") + len("circle")
            code_txt_indicate = code8.code[0][strt:end]
            self.play(
                Indicate(circle),
                Indicate(code_txt_indicate),
                run_time=tracker.time_until_bookmark("al"),
            )

            strt, end = code_str.find("UP"), code_str.find("UP") + len("UP")
            code_txt_indicate = code8.code[0][strt:end]
            dashed_line = DashedLine(
                rect2.get_corner(UL) + 1.5 * LEFT,
                rect2.get_corner(UR) + 1.5 * RIGHT,
                color=BLUE,
            )
            self.play(
                Indicate(dashed_line),
                Indicate(code_txt_indicate),
                run_time=tracker.time_until_bookmark("am"),
            )

            strt, end = code_str.find("align_to(circle, UP)"), code_str.find(
                "align_to(circle, UP)"
            ) + len("align_to(circle, UP)")
            code_txt_indicate = code8.code[0][strt:end]
            self.play(
                Indicate(code_txt_indicate),
                circle.animate.align_to(rect2, UP),
                run_time=tracker.time_until_bookmark("an"),
            )

            self.remove(dashed_line)

            self.wait_until_bookmark("ao")

            directions = [UR, DR, DL, UL]
            circles = [circle] + [circle.copy() for _ in range(3)]
            for circ, direction in zip(circles, directions):
                self.play(circ.animate.align_to(rect2, direction))

        self.play(*[FadeOut(mobj) for mobj in self.mobjects])

        with self.voiceover(
            """Thanks a lot for watching ... if you enjoyed the video ... please like and subscribe ...."""
        ):
            pass
        self.wait(5)
