import { Img, Layout, makeScene2D, Txt, View2D } from "@motion-canvas/2d";
import { all, createRef } from "@motion-canvas/core";
import { DraculaColors } from "../../utils/defaults";

export function* addIntro(view: View2D, no: number, text: string) {

  const headingText = `Python Tip` 
  const heading = createRef<Txt>();
  const noRef = createRef<Txt>();
  const textRef = createRef<Txt>();
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
          ref={heading}
          fill={DraculaColors.pink}
          text={headingText}
          y={-1200}
          fontSize={300}
        />
        <Txt
          ref={noRef}
          fill={DraculaColors.foreground}
          text={`# ${no}`}
          y={-600}
          fontSize={500}
        />
      <Txt
        ref={textRef}
        fill={DraculaColors.green}
        text={text}
        y={600}
        fontSize={300}
      />
    </Layout>
  )

  yield* all(
    heading().opacity(0, 1),
    heading().position.x(view.width() / 2, 1),
    noRef().opacity(0, 1),
    noRef().position.x(view.width() / 2, 1),
    img().opacity(0, 1),
    textRef().opacity(0, 1),
    textRef().position.x(-view.width() / 2, 1),
  )
}
