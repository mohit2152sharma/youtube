
import { Code,  lines, makeScene2D, Rect } from "@motion-canvas/2d";
import { all, createRef as createSignalRef, DEFAULT, waitUntil } from "@motion-canvas/core";
import { DraculaColors, PythonCode, PythonHighlighter } from '../../utils/defaults';
import { addIntro } from "../intros/noobvspro";

export default makeScene2D(function* (view) {
  view.fill(DraculaColors.background)

  yield* addIntro(view, 'a, b = (1, 2)')

  const forLoopCode = createSignalRef<Code>();
  const forLoopRect = createSignalRef<Rect>();
  view.add(
    <Rect ref={forLoopRect} radius={12} padding={40} y={-300}>
      <PythonCode
        ref={forLoopCode}
        code={`x = (1, 2)`}
        fontSize={120}
        opacity={0}
        lineHeight={150}
        highlighter={PythonHighlighter}
      />
    </Rect>
  );

  // Step 1: create a list with repeated elements
  yield* waitUntil('start')
  yield* forLoopCode().opacity(1, 1)

  yield* waitUntil('highlight-unique')
  yield* forLoopCode().selection(forLoopCode().findAllRanges(/1, 2/g), 1)
  

  yield* waitUntil('variables')
  yield* all(
   forLoopCode().code.append('\n\na\nb', 1),
   forLoopCode().selection(lines(2,4), 1)
  )

  yield* waitUntil('index')
  yield* all(
    forLoopCode().code('x = (1, 2)\n\na = x[0]\nb = x[1]', 1),
  )

  yield* waitUntil('unpacking')
  yield* all(
    forLoopCode().code.append('\n\n# Tuple unpacking', 1),
    forLoopCode().selection(lines(5), 1)
  )

  yield* waitUntil('unpacktuple')
  yield* all(
    forLoopCode().code.append('\na, b = x', 1),
    forLoopCode().selection(lines(6), 1)
  )

  yield* waitUntil('workswithother')
  yield* all(
    forLoopCode().code.append('\n\n#Works with any iterable', 1),
    forLoopCode().selection(lines(8), 1)
  )

  yield* waitUntil('example')
  yield* all(
    forLoopCode().code.append('\ni, j = [1, 2]\ny, z = "ab"\n# y will be a\n# z will be b', 1),
    forLoopCode().selection(lines(9, 13), 1)
  )

  yield* waitUntil('reset')
  yield* forLoopCode().selection(DEFAULT, 1)

  yield* waitUntil('end')
})


/*
 * Many times you have a tuple and you need to extract elements from it
 * You can do simple way, create two elements a and b and use indexes to extract the elements
 * But there is a better way with tuple unpacking
 * you can extract elements into separate variables in single line.
 * Here's the bonus part, it works with not just tuples but with all iterables like list and string
 * thanks for watching do remember to like and subscribe
 */
