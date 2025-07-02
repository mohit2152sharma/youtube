import { all, createRef, easeInBack, easeInBounce, easeInCirc, easeInCubic, easeInElastic, easeInExpo, easeInOutCubic, easeInQuad, easeInQuart, easeInQuint, easeInSine, makeRef, range, sequence, waitFor, waitUntil } from "@motion-canvas/core";
import { Layout, makeScene2D, Txt } from "@motion-canvas/2d";
import { DraculaColors } from "../utils/defaults";

export default makeScene2D(function* (view) {
  
  view.fill(DraculaColors.background)

  const layout = createRef<Layout>();

  const words = [
    { text: "How", fontStyle: "Arial Black", fontSize: 200, fill: "white", anime: easeInCubic},
		{ text: "To", fontStyle: "JetBrains Mono", fontSize: 200, fill: DraculaColors.green, anime: easeInCubic},
		{ text: "Edit", fontStyle: "Arial Black", fontSize: 200, fill: "white", anime: easeInCubic},
		{ text: "Without", fontStyle: "Arial Black", fontSize: 200, fill: "white", anime: easeInCubic},
		{ text: "Repeating", fontStyle: "Arial Black", fontSize: 200, fill: "white", anime: easeInCubic},
		{ text: "Manually", fontStyle: "Arial Black", fontSize: 200, fill: "white", anime: easeInCubic},
		{ text: "In", fontStyle: "Arial Black", fontSize: 200, fill: "white", anime: easeInCubic},
		{ text: "Vim?", fontStyle: "JetBrains Mono", fontSize: 200, fill: DraculaColors.pink, anime: easeInCubic},
	]

  const wordRefs: Txt[] = [];

  view.add(
    <Layout
      ref={layout}
      layout={true}
      alignContent={"center"}
      justifyContent={"center"}
      direction={"row"}
      gap={80}
      maxWidth={view.width() - 400}
      wrap={"wrap"}
    >
      {
        range(words.length).map(i => (
          <Txt 
            ref={makeRef(wordRefs, i)}
            opacity={0}
            fontSize={words[i].fontSize}
            fill={words[i].fill}
            shadowColor={"blue"}
            fontFamily={words[i].fontStyle}
            text={words[i].text}
          />
        ))
      }
    </Layout>
  )


  yield* waitUntil("start")
  yield* sequence(0.5, 
    ...wordRefs.map((ref, index) => ref.opacity(1, 0.8, words[index].anime))
  )

  yield* waitUntil("intro-end")
})
