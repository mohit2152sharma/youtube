import { Img, Layout, makeScene2D } from "@motion-canvas/2d";
import { DraculaColors } from "../utils/defaults";
import { all, createRef, easeInBounce, easeInCirc, easeInElastic, easeInExpo, easeInOutBounce, waitFor, waitUntil } from "@motion-canvas/core";

export default makeScene2D(function* (view) {

  view.fill(DraculaColors.background)

  const subs = createRef<Img>();
  const like = createRef<Img>();
  const layoutRef = createRef<Layout>();

  view.add(
    <Layout layout={true} gap={30} alignItems={"center"} justifyContent={"space-between"} ref={layoutRef} direction="column">
      <Img src="subscribe.png" ref={subs} y={-view.height() / 2 + 300} scale={0}>
      </Img>
    </Layout>
  )

  yield* waitUntil('subs')
  yield* all(
    subs().opacity(1,1),
    subs().scale(1,1, easeInOutBounce)
  )
  
  yield* waitUntil('outroend')
})
