import { Layout, makeScene2D, Txt } from "@motion-canvas/2d";
import { all, createRef, easeInBack, easeInBounce, easeInCirc, easeInCubic, easeInElastic, easeInExpo, easeInOutCubic, easeInQuad, easeInQuart, easeInQuint, easeInSine, makeRef, range, sequence, waitFor, waitUntil } from "@motion-canvas/core";
import { DraculaColors } from "../utils/defaults";

export default makeScene2D(function* (view) {
  
  view.fill(DraculaColors.background)

  const layout = createRef<Layout>();

  const words = [
    { text: "Many", fontStyle: "Arial Black", fontSize: 200, fill: "white", anime: easeInElastic},
		{ text: "Pythonistas", fontStyle: "JetBrains Mono", fontSize: 200, fill: DraculaColors.green, anime: easeInBounce},
		{ text: "Don't", fontStyle: "Arial Black", fontSize: 200, fill: "white", anime: easeInBounce},
		{ text: "Know", fontStyle: "Arial Black", fontSize: 200, fill: "white", anime: easeInQuint},
		{ text: "This", fontStyle: "Arial Black", fontSize: 200, fill: "white", anime: easeInQuart},
		{ text: "But", fontStyle: "Arial Black", fontSize: 200, fill: "white", anime: easeInElastic},
		{ text: "Python", fontStyle: "Arial Black", fontSize: 200, fill: "white", anime: easeInBack},
		{ text: "for", fontStyle: "JetBrains Mono", fontSize: 200, fill: DraculaColors.pink, anime: easeInCubic},
		{ text: "Loop", fontStyle: "Arial Black", fontSize: 200, fill: "white", anime: easeInSine},
		{ text: "Has", fontStyle: "Arial Black", fontSize: 200, fill: "white", anime: easeInExpo},
		{ text: "An", fontStyle: "Arial Black", fontSize: 200, fill: "white", anime: easeInCirc},
		{ text: "else", fontStyle: "JetBrains Mono", fontSize: 200, fill: DraculaColors.pink, anime: easeInQuad},
		{ text: "Clause", fontStyle: "Arial Black", fontSize: 200, fill: "white", anime: easeInBounce}
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
