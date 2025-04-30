from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.elevenlabs import ElevenLabsService


class TupleComma(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            ElevenLabsService(model="eleven_monolingual_v1", voice="Ryan Kurk")
        )

        code_text = """\
        tupl = ("gin", "tonic", "scotch")
        """
        code = Code(
            code=code_text,
            language="python",
            line_spacing=1.15,
            insert_line_no=False,
            background="window",
            font="Hack Nerd Font Mono",
        )

        self.play(Write(code))
        self.wait(5)
