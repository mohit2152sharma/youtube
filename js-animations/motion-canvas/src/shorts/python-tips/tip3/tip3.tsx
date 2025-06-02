import { Code, lines, makeScene2D, Rect } from "@motion-canvas/2d";
import { addIntro } from "../../intros/tips";
import { all, createRef, DEFAULT, waitUntil } from "@motion-canvas/core";
import { DraculaColors, PythonCode, PythonHighlighter } from "../../../utils/defaults";

export default makeScene2D(function* (view) {
  view.fill(DraculaColors.background)

  yield* addIntro(view, 3, "f-strings")

  yield* waitUntil('start')

  // If you have a variable and you need to log it's value
  const code = createRef<Code>();
  const rect = createRef<Rect>();
  view.add(
    <Rect ref={rect} radius={12} padding={40} y={-300}>
      <PythonCode
        ref={code}
        code={`print(f"Total: {a+b}, A%: {a/a+b})`}
        fontSize={100}
        opacity={0}
        lineHeight={120}
        highlighter={PythonHighlighter}
      />
    </Rect>
  )

  yield* code().opacity(1,1)


  yield* waitUntil('same')
  yield* all(
    code().selection(code().findAllRanges(/a\+b/g), 1)
  )

  yield* waitUntil('walrus')
  yield* all(
    code().code.append('\n\n# Walrus operator', 1),
    code().selection(lines(2), 1)
  )

  yield* waitUntil('walrusexp')
  yield* all(
    code().code.append('\n\nprint(\n\tf"Total: {total:=a+b}, A%:{a/total}\n)', 1),
    code().selection(lines(4, 7), 1),
    code().fontSize(90, 1)
  )

  yield* waitUntil('highlight')
  yield* code().selection(code().findAllRanges(/:=/g), 1)

  yield* waitUntil('calc')
  yield* code().selection(code().findAllRanges(/total:=a\+b/g), 1)

  yield* waitUntil('reuse')
  yield* code().selection(code().findAllRanges(/a\/total/g), 1)
  
  yield* waitUntil('reset')
  yield* code().selection(DEFAULT, 1)

  yield* waitUntil('end')
})


/*
 * Suppose you have the f string, in this you are computing the same thing twice
 * we can avoid that using walrus operator
 * Use the walrus operator to calculate the total 
 * and we can reuse it in the same line
 * Thanks for watching, like and subscribe for more tips
 */
