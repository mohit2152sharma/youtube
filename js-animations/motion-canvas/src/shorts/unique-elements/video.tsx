import { Code,  lines, makeScene2D, Rect } from "@motion-canvas/2d";
import { all, createRef as createSignalRef, DEFAULT, waitUntil } from "@motion-canvas/core";
import { DraculaColors, PythonCode, PythonHighlighter } from '../../utils/defaults';
import { addIntro } from "../intros/noobvspro";

export default makeScene2D(function* (view) {
  view.fill(DraculaColors.background)

  yield* addIntro(view, 'list[] or set{}')

  const forLoopCode = createSignalRef<Code>();
  const forLoopRect = createSignalRef<Rect>();
  view.add(
    <Rect ref={forLoopRect} radius={12} padding={40} y={-300}>
      <PythonCode
        ref={forLoopCode}
        code={`original_list = [
  1, 2, 2, 3, 4, 4, 5
]`}
        fontSize={90}
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
  yield* forLoopCode().selection([
    [[1, 2], [1,4]],
    [[1, 5], [1,7]],
    [[1, 11], [1,13]],
    [[1, 14], [1,16]],
    [[1, 20], [1, 21]],
  ], 1)
  

  yield* waitUntil('result-list')
  yield* all(
   forLoopCode().code.append('\nresult = []', 1),
   forLoopCode().selection(lines(3), 1)
  )

  yield* waitUntil('forloop')
  yield* all(
    forLoopCode().code.append('\nfor element in original_list:', 1),
    forLoopCode().selection(lines(4), 1)
  )

  yield* waitUntil('ifcondition')
  yield* all(
  forLoopCode().code.append('\n\t\tif element not in result:', 1),
  forLoopCode().selection(lines(5), 1)
  )

  yield* waitUntil('append')
  yield* all(
  forLoopCode().code.append('\n\t\t\t\tresult.append(element)', 1),
  forLoopCode().selection(lines(6), 1)
  )

  yield* waitUntil('showresult')
  yield* all(
    forLoopCode().code.append('\n\nprint(result)\n# [1, 2, 3, 4, 5]', 1),
    forLoopCode().selection(lines(7,9), 1)
  )

  yield* waitUntil('set')
  yield* all(
    forLoopCode().code.append('\n\n\n\n#Set: collection of unique,\n# hashable elements', 1),
    forLoopCode().selection(lines(13, 15), 1)
  )

  yield* waitUntil('setresult')
  yield* all(
    forLoopCode().code.append('\nresult2 = list(set(original_list))', 1),
    forLoopCode().selection(lines(15), 1)
  )

  yield* waitUntil('highlightset')
  yield* forLoopCode().selection(forLoopCode().findAllRanges(/set\(original_list\)/g), 1)

  yield* waitUntil('highlightlist')
  yield* forLoopCode().selection(forLoopCode().findAllRanges(/list\(.*/g), 1)

  yield* waitUntil('showresult2')
  yield* all(
    forLoopCode().code.append('\nprint(result2)\n# [1, 2, 3, 4, 5]', 1),
    forLoopCode().selection(lines(16, 19), 1)
  )

  yield* waitUntil('reset')
  yield* forLoopCode().selection(DEFAULT, 1)

  yield* waitUntil('end')
})

/*
 * Suppose you have a list and you need to find the unique elements in this list
 * naive approach is to create a new list, 
 * then create a for loop and iterate over each element, 
 * if the element is in the new list, skip, otherwise append to the new list, like in the case of 2
 * the first 2 will be added to the new list, and for the second 2 it will skip because it's already in the list
 * There is a better, shorter way to do the same using sets. Set is a data structure which contains unique hashable elements
 * we pass the original list to the set, which gives us a set of unique elements and then we pass it back to a list constructor
 * which gives us our result
 * thanks for watching do remember to like and subscribe
 */
