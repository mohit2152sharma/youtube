from manim import *
from manim_voiceover import VoiceoverScene

from _eleven_voiceover import ElevenLabsService
from _utils import create_code_scene

manager = ElevenLabsService(voice="Markus - Mature and Chill")
dev = ElevenLabsService(voice="Ryan Kurk")


class FindCommand(VoiceoverScene):
    def construct(self):
        self.set_speech_service(manager)

        with self.voiceover(
            "Hey!! I need your help. I have couple of images that are taking a lot of space on my PC. I need to delete them. How can I do that?"
        ):
            grumpy1 = ImageMobject("./find-cmnd/grump1.jpeg")
            self.add(grumpy1)

        self.set_speech_service(dev)
        self.remove(grumpy1)
        with self.voiceover(
            "Sure... that should be simple. - I can help you with that"
        ):
            dog1 = ImageMobject("./find-cmnd/dog1.jpeg")
            self.add(dog1)

        self.remove(dog1)
        with self.voiceover(
            "here!... you can use this command. This looks for all the files with png extension and deletes them."
        ):
            code = create_code_scene("ls -R | grep '*.png$' | xargs rm", "bash")
            self.add(code)

        self.set_speech_service(manager)
        self.remove(code)
        with self.voiceover(
            "Nice!!! but wait. This will delete all the png files in the current and it's subdirectories. I only want to delete in specific directory"
        ):
            cat2 = ImageMobject("./find-cmnd/cat2.jpeg")
            self.add(cat2)

        self.remove(cat2)
        self.set_speech_service(dev)
        with self.voiceover("hmm!... Okay, that should be simple as well."):
            dog2 = ImageMobject("./find-cmnd/dog2.jpeg")
            self.add(dog2)

        self.remove(dog2)
        with self.voiceover("Here... you can use this command"):
            code = create_code_scene(
                "ls -R dir1 dir2 | grep '*.png$' | xargs rm", "bash"
            )
            self.add(code)

        self.set_speech_service(manager)
        self.remove(code)
        with self.voiceover(
            "Hmmm....Sorry. I forgot to mention that I also have images with file type jpeg and jpg"
        ):
            cat3 = ImageMobject("./find-cmnd/cat3.jpeg")
            self.add(cat3)

        self.remove(cat3)
        self.set_speech_service(dev)
        with self.voiceover(
            "This is getting complicated. - I think with find command I can do that."
        ):
            dog3 = ImageMobject("./find-cmnd/dog3.jpeg")
            self.add(dog3)

        self.remove(dog3)
        with self.voiceover("This command should work."):
            code = create_code_scene(
                """
                find dir1 dir2 -type f \( -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" \) -exec rm {} \;
                # or
                # find dir1 dir2 -type f \( -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" \) -exec rm {} +
                """,
                "bash",
            ).scale(0.7)
            self.add(code)

        with self.voiceover(
            "So what this command does is - It will search in dir1 and dir2 for files. This indicated by type f option. -"
            "Then I specify the names of the file using name option. - I am using globbing to match all files, which have "
            "png, jpg or jpeg extension. - Those three conditions are clubbed together using or operator, indicated by o option. -"
            "Then, I execute the remove command for each matched file. - This is specified by exec rm curly brackets backward slash semicolon. -"
            "Sometimes... you may also see the second command. The only difference is how remove command is executed."
            "The curly braces are a placeholder for each matched file and plus sign indicates that add each matched file to the remove command"
            ". - Something like remove file1 file2 file3 and so on."
        ):
            pass

        self.remove(code)

        self.set_speech_service(manager)
        with self.voiceover("Thanks a lot...you are a life saver"):
            cat4 = ImageMobject("./find-cmnd/cat4.jpeg")
            self.add(cat4)

        self.set_speech_service(dev)
        self.remove(cat4)
        with self.voiceover(
            "No problem...happy to help. Just be sure to like and subscribe"
        ):
            dog4 = ImageMobject("./find-cmnd/dog4.jpeg")
            self.add(dog4)
        self.wait(3)
