import diff_match_patch as dmp_module
from manim import *

config.background_color = "#191919"


def find_matching_code_spans(before: Code, after: Code):
    in_str = before.code_lines.lines_text.original_text
    out_str = after.code_lines.lines_text.original_text

    dmp = dmp_module.diff_match_patch()
    diffs = dmp.diff_main(in_str, out_str)
    dmp.diff_cleanupSemantic(diffs)

    in_pos = out_pos = 0

    matches = []
    deletions = []
    additions = []

    for op, diff in diffs:
        length = len(diff)
        if op == 0:  # Match
            in_span = (in_pos, length)
            out_span = (out_pos, length)
            matches.append((in_span, out_span))
            in_pos += length
            out_pos += length
        elif op == -1:  # Delete
            deletions.append((in_pos, length))
            in_pos += length
        elif op == 1:  # Add
            additions.append((out_pos, length))
            out_pos += length

    return matches, deletions, additions


def select_characters(code: Code, span):
    start, length = span

    if length == 0:
        return []

    end = start + length
    selected_chars = []

    current_index = 0
    for line_number, line in enumerate(code.code_lines):
        pos_of_line_start = current_index
        pos_of_line_end = current_index + len(line) + 1

        span_start = max(start, pos_of_line_start)
        span_end = min(end, pos_of_line_end)

        if span_start < span_end:
            line_relative_start = span_start - pos_of_line_start
            line_relative_end = span_end - pos_of_line_start

            selected_chars.append(line[line_relative_start:line_relative_end])

        current_index = pos_of_line_end

        if current_index > end:
            break

    return selected_chars


class CodeTransform(AnimationGroup):
    def __init__(
        self,
        before: Code,
        after: Code,
        **kwargs,
    ):
        matching_pairs, deletions, additions = find_matching_code_spans(before, after)
        print(f"{matching_pairs=}")
        print(f"{deletions=}")
        print(f"{additions=}")

        transform_pairs = [
            (select_characters(before, in_match), select_characters(after, out_match))
            for in_match, out_match in matching_pairs
        ]

        delete_chars = [select_characters(before, deletion) for deletion in deletions]
        add_chars = [select_characters(after, addition) for addition in additions]

        super().__init__(
            LaggedStart(
                # FadeOut(*[char for chars in delete_chars for char in chars]),
                LaggedStart(
                    *[
                        Transform(before_match, after_match)
                        for before_chars, after_chars in transform_pairs
                        for before_match, after_match in zip(before_chars, after_chars)
                    ]
                ),
                FadeIn(*[char for chars in add_chars for char in chars]),
            ),
            group=None,
            run_time=None,
            rate_func=linear,
            lag_ratio=0.0,
            **kwargs,
        )
