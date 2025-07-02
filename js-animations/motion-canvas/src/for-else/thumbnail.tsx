import { Code, Img, Layout, makeScene2D, Rect, Txt } from "@motion-canvas/2d";
import { DraculaColors, PythonCode, PythonHighlighter } from "../utils/defaults";
import { createRef, easeInOutCubic, waitUntil } from "@motion-canvas/core";

export default makeScene2D(function* (view) {

    view.fill(DraculaColors.background);


    // Create refs for new elements
    const linusImg = createRef<Img>();
    const txt = createRef<Code>();
    const rect = createRef<Rect>()

    view.add(
      <Layout>
        <Img
            ref={linusImg}
            src="linus-laughing.png"
            // width={1720/2.5}
            // height={1080/2.5}
            x={view.width() / 2 - 400}
            y={view.height()/2 + 900 }
            offset={1}
            scale={3}
            shadowColor="#fdf6f0"
            shadowOffset={40}
            shadowBlur={200}
        />
        <PythonCode 
          code="for else"
          highlighter={PythonHighlighter}
          shadowBlur={100}
          shadowOffset={20}
          shadowColor={"#c1ffd7"}
          ref={txt}
          opacity={1}
          fontFamily="JetBrains Mono"
          fontSize={500}
          fontWeight={"bold"}
          x={700}
          y={-800}
          zIndex={10}
        />
</Layout>
    );


  yield* waitUntil('thumbnail-start')

  yield* linusImg().opacity(0, 1, easeInOutCubic)
})
