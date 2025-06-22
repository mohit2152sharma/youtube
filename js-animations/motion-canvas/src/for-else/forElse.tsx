import { Code, Layout, lines, makeScene2D, Rect, Txt } from "@motion-canvas/2d";
import { DraculaColors, PythonCode, PythonHighlighter } from "../utils/defaults";
import { all, chain, createRef, DEFAULT, easeInCubic, easeInOutCubic, loop, range, sequence, waitFor, waitUntil } from "@motion-canvas/core";
import { highlight, reset } from "../utils/funcs";

const forLoop = `\n
for i in range(20):
    print(i)`

const elseClause = `\nelse:
    print("Finished printing the loop")`

const whileClause = `\n
while i <= 20:
    print(i)
else:
    print("Finished printing while loop")`


const broke = `\n
for user_id in user_database:
    if user_id == "user1234":
        print(f"User found")
        generate_recommendation(user_id)
        break
else:
    print("User not present in database")`


const returned = `\n
def generate_user_recommendation(id): 
    for user_id in user_database:
        if user_id == id: 
            return generate_recommendation(id)
    else:
        print(f"User {id=} not present in database")`


const factor = `\n
def find_prime_factor(n):
    """Find the first prime factor of a number"""
    print(f"Finding prime factors of {n}:")
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f"Found factor: {i}")
            return i
    else:
        # This executes only if the loop completed without breaking
        print(f"{n} is prime!")
        return n`


export default makeScene2D(function* (view) {
  
  view.fill(DraculaColors.background)


  const code = createRef<Code>()
  const codeRect = createRef<Rect>();
  const layout = createRef<Layout>();
  const codeResult = createRef<Code>();

  view.add(
    <Layout 
      ref={layout}
      direction={"column"}
      alignItems={"center"}
      justifyContent={"center"}
      width={view.width}
      height={view.height}
      gap={60}
  >
    <Rect
      ref={codeRect}
      radius={16}
      padding={40}
      width={view.width() -400}
      height={view.height() - 500}
      layout={true}
      alignItems={"center"}
      justifyContent={"center"}
      direction={"column"}
      >
        <PythonCode
        ref={code}
        highlighter={PythonHighlighter}
        fontSize={100}
        fontFamily="JetBrains Mono"
        />
        <PythonCode
        ref={codeResult}
        highlighter={PythonHighlighter}
        fontSize={100}
        fontFamily="JetBrains Mono"
        alignSelf={"start"}
        marginLeft={600}
        />
    </Rect>
  </Layout>
  )



  yield* waitUntil('show-for')
  yield* code().code.append(forLoop, 1)

  yield* waitUntil('show-else')
  yield* code().code.append(elseClause, 1)

  yield* waitUntil('loop-start')
  for (let i = 0; i<=20; i++) {

    if (i < 5) {
      yield* chain( 
        ...[
          code().selection(lines(2), 0.1, easeInOutCubic),
          all(
            code().selection(lines(3), 0.1, easeInOutCubic), 
            codeResult().code.append(`\n# ${i}`, 0.1)
          )
        ]
      )
    } else {
        yield* chain( 
        ...[
          code().selection(lines(2), 0.1, easeInOutCubic),
          all(
            code().selection(lines(3), 0.1, easeInOutCubic), 
            codeResult().code.append(`\n# ${i}`, 0.1),
            codeResult().code.remove(lines(1), 0.1)
          )
        ]
      )
    }
  }


  yield* waitUntil('loop-end')
  yield* all(
    code().selection(lines(5,7), 1, easeInOutCubic), 
    codeResult().code.append('\n# Finished printing the loop', 1), 
    codeResult().code.remove(lines(1), 1)
  )

  yield* waitUntil('reset')
  yield* all(
    code().selection(DEFAULT, 1, easeInOutCubic),
    codeResult().opacity(0, 1, easeInOutCubic)
  )
  codeResult().remove()

  yield* waitUntil('break')
  yield* code().code(broke, 1, easeInOutCubic)

  yield* waitUntil('break-higlight')
  yield* code().selection(code().findAllRanges(/break/g), 1, easeInOutCubic)

  yield* waitUntil('return')
  yield* code().code(returned, 1, easeInOutCubic)

  yield* waitUntil('return-higlight')
  yield* code().selection(code().findAllRanges(/return generate_recommendation\(id\)/g), 1, easeInOutCubic)

  yield* waitUntil('while-clause')
  yield* all(
    code().selection(DEFAULT, 0.1),
    code().code(whileClause, 1, easeInOutCubic)
  )

  yield* waitUntil('remove-code')
  yield* code().opacity(0, 1, easeInOutCubic)

  code().remove()
  codeRect().remove()

  const title = createRef<Txt>()

  layout().add(
    <Txt 
      ref={title}
      fontSize={240}
      opacity={0}
      text={"When should you use it?"}
      fill="white"
      fontFamily={"Arial Black"}
    />
  )

  yield* waitUntil('show-title')
  yield* title().opacity(1, 1, easeInOutCubic)

  yield* waitUntil('move-title')
  yield* all(
    title().fontSize(160, 1, easeInOutCubic), 
    title().position.y(-(view.height() / 2 - 200), 1, easeInOutCubic)
  )

  const exmple = createRef<Code>();

  layout().add(
    <PythonCode
    ref={exmple}
    highlighter={PythonHighlighter}
    fontSize={80}
    fontFamily="JetBrains Mono"
    />
  )

  yield* waitUntil('show-example')
  yield* exmple().code.append(factor, 1)

  yield* waitUntil('find-prime')
  yield* highlight(exmple, exmple().findAllRanges(/find_prime_factor/g))

  yield* waitUntil('call-n')
  yield* highlight(exmple, exmple().findAllRanges(/\(n\)/g))


  yield* waitUntil('loop-higlight')
  for(let i = 0; i < 3; i++) {
    yield* chain(
      ...range(4).map((j) => exmple().selection(lines(j+6), 0.4, easeInOutCubic))
    )
  }

  yield* waitUntil('loop-clause')
  yield* sequence(1, 
    ...range(4).map((j) => exmple().selection(lines(10+j), 0.4, easeInCubic))
  )

  yield* waitUntil('exmple-reset')
  yield* reset(exmple)

  yield* waitUntil('video-end')
})



