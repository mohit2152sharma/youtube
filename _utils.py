import pygments.styles as code_styles
from manim import Code


def create_code_scene(code: str, language: str = "python"):
    code_style = code_styles.get_style_by_name("monokai")
    return Code(
        code=code,
        language=language,
        line_spacing=1.15,
        insert_line_no=False,
        background="window",
        font="Hack Nerd Font Mono",
        style=code_style,
    )
