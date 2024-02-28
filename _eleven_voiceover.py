import os
import sys
from pathlib import Path

from dotenv import find_dotenv, load_dotenv
from manim import logger
from manim_voiceover.helper import create_dotenv_file, remove_bookmarks

try:
    import elevenlabs
except ImportError:
    logger.error(
        "Missing packages. Run `pip install elevenlabs` to use ElevenLabsService."
    )

from manim_voiceover.services.base import SpeechService

load_dotenv(find_dotenv(usecwd=True))


def create_dotenv_elevenlabs():
    logger.info(
        "Check out https://docs.elevenlabs.io/api-reference/quick-start to learn how to create an account and get your subscription key."
    )
    if not create_dotenv_file(
        [
            "ELEVEN_API_KEY",
        ]
    ):
        raise Exception(
            "The environment variables ELEVENLABS_KEY is not set. Please set it or create a .env file with the variable."
        )
    logger.info("The .env file has been created. Please run Manim again.")
    sys.exit()


from elevenlabs import generate, save, set_api_key, voices

elevenlabs_key = os.environ["ELEVEN_API_KEY"]
set_api_key(elevenlabs_key)


class ElevenLabsService(SpeechService):
    """Speech service for Elevenlabs TTS API."""

    def __init__(self, model="eleven_monolingual_v1", voice="Daniel", **kwargs):
        SpeechService.__init__(self, **kwargs)
        self.model = model
        available_voices = voices()

        selected_voice = [v for v in available_voices if v.name == voice]

        if selected_voice:
            self.voice = selected_voice[0]
        else:
            f"Missing Voice : {voice} not found in Elevenlabs voices , defaulting to {selected_voice[0]}"
            self.voice = available_voices[0]

    def generate_from_text(
        self, text: str, cache_dir: str = None, path: str = None, **kwargs
    ) -> dict:
        if cache_dir is None:
            cache_dir = self.cache_dir

        input_text = remove_bookmarks(text)
        input_data = {"input_text": input_text, "service": "elevenlabs"}

        cached_result = self.get_cached_result(input_data, cache_dir)

        # if not config.disable_caching:
        if cached_result is not None:
            return cached_result

        if path is None:
            audio_path = self.get_audio_basename(input_data) + ".mp3"
        else:
            audio_path = path
        try:
            audio = generate(text=text, voice=self.voice, model=self.model)
            save(audio, str(Path(cache_dir) / audio_path))
        except Exception as e:
            logger.error(e)
            raise Exception("Failed to initialize ElevenLabs.")

        json_dict = {
            "input_text": text,
            "input_data": input_data,
            "original_audio": audio_path,
        }

        return json_dict


# from pprint import pprint
#
# v = voices()
# for i in v:
#     pprint(i.name)
