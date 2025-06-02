import { Img, Layout, makeScene2D } from "@motion-canvas/2d";
import { DraculaColors } from "../utils/defaults";
import { all, createRef, easeInBounce, easeInCirc, easeInElastic, easeInExpo, easeInOutBounce, waitFor, waitUntil } from "@motion-canvas/core";

export default makeScene2D(function* (view) {

  view.fill(DraculaColors.background)

  const subs = createRef<Img>();
  const like = createRef<Img>();
  const layoutRef = createRef<Layout>();

  view.add(
    <Layout layout={false} gap={30} alignItems={"center"} justifyContent={"space-between"} ref={layoutRef} direction="column">
      <Img src="subscribe.png" ref={subs} y={-1400} scale={0}>
      </Img>
      <Img src="thumbsup.png" ref={like} scale={0} radius={50} height={800} y={400}>
      </Img>
    </Layout>
  )

  yield* waitUntil('like')
  yield* all(
    like().opacity(1,1),
    like().scale(3,1, easeInOutBounce)
  )

  yield* waitUntil('subs')
  yield* all(
    subs().opacity(1,1),
    subs().scale(1,1, easeInOutBounce)
  )
  
  yield* waitUntil('outroend')
})
