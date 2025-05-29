import { Code, Img, Layout, lines, makeScene2D, Rect, Txt } from "@motion-canvas/2d";
import { all, chain, createRef, DEFAULT, delay, easeInOutCubic, easeOutCubic, finishScene, Origin, sequence, useDuration, useLogger, waitFor, waitUntil } from "@motion-canvas/core";
import { PythonCode, PythonHighlighter } from "../utils/defaults";

// Dracula theme colors
const DraculaColors = {
  background: '#282a36',
  currentLine: '#44475a',
  foreground: '#f8f8f2',
  comment: '#6272a4',
  cyan: '#8be9fd',
  green: '#50fa7b',
  orange: '#ffb86c',
  pink: '#ff79c6',
  purple: '#bd93f9',
  red: '#ff5555',
  yellow: '#f1fa8c'
};

const CodeSnippets = {
  call: `\
  def __call__(self):
    ...`,
  class: `\
class MyClass:\n\n`

}

export default makeScene2D(function* (view) {
  // Set Dracula background
  view.fill(DraculaColors.background);

  const codeRect = createRef<Rect>();
  const code = createRef<Code>();
  const whatBox = createRef<Rect>();
  const howBox = createRef<Rect>();
  const whenBox = createRef<Rect>();
  const whatText = createRef<Txt>();
  const howText = createRef<Txt>();
  const whenText = createRef<Txt>();
  const layout = createRef<Layout>();

  view.add(
    <Layout justifyContent="center" ref={layout} direction="column" alignItems="center" gap={200} width={view.width} height={view.height}>
      <Rect
        radius={12}
        padding={40}
        ref={codeRect}
      >
        <PythonCode
          ref={code}
          highlighter={PythonHighlighter}
          fontSize={100}
          fill={DraculaColors.foreground}
          fontFamily="JetBrains Mono"
        />
      </Rect>

      <Layout direction="row" gap={80} alignItems="center">
        <Rect
          ref={whatBox}
          width={400}
          height={200}
          fill={DraculaColors.currentLine}
          radius={12}
          opacity={0}
          alignItems="center"
          justifyContent="center"
          x={-view.width() / 4 }
          y={view.height() / 3}
        >
          <Txt
            ref={whatText}
            text="What?"
            fontSize={100}
            fill={DraculaColors.cyan}
            fontFamily="JetBrains Mono"
            fontWeight={600}
          />
        </Rect>

        <Rect
          ref={howBox}
          width={400}
          height={200}
          fill={DraculaColors.currentLine}
          radius={12}
          opacity={0}
          alignItems="center"
          justifyContent="center"
          x={Origin.Middle}
          y={view.height() / 3}
        >
          <Txt
            ref={howText}
            text="How?"
            fontSize={100}
            fill={DraculaColors.green}
            fontFamily="JetBrains Mono"
            fontWeight={600}
          />
        </Rect>

        <Rect
          ref={whenBox}
          width={400}
          height={200}
          fill={DraculaColors.currentLine}
          radius={12}
          opacity={0}
          alignItems="center"
          justifyContent="center"
          x={view.width() / 4}
          y={view.height() / 3}
        >
          <Txt
            ref={whenText}
            text="When?"
            fontSize={100}
            fill={DraculaColors.orange}
            fontFamily="JetBrains Mono"
            fontWeight={600}
          />
        </Rect>
      </Layout>
    </Layout>
  );

  // Animation sequence
  yield* code().code.append(CodeSnippets.call, useDuration('call'));
  yield* waitUntil('classes')
  yield* code().code.prepend(CodeSnippets.class, 1)


  yield* waitUntil('what')
  yield* whatBox().opacity(1, 1);

  yield* waitUntil('how')
  yield* howBox().opacity(1, 1);

  yield* waitUntil('when')
  yield* whenBox().opacity(1, 1);

  const disappear = [whenBox, howBox, code]
  yield* sequence(0.1, ...disappear.map(box => box().opacity(0, 0.5)))


  for(const el of disappear){
    el().remove()
  }
  
  const duration = useDuration('movewhat')
  yield* all(
   whatBox().position([-view.width()/2 + 100, -view.height()/2 + 100 ], duration, easeInOutCubic),
   whatBox().offset(-1, 0.3),
    delay(0.1, whatBox().width(view.width() - 200, duration)),
  whatBox().height(400, duration),
  whatText().fontSize(200, duration),
  )

  // second slide
  const slide2layout = createRef<Layout>();
  const textBoxLayout = createRef<Layout>();
  const textBox = createRef<Rect>();
  const contentText = createRef<Txt>();
  const methodRect = createRef<Rect>();
  const methodExp = createRef<Code>();
  const callRect = createRef<Rect>();
  const callExp = createRef<Code>();
  const imageRef = createRef<Img>();

  view.add(
    <Layout ref={slide2layout} y={500} padding={40} justifyContent="start" alignItems="stretch" direction="column" layout width={view.width} height={view.height}>
      <Layout ref={textBoxLayout} direction="column">
        <Rect ref={textBox} margin={30} padding={50} opacity={0} >
          <Txt
            ref={contentText}
            fontSize={100}
            text="It makes an instance callable"
            fill={DraculaColors.foreground}
            fontFamily="JetBrains Mono">
          </Txt>
        </Rect>
      </Layout>
        <>
      <Layout layout height={view.height() - 400 - 100 - 260} gap={40} direction="row" alignItems="center" justifyContent="space-between">
        <Rect ref={methodRect}  padding={50} margin={[0, 40, 40, 40]} y={-50}> <PythonCode
          ref={methodExp}
          code="instance.method(*args)"
          fontSize={100}
          opacity={0}
          fill={DraculaColors.currentLine}>
        </PythonCode>
        </Rect>
        <Img ref={imageRef} opacity={0} src="index-finger.png" height={200} width={200} rotation={-180} />
        <Rect grow={1} ref={callRect} padding={50} margin={[20, 40, 40, 40]}   >
          <PythonCode
            ref={callExp}
            code="instance(*args)"
            opacity={0}
            fontSize={100}
            fill={DraculaColors.currentLine}>
          </PythonCode>
        </Rect>
      </Layout>
        </>
    </Layout>
  )

  // yield* headingBox().opacity(1, 5)
  yield* waitUntil('slide1-subtitle')
  yield* textBox().opacity(1, 1)

  yield* waitUntil('method-call')
  yield* all(
  methodExp().opacity(1, 1),
  imageRef().opacity(1, 1)
  )

  yield* waitUntil('instance-call')
  yield* all(
    imageRef().rotation(0, 1),
    callExp().opacity(1, 1)
  )

  yield* waitUntil('how-slide')
  yield* all(
    whatText().text('How?', 1, easeInOutCubic),
    textBox().opacity(0,1,easeInOutCubic)
  )

  // yield* all(
    // methodRect().opacity(0, 1),
    // callExp().code(`class Instance:\n\tdef __init__(self): ...\n\n\tdef __call__(self, *args):\n\t\tdo_something(*args)\n\ninstance=Instance()\ninstance('hello')`, 1),
  // )


  yield* waitUntil('show-how')
  yield* all(
    callExp().code(`class Instance:\n\tdef __init__(self): ...\n\n\tdef __call__(self, *args):\n\t\tdo_something(*args)\n\ninstance=Instance()\ninstance('hello')`, 1),
  methodExp().fontSize(1,1),
  callRect().grow(10, 1),
  methodRect().grow(0, 1)
  )

  yield* waitUntil('show-call')
  yield* all(
    callExp().selection(lines(3,4), 1),
    imageRef().rotation(-45, 1),
  )

  // yield* callRect().parent().position.x(-100, 1)
  // yield* callExp().position.x(-100, 1)
  yield* waitUntil('when-slide')
  yield* all(
    whatText().text("When?", 1),
    imageRef().opacity(0,1),
    callExp().opacity(0,1)
  )

  yield* waitUntil('stateful')
  yield* all(
    textBox().opacity(1,1),
    contentText().text('Stateful functions', 1)
  )



  yield* waitUntil('ex1')
  yield* all(
    callExp().opacity(1,1),
  callExp().code(`class Counter:
    def __init__(self):
        self.count = 0
    
    def __call__(self):
        self.count += 1
        return self.count

counter = Counter()
print(counter())  # 1
print(counter())  # 2`, 1),
  callExp().fontSize(80, 1),
  callExp().selection(DEFAULT, 1)
  )

  yield* waitUntil('h1')
  yield* callExp().selection(lines(8), 0.4, easeInOutCubic)

  yield* waitUntil('h2')
  yield* callExp().selection(lines(2), 0.4, easeInOutCubic)

  yield* waitUntil('h3')
  yield* callExp().selection(lines(9), 0.4, easeInOutCubic)

  yield* waitUntil('h4')
  yield* callExp().selection(lines(5,6), 0.5, easeInOutCubic)

  yield* waitUntil('h5')
  yield* callExp().selection(lines(9,10), 0.5, easeInOutCubic)

  yield* waitUntil('h-reset' )
  yield* callExp().selection(DEFAULT,1, easeInOutCubic)


  yield* waitUntil('example2')
  yield* contentText().text('Making instances behave like functions', 1, easeInOutCubic)

  yield* waitUntil('example2-code')
  yield* callExp().code(`class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, value):
        return value * self.factor

# Usage
double = Multiplier(2)
triple = Multiplier(3)
doubled = double(5)  # Returns 10
tripled = tripl(5) # Returns 15`, 1)


  yield* waitUntil('ex2-h1')
  yield* callExp().selection(lines(0, 6), 0.4, easeInOutCubic)

  yield* waitUntil('ex2-h2')
  yield* callExp().selection(lines(8), 0.4, easeInOutCubic)

  yield* waitUntil('ex2-h3')
  yield* callExp().selection(lines(4,5), 0.4, easeInOutCubic),

  yield* waitUntil('ex2-h4')
  yield* callExp().selection(lines(10,11), 0.4, easeInOutCubic),

  yield* waitUntil('ex2-reset')
  yield* callExp().selection(DEFAULT, 0.4, easeInOutCubic)


  yield* waitFor(1)
  finishScene()
});
