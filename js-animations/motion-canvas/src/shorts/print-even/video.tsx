import { Code,  lines, makeScene2D, Rect } from "@motion-canvas/2d";
import { all, createRef as createSignalRef, DEFAULT, waitUntil } from "@motion-canvas/core";
import { DraculaColors, PythonCode, PythonHighlighter } from '../../utils/defaults';
import { addIntro } from "../intros/noobvspro";

export default makeScene2D(function* (view) {
  view.fill(DraculaColors.background)

  yield* addIntro(view, 'even or odd')

  const forLoopCode = createSignalRef<Code>();
  const forLoopRect = createSignalRef<Rect>();
  view.add(
    <Rect ref={forLoopRect} radius={12} padding={40} y={-300}>
      <PythonCode
        ref={forLoopCode}
        code={`def even_or_odd(no: int):`}
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

  yield* waitUntil('highlight-func')
  yield* all(
    forLoopCode().code.append('\n\t\tif no % 2 == 0:\n\t\t\t\tprint("even")\n\t\telse:\n\t\t\t\tprint("odd")', 1),
    forLoopCode().selection(lines(1, 5) ,1)
  )
  

  yield* waitUntil('pro')
  yield* all(
   forLoopCode().code.append('\n\ndef even_or_odd(no: int):', 1),
   forLoopCode().selection(lines(6), 1)
  )

  yield* waitUntil('pro-sol')
  yield* all(
   forLoopCode().code.append('\n\t\ti = ("even", "odd")\n\t\tprint(i[no % 2])', 1),
   forLoopCode().selection(lines(7, 9), 1)
  )

  yield* waitUntil('tuple')
  yield* forLoopCode().selection(forLoopCode().findAllRanges(/\("even", "odd"\)/g), 1)

  yield* waitUntil("even")
  yield* forLoopCode().selection(forLoopCode().findLastRange(/"even"/g), 1)

  yield* waitUntil("odd")
  yield* forLoopCode().selection(forLoopCode().findLastRange(/"odd"/g), 1)

  yield* waitUntil("modulo")
  yield* forLoopCode().selection(forLoopCode().findAllRanges(/\[no % 2\]/g), 1)

  yield* waitUntil('fullsol')
  yield* forLoopCode().selection(lines(7, 9), 1)

  yield* waitUntil('reset')
  yield* forLoopCode().selection(DEFAULT, 1)

  yield* waitUntil('end')
})

/*
 * suppose you are writing a function which prints even if the number is even otherwsie it prints odd
 * Simple way you can achieve this is via if else clause
 * Another way to do this is, create a tuple with even at zero index and odd at 1 index
 * and use modulo operator to index this tuple, when the number is even modulo operator will give zero and since index
 * 0 is even, even will be printed
 * likewise when the number is odd, the modulo operator will give one and odd will be printed
 * thanks for watching, do remember to like and subscribe
 */
