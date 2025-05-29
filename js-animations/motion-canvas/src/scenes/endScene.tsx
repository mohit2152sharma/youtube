import { Img, Layout, makeScene2D, Txt, Video } from "@motion-canvas/2d";
import { createRef, easeInOutCubic, waitFor, waitUntil } from "@motion-canvas/core";


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

export default makeScene2D(function* (view) {
  view.fill(DraculaColors.background)


  const thankyou = createRef<Txt>();
  // const imageRef = createRef<Img>();
  const imageRef = createRef<Video>();


  view.add(
    <Layout 
      layout
      direction="column"
      justifyContent="center"
      alignItems="center"
      width={view.width}
      height={view.height}
      gap={100}
      fontSize={200}
      fontFamily="JetBrains Mono">
      <Txt
        text="Thanks for watching"
        ref={thankyou}
        opacity={0}
        fill={DraculaColors.foreground}
        />
      <Video 
        ref={imageRef}
        opacity={0}
        src="brent-rambo-thumbs-up.mp4"
        height={1080}
        width={1920}
        />
    </Layout>
  )

  yield* waitUntil('thanks')
  yield* thankyou().opacity(1,1, easeInOutCubic)
  yield* waitUntil('like')
  yield* imageRef().opacity(1,1, easeInOutCubic)
  imageRef().play()
  yield* waitFor(2)
})
