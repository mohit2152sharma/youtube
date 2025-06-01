import { Code, Img, Layout, makeScene2D, Path, Txt } from "@motion-canvas/2d";
import {
    all,
    createRef,
    delay,
    easeInOutCubic,
    easeOutCubic,
    easeOutSine,
    sequence,
    waitUntil
} from "@motion-canvas/core";
import { PythonCode, PythonHighlighter } from "../utils/defaults";
import { sequence as seq } from '../utils/sequence'

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
    view.fill(DraculaColors.background);

    // Create refs for new elements
    const linusImg = createRef<Img>();
    const importFunc = createRef<Code>();
    const functs = createRef<Code>();
    const curvedArrow = createRef<Path>();

    // Create refs for all elements
    const title = createRef<Txt>();
    const subtitle = createRef<Txt>();
    const functionRefs = [
        createRef<Code>(), // @functools.cache
        createRef<Code>(), // @functools.cached_property
        createRef<Code>(), // functools.cmp_to_key
        createRef<Code>(), // @functools.lru_cache
        createRef<Code>(), // functools.partial
        createRef<Code>(), // @functools.singledispatch
        createRef<Code>(), // functools.singledispatchmethod
        createRef<Code>(), // functools.update_wrapper
        createRef<Code>()  // @functools.wraps
    ];
    const functionRefs2 = functionRefs.map(() => createRef<Code>())

    const functionNames = [
        '@functools.cache',
        '@functools.cached_property',
        'functools.cmp_to_key',
        '@functools.lru_cache',
        'functools.partial',
        '@functools.singledispatch',
        'functools.singledispatchmethod',
        'functools.update_wrapper',
        '@functools.wraps'
    ];

    // Add Linus image
    view.add(
        <Img
            ref={linusImg}
            src="/linus.png"
            width={400}
            height={400}
            x={view.width() / 2}
            y={view.height() / 2}
            offset={1}
            scale={5}
        />
    );

    // Add classes text
    view.add(
        <PythonCode
            ref={importFunc}
            code="import functools"
            fontSize={200}
            highlighter={PythonHighlighter}
            fontFamily="JetBrains Mono"
            fontWeight={600}
            x={-view.width() / 2 + 100}
            y={-view.height() / 2 + 300}
            offset={-1}
        />
    );

    const opacities = seq(1, 0, functionRefs.length)
    view.add(
        <Layout layout x={-800} y={300} justifyContent="start" gap={10} direction="column">
            {
                functionRefs.map((ref, index) => (
                    <PythonCode
                        ref={ref}
                        highlighter={PythonHighlighter}
                        fontSize={75}
                        code={functionNames[index]}
                        opacity={opacities[index]}
                    />
                ))
            }
        </Layout>
    )

    // Add title
    view.add(
        <Txt
            ref={title}
            text="Python functools"
            fontSize={220}
            fill={DraculaColors.cyan}
            fontFamily="JetBrains Mono"
            fontWeight={700}
            y={-500}
            opacity={0}
        />
    );

    // Add subtitle
    view.add(
        <Txt
            ref={subtitle}
            text="powerful tools for functional programming"
            fontSize={100}
            fill={DraculaColors.purple}
            fontFamily="JetBrains Mono"
            fontWeight={400}
            y={-280}
            opacity={0}
        />
    );

    // Add function names
    view.add(
        <Layout direction="column" justifyContent="start" alignItems="start" layout gap={10} y={400}>
            {functionRefs2.map((ref, index) => (
                <PythonCode
                    ref={ref}
                    code={functionNames[index]}
                    highlighter={PythonHighlighter}
                    fontSize={75}
                    fill={DraculaColors.orange}
                    fontFamily="JetBrains Mono"
                    fontWeight={500}
                    y={-60 + index * 70}
                    x={view.width() + 200}
                    opacity={0}
                    alignSelf="start"
                />
            ))}
        </Layout>
    );

    // Animation sequence
    yield* waitUntil('intro-start');


    // Fade out intro elements
    yield* all(
        linusImg().opacity(0, 2, easeInOutCubic),
        importFunc().opacity(0, 2, easeInOutCubic),
        ...functionRefs.map((ref) => {
            return delay(0.1, ref().opacity(0, 1, easeOutCubic))
        })
    );

    yield* waitUntil('title-appear');
    yield* title().opacity(1, 1, easeInOutCubic);

    yield* waitUntil('subtitle-appear');
    yield* subtitle().opacity(1, 1, easeInOutCubic);

    yield* waitUntil('functions-start');
    yield* sequence(0.3, ...functionRefs2.map((ref, index) => {
        return all(
            ref().opacity(1, 1, easeInOutCubic)
        );
    }));

    yield* waitUntil('intro-end')
}); 
