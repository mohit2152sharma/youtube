import { Code, Img, Layout, Txt, View2D } from "@motion-canvas/2d";
import { all, createRef } from "@motion-canvas/core";
import { DraculaColors, PythonCode } from "../../utils/defaults";

export function* addIntro (view: View2D, introBottonText: string) {

  const noob = createRef<Txt>();
  const vs = createRef<Txt>();
  const pro = createRef<Txt>();
  const introText = createRef<Code>();
  const img = createRef<Img>();
  view.add(
    <Layout
      layout={false}
      direction="column"
      fontFamily="JetBrains Mono"
      justifyContent={"center"}
      alignContent={"center"}
      alignItems={"center"}
    >
      <Img
        ref={img}
        src="matrix-style.jpg"
        zIndex={-1}
        scale={1.2}
        opacity={0.2}
      />
      <Txt
        ref={noob}
        fill={DraculaColors.pink}
        text="noob"
        x={0}
        y={-1200}
        fontSize={500}
      />
      <Txt
        ref={vs}
        fill={DraculaColors.foreground}
        text="vs"
        y={-600}
        fontSize={500}
      />
      <Txt
        ref={pro}
        fill={DraculaColors.green}
        text="pro"
        fontSize={500}
      />
      <PythonCode
        ref={introText}
        code={introBottonText}
        fontSize={200}
        y={1200}
      />
    </Layout>
  )

  yield* all(
    noob().opacity(0, 1),
    noob().position.x(view.width() / 2, 1),
    vs().opacity(0, 1),
    vs().position.x(-view.width() / 2, 1),
    pro().opacity(0, 1),
    pro().position.x(view.width() / 2, 1),
    img().opacity(0, 1),
    introText().opacity(0, 1),
    introText().position.x(-view.width() / 2, 1),
  )
}
