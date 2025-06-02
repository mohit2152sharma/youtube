import { Code, lines, makeScene2D, Rect } from "@motion-canvas/2d";
import { addIntro } from "../../intros/tips";
import { all, createRef, DEFAULT, waitUntil } from "@motion-canvas/core";
import { DraculaColors, PythonCode, PythonHighlighter } from "../../../utils/defaults";

export default makeScene2D(function* (view) {
  view.fill(DraculaColors.background)

  yield* addIntro(view, 2, "f-strings")

  yield* waitUntil('start')

  // If you have a variable and you need to log it's value
  const code = createRef<Code>();
  const rect = createRef<Rect>();
  view.add(
    <Rect ref={rect} radius={12} padding={40} y={-300}>
      <PythonCode
        ref={code}
        code={`from datetime import datetime\ndt = datetime.now()`}
        fontSize={100}
        opacity={0}
        lineHeight={120}
        highlighter={PythonHighlighter}
      />
    </Rect>
  )

  yield* code().opacity(1,1)

  yield* waitUntil('dtformat')
  yield* all(
    code().code.append('\n\n# dd/mm/yyyy', 1),
    code().selection(lines(3), 1)
  )

  yield* waitUntil('normal')
  yield* all(
    code().code.append(`\n\nprint(\n\t\tf"Date is {dt.strftime('%d-%m-%Y')}\n)`, 1),
    code().selection(lines(5, 8), 1),
    code().fontSize(90, 1)
  )

  yield* waitUntil('highstrf')
  yield* code().selection(code().findAllRanges(/dt\.strftime\('%d-%m-%Y'\)/g), 1)

  yield* waitUntil('better')
  yield* all(
    code().code.append(
      `\n\nprint(\n\t\tf"Date is {dt:%d-%m-%Y}\n)`, 1
    ),
    code().selection(lines(9, 12), 1)
  )

  yield* waitUntil('highfstr')
  yield* code().selection(code().findAllRanges(/{dt:%d-%m-%Y}/g), 1)

  yield* waitUntil('reset')
  yield* code().selection(DEFAULT, 1)

  yield* waitUntil('end')
})


/*
 * Many times you have a datetime object that you need to format in 
 * a particular date style
 * Usually we would use strftime to convert the datetime object to that particular style
 * But if you only need to print the date, you can use the 
 * format style directly in the f string i.e. variable colon the style in which you need to print.
 * Thanks for watching, do remember to like and subscribe
 */
