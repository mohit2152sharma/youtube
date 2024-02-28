from manim_voiceover import VoiceoverScene

from _eleven_voiceover import ElevenLabsService


class TestScene(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            ElevenLabsService(
                model="eleven_monolingual_v1", voice="Markus - Mature and Chill"
            )
        )

        with self.voiceover("This is a test voice"):
            pass
