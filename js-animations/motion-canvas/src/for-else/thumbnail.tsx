import { Code, Img, Layout, makeScene2D, Txt } from "@motion-canvas/2d";
import { DraculaColors, PythonCode, PythonHighlighter } from "../utils/defaults";
import { createRef, easeInOutCubic, waitUntil } from "@motion-canvas/core";

export default makeScene2D(function* (view) {

    view.fill(DraculaColors.background);


    // Create refs for new elements
    const linusImg = createRef<Img>();
    const txt = createRef<Code>();

    view.add(
      <Layout>
        <Img
            ref={linusImg}
            src="linus-standing.png"
            // width={1720/2.5}
            // height={1080/2.5}
            x={view.width() / 2 + 800}
            y={view.height() + 700}
            offset={1}
            scale={4}
        />
        <PythonCode 
          code="for/else"
          highlighter={PythonHighlighter}
          ref={txt}
          opacity={1}
          fontFamily="JetBrains Mono"
          fontSize={400}
          x={-800}
          y={100}
        />
</Layout>
    );


  yield* waitUntil('thumbnail-start')

  yield* linusImg().opacity(0, 1, easeInOutCubic)
})
