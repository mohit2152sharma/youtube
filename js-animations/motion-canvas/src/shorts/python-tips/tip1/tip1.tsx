import { Code, lines, makeScene2D, Rect } from "@motion-canvas/2d";
import { addIntro } from "../../intros/tips";
import { all, createRef, createSignal, DEFAULT, waitUntil } from "@motion-canvas/core";
import { DraculaColors, PythonCode, PythonHighlighter } from "../../../utils/defaults";

export default makeScene2D(function* (view) {
  view.fill(DraculaColors.background)

  yield* addIntro(view, 1, "f-strings")

  yield* waitUntil('start')

  // If you have a variable and you need to log it's value
  const code = createRef<Code>();
  const rect = createRef<Rect>();
  view.add(
    <Rect ref={rect} radius={12} padding={40} y={-300}>
      <PythonCode
        ref={code}
        code={`variable = 42`}
        fontSize={130}
        opacity={0}
        lineHeight={120}
        highlighter={PythonHighlighter}
      />
    </Rect>
  )

  yield* code().opacity(1,1)

  yield* waitUntil('print')
  yield* all(
    code().code.append('\n\nprint(f"value={value})', 1),
    code().selection(lines(2), 1)
  )

  yield* waitUntil('showprint')
  yield* all(
    code().code.append('\n\n# value=42', 1),
    code().selection(lines(2, 4), 1)
  )

  yield* waitUntil('better')
  yield* all(
    code().code.append('\n\n\n\n# For python>3.8', 1),
    code().selection(lines(8), 1)
  )


  yield* waitUntil('showbetter')
  yield* all(
    code().code.append('\n\nprint(f"{value=})', 1),
    code().selection(lines(8, 10), 1)
  )

  yield* waitUntil('showprint2')
  yield* all(
    code().code.append('\n\n# value=42', 1),
    code().selection(lines(9, 12), 1)
  )

  yield* waitUntil('reset')
  yield* code().selection(DEFAULT, 1)

  yield* waitUntil('end')
})


/*
 * Many times for debugging purposes you need to print a variable
 * For this instead of writing the print statement this way
 * we can use the debug syntax to print both the expression and value
 * Thanks for watching, do remember to like and subscribe for more tips
 */
