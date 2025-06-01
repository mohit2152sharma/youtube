import { Code, Layout, Line, lines, makeScene2D, Rect, Txt } from "@motion-canvas/2d";
import {
    all,
    createRef,
    createSignal,
    DEFAULT,
    easeInOutCubic,
    finishScene,
    useDuration,
    waitFor,
    waitUntil
} from "@motion-canvas/core";
import { PythonCode, PythonHighlighter } from "../utils/defaults";

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

// Code snippets for each functools function
const CodeSnippets = {
    cache: `import functools
import time

@functools.cache
def factorial(n):
    """Simulates a factorial calculation"""
    time.sleep(0.1)  
    return n * factorial(n-1) if n > 1 else 1

# First call - computes all values
print(factorial(5))  # Takes ~0.5 seconds

# Subsequent calls - instant (cached)
print(factorial(3))  # Instant - already computed
print(factorial(5))  # Instant - cached result`,

    cached_property: `import functools
import statistics

class DataSet:
    def __init__(self, numbers):
        self._data = tuple(numbers)
    
    @functools.cached_property
    def mean(self):
        """Expensive computation - only calculated once"""
        print("Calculating mean...")
        return statistics.mean(self._data)

# Usage
dataset = DataSet([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# First call - calculates and caches
print(dataset.mean)
# Second call - returns cached value
print(dataset.mean)`,

    cmp_to_key: `import functools

def compare_strings_ignore_case(a, b):
    """Old-style comparison function"""
    a_lower = a.lower()
    b_lower = b.lower()
    if a_lower < b_lower:
        return -1
    elif a_lower > b_lower:
        return 1
    else:
        return 0

# Convert to key function for modern sorting
words = ['Apple', 'banana', 'Cherry', 'date']

# Using cmp_to_key to convert comparison function
sorted_words = sorted(words, 
    key=functools.cmp_to_key(compare_strings_ignore_case))
print(sorted_words)  # ['Apple', 'banana', 'Cherry', 'date']`,

    lru_cache: `import functools

@functools.lru_cache(maxsize=3)
def fibonacci(n):
    """Fibonacci with limited cache size"""
    print(f"Computing fib({n})")
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Calculate some fibonacci numbers
print(f"fib(10) = {fibonacci(10)}")
print(f"fib(8) = {fibonacci(8)}")   # Some values cached
print(f"fib(12) = {fibonacci(12)}")

# Check cache statistics
print(f"Cache info: {fibonacci.cache_info()}")
# Cache info: CacheInfo(hits=12, misses=13, maxsize=3, currsize=3)

# Clear cache
fibonacci.cache_clear()`,

    partial: `import functools

def multiply(x, y, z):
    """Simple multiplication function"""
    return x * y * z

# Create partial functions
double = functools.partial(multiply, 2)        # x=2, need y and z
triple_by_2 = functools.partial(multiply, 3, 2) # x=3, y=2, need z

print(double(5, 3))     # multiply(2, 5, 3) = 30
print(triple_by_2(4))   # multiply(3, 2, 4) = 24`,

    singledispatch: `import functools
from decimal import Decimal

@functools.singledispatch
def format_value(value):
    """Default implementation for unknown types"""
    return f"Unknown type: {type(value).__name__} = {value}"

@format_value.register(float)
def _(value):
    return f"Float: {value:.2f}"

@format_value.register(str)
def _(value):
    return f"String: '{value}' (length: {len(value)})"

print(format_value(3.14159))
# Float: 3.14
print(format_value("hello")) 
# String: 'hello' (length: 5)`,

    singledispatchmethod: `import functools

class Formatter:
    @functools.singledispatchmethod
    def format(self, value):
        """Default formatter"""
        return f"Default: {value}"
    
    @format.register
    def _(self, value: float):
        return f"Float: {value:.3f}"
    
    @format.register
    def _(self, value: str):
        return f"String: '{value.upper()}'"

# Usage
formatter = Formatter()
print(formatter.format(3.14159))   # Float: 3.142
print(formatter.format("hello"))   # String: 'HELLO'`,

    update_wrapper: `
def original_function():
    """This is the original function's docstring"""
    return "original result"

def manual_wrapper(*args, **kwargs):
    """Manual wrapper function"""
    result = original_function(*args, **kwargs)
    return result

# Without update_wrapper
print(f"Wrapper name: {manual_wrapper.__name__}") # Wrapper name: manual_wrapper
print(f"Wrapper doc: {manual_wrapper.__doc__}") # Wrapper doc: Manual wrapper function

# Using update_wrapper
functools.update_wrapper(manual_wrapper, original_function)
print(f"After update_wrapper name: {manual_wrapper.__name__}")  
# After update_wrapper name: original_function
print(f"After update_wrapper doc: {manual_wrapper.__doc__}")
# After update_wrapper doc: This is the original function's docstring
`,

    wraps: `import time

def timer(func):
    """Decorator function to print execution time"""
    @functools.wraps(func)  # Preserves original function metadata
    def wrapper(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        print(f"Time taken: {time.time() - t0}")
        return result
    return wrapper

@timer
def greet(name: str):
    """A function that greets user"""
    return f"Welcome {name}"

print(greet.__doc__)   
# A function that greets user`
};

export default makeScene2D(function* (view) {
    // Set Dracula background
    view.fill(DraculaColors.background);

    // Main layout components
    const mainLayout = createRef<Layout>();
    const titleText = createRef<Txt>();
    const codeRect = createRef<Rect>();
    const code = createRef<Code>();

    view.add(
        <Layout
            ref={mainLayout}
            direction="column"
            alignItems="center"
            justifyContent="center"
            width={view.width}
            height={view.height}
            gap={60}
        >
            {/* Function title */}
            <Txt
                ref={titleText}
                text="functools"
                fontSize={120}
                fill={DraculaColors.cyan}
                fontFamily="JetBrains Mono"
                fontWeight={700}
                y={-view.height() / 2 + 100}
            />

            {/* Code container */}
            <Rect
                ref={codeRect}
                radius={16}
                padding={40}
                fill={DraculaColors.currentLine}
                width={view.width() - 400}
                height={view.height() - 500}
            >
                <PythonCode
                    ref={code}
                    highlighter={PythonHighlighter}
                    fontSize={64}
                    fill={DraculaColors.foreground}
                    fontFamily="JetBrains Mono"
                />
            </Rect>
        </Layout>
    );

    // ===== @functools.cache =====
    /*
    Voiceover script:
    "Let's start with functools.cache, it's a decorator that caches the results of a function"
    "When we decorate a function with @functools.cache..."
    "It automatically memoizes function results"
    "The first call to expensive_calculation with 5..."
    "Takes time because it computes all recursive calls"
    "But subsequent calls with previously computed values..."
    "Return instantly from the cache"
    "This is perfect for expensive recursive functions like factorial calculations"
    */

    yield* waitUntil('cache-intro')
    yield* titleText().text('@functools.cache', 1, easeInOutCubic);
    yield* waitUntil('cache-code')
    yield* code().code(CodeSnippets.cache, 1);

    yield* waitUntil('cache-decorator');
    yield* code().selection(lines(3), 1);

    yield* waitUntil('cache-function');
    yield* code().selection(lines(4, 8), 1);

    yield* waitUntil('cache-decorator-again')
    yield* code().selection(lines(3), 1);

    yield* waitUntil('cache-function-result')
    yield* code().selection(lines(7), 1)

    yield* waitUntil('cache-first-call');
    yield* code().selection(lines(10), 1);

    yield* waitUntil('cache-expensive-lines')
    yield* code().selection(lines(6,7), 1);

    yield* waitUntil('cache-subsequent');
    yield* code().selection(lines(13, 15), 1);

    yield* waitUntil('cache-subsequent-cache')
    yield* all(
        code().selection([[[3, 11], [3, 16]], [[13, 0], [13, 20]], [[14, 0], [14, 20]]], 1)
    )

    yield* waitUntil('cache-reset');
    yield* code().selection(DEFAULT, 1);

    // ===== @functools.cached_property =====
    /*
    Voiceover script:
    "Next is cached_property, it's the same as cache but for class properties"
    "When we define a class with expensive property calculations..."
    "The cached_property decorator ensures the computation happens only once"
    "Here we have a DataSet class with a mean calculation"
    "The first access to the mean property triggers the calculation"
    "But subsequent accesses return the cached value immediately"
    "This is ideal for expensive computations on immutable data"
    */

    yield* all(
        titleText().text('@functools.cached_property', useDuration('cached-property-intro'), easeInOutCubic),
        code().code(CodeSnippets.cached_property, useDuration('cached-property-code'), easeInOutCubic)
    );

    yield* waitUntil('cached-property-class');
    yield* code().selection(lines(3, 5), 1);

    yield* waitUntil('cached-property-computation');
    yield* code().selection(lines(8, 11), 1);

    yield* waitUntil('cached-property-decorator');
    yield* code().selection(lines(7), 1);

    yield* waitUntil('classname')
    yield* code().selection(lines(3), 1)

    yield* waitUntil('propname')
    yield* all(
        code().selection([lines(3), lines(8)], 1)
    )

    yield* waitUntil('cached-property-usage');
    yield* code().selection(lines(17), 1);

    yield* waitUntil('cached-property-first');
    yield* code().selection([lines(17), lines(9), lines(11)], 1);

    yield* waitUntil('cached-property-second');
    yield* code().selection(lines(19), 1);

    yield* waitUntil('cached-property-cache')
    yield* code().selection([lines(19), lines(7)], 1)

    yield* waitUntil('cached-property-reset');
    yield* code().selection(DEFAULT, 1);

    // ===== functools.cmp_to_key =====
    /*
    Voiceover script:
    "functools.cmp_to_key converts old-style comparison functions to modern key functions"
    "Here we have an old-style comparison function that compares strings case-insensitively"
    "It returns -1, 0, or 1 based on the comparison result"
    "Modern Python sorting uses key functions instead"
    "We use cmp_to_key to convert our comparison function"
    "This allows us to use the old comparison logic with modern sorting"
    */

    // yield* waitUntil('cmp-to-key-intro');
    // yield* titleText().text('functools.cmp_to_key', 1);
    // yield* code().code(CodeSnippets.cmp_to_key, 1);
    //
    // yield* waitUntil('cmp-to-key-function');
    // yield* code().selection(lines(2, 10), 1);
    //
    // yield* waitUntil('cmp-to-key-logic');
    // yield* code().selection(lines(5, 9), 1);
    //
    // yield* waitUntil('cmp-to-key-data');
    // yield* code().selection(lines(12), 1);
    //
    // yield* waitUntil('cmp-to-key-convert');
    // yield* code().selection(lines(14, 16), 1);
    //
    // yield* waitUntil('cmp-to-key-result');
    // yield* code().selection(lines(17), 1);
    //
    // yield* waitUntil('cmp-to-key-reset');
    // yield* code().selection(DEFAULT, 1);

    // ===== @functools.lru_cache =====
    /*
    Voiceover script:
    "lru_cache provides Least Recently Used caching with a size limit"
    "Unlike cache, lru_cache has a maxsize parameter"
    "This prevents unlimited memory growth"
    "Here we set maxsize to 3 for our fibonacci function"
    "The cache keeps track of the 3 most recently used values"
    "We can inspect cache statistics with cache_info"
    "And clear the cache manually when needed"
    */

    yield* all(
        titleText().text('@functools.lru_cache', useDuration('lru-cache-intro')),
        code().code(CodeSnippets.lru_cache, useDuration('lur-cache-code'))
    )

    yield* waitUntil('lru-cache-decorator');
    yield* code().selection(lines(2), 1);

    yield* waitUntil('lru-cache-maxsize');
    yield* code().selection(code().findAllRanges(/maxsize/gi), 1);

    yield* waitUntil('lru-cache-maxsize3')
    yield* code().selection(code().findAllRanges(/maxsize=3/gi), 1);

    yield* waitUntil('lru-cache-function');
    yield* code().selection(lines(3, 8), 1);

    yield* waitUntil('lru-cache-calls');
    yield* code().selection(lines(11, 13), 1);

    yield* waitUntil('lru-cache-stats');
    yield* code().selection(lines(16, 17), 1);

    yield* waitUntil('lru-cache-clear');
    yield* code().selection(lines(20), 1);

    yield* waitUntil('lru-cache-reset');
    yield* code().selection(DEFAULT, 1);
    //
    // ===== functools.partial =====
    /*
    Voiceover script:
    "functools.partial creates new functions with some arguments pre-filled"
    "Starting with a simple multiply function that takes three arguments"
    "We can create a partial function 'double' with x pre-set to 2"
    "Now double only needs two arguments instead of three"
    "Similarly, triple_by_2 has both x and y pre-filled"
    "This is useful for creating specialized functions from general ones"
    */

    yield* waitUntil('partial-intro');
    yield* titleText().text('functools.partial', 1);
    yield* code().code(CodeSnippets.partial, 1);

    yield* waitUntil('partial-original');
    yield* code().selection(lines(2, 4), 1);

    yield* waitUntil('partial-args')
    yield* code().selection([[2, 12], [2, 21]], 1)

    yield* waitUntil('partial-create');
    yield* code().selection(lines(6, 7), 1);

    yield* waitUntil('partial-preset')
    yield* code().selection(code().findFirstRange(/\(multiply, 2\)/g), 1)

    yield* waitUntil('partial-usage');
    yield* code().selection(lines(10), 1);

    yield * waitUntil('partial-triple')
    yield* code().selection(lines(8), 1)

    yield* waitUntil('partial-triple-args')
    yield* code().selection(code().findFirstRange(/\(multiply, 3, 2\)/g), 1)

    yield* waitUntil('partial-practical');
    yield* code().selection(lines(10, 11), 1);

    yield* waitUntil('partial-reset');
    yield* code().selection(DEFAULT, 1);

    // ===== @functools.singledispatch =====
    /*
    Voiceover script:
    "singledispatch creates function overloads based on the first argument's type"
    "We start with a base function decorated with @singledispatch"
    "Then register implementations for specific types using @function.register"
    "Each registered function handles a different type"
    "When we call format_value, it automatically dispatches to the right implementation"
    "Based on the type of the first argument"
    "This provides type-based polymorphism in Python"
    */

    yield* waitUntil('singledispatch-intro');
    yield* titleText().text('@functools.singledispatch', 1);
    yield* code().code(CodeSnippets.singledispatch, 1);

    yield* waitUntil('singledispatch-base');
    yield* code().selection(lines(3, 6), 1);

    yield* waitUntil('singledispatch-register');
    yield* code().selection([lines(8), lines(12)], 1);

    yield* waitUntil('singledispatch-types');
    yield* code().selection(code().findAllRanges(/register\(.*\)/g), 1);

    yield* waitUntil('singledispatch-usage');
    yield* code().selection(lines(16, 19), 1);

    yield* waitUntil('singledispatch-reset');
    yield* code().selection(DEFAULT, 1);

    // ===== functools.singledispatchmethod =====
    /*
    Voiceover script:
    "singledispatchmethod brings single dispatch to class methods"
    "We define a method with @singledispatchmethod"
    "Then register implementations for different types"
    "Each registered method handles a specific type"
    "When we call the method, it dispatches based on the argument type"
    "This is useful for creating polymorphic methods in classes"
    */

    yield* waitUntil('singledispatchmethod-intro');
    yield* titleText().text('functools.singledispatchmethod', 1);
    yield* code().code(CodeSnippets.singledispatchmethod, 1);

    yield* waitUntil('singledispatchmethod-base');
    yield* code().selection(lines(3, 6), 1);

    yield* waitUntil('singledispatchmethod-register');
    yield* code().selection(code().findAllRanges(/@format.register/g), 1);

    yield* waitUntil('singledispatchmethod-types');
    yield* code().selection(code().findAllRanges(/value: \w+/g), 1);

    yield* waitUntil('singledispatchmethod-usage');
    yield* code().selection(lines(16, 19), 1);

    yield* waitUntil('singledispatchmethod-reset');
    yield* code().selection(DEFAULT, 1);

    // ===== functools.update_wrapper =====
    /*
    Voiceover script:
    "update_wrapper preserves the original function's metadata in wrapper functions"
    "Here we have an original function with its own docstring"
    "And a manual wrapper that calls the original"
    "Without update_wrapper, the wrapper keeps its own metadata"
    "After applying update_wrapper, the wrapper appears to be the original function"
    "This preserves important metadata like function name and documentation"
    */

    yield* waitUntil('update-wrapper-intro');
    yield* titleText().text('functools.update_wrapper', 1);
    yield* code().code(CodeSnippets.update_wrapper, 1);

    yield* waitUntil('update-wrapper-original');
    yield* code().selection(lines(1, 3), 1);

    yield* waitUntil('original-docstring')
    yield* code().selection(lines(2), 1)

    yield* waitUntil('update-wrapper-manual');
    yield* code().selection(lines(5, 8), 1);

    yield* waitUntil('manual-call-original')
    yield* code().selection(code().findFirstRange(/original_function\(\*args, \*\*kwargs\)/g), 1)

    yield* waitUntil('update-wrapper-without');
    yield* code().selection(lines(11, 12), 1);

    const wrapper = createSignal(() => {
        const range = code().findAllRanges(/# Wrapper.*/g)
        const bbox = code().getSelectionBBox(range)
        return bbox
    })

    const lineRef = createRef<Line>();
    const lineRefs = wrapper().map(() => createRef<Line>())
    code().add(
        lineRefs.map((ref, index) => (
        <Line 
            offset={0}
            ref={ref}
            points={[wrapper()[index].bottomLeft, wrapper()[index].bottomRight]}
            lineWidth={4}
            stroke={"white"}
            opacity={0}
        />
        ))
    )
    yield* waitUntil('update-wrapper-wo-output')
    yield* all(
        code().selection(code().findAllRanges(/# Wrapper.*/g), 1),
        ...lineRefs.map((ref) => {
            return ref().opacity(1,1)
        })
    )

    yield* waitUntil('update-wrapper-apply');
    yield* all( 
        code().selection(lines(15), 1),
        ...lineRefs.map((ref) => {
            return ref().opacity(0,1)
        })
    )

    yield* waitUntil('update-wrapper-after');
    yield* code().selection(lines(16, 19), 1);

    yield* waitUntil('update-wrapper-reset');
    yield* code().selection(DEFAULT, 1);

    // ===== @functools.wraps =====
    /*
    Voiceover script:
    "Finally, @functools.wraps is a convenient decorator for applying update_wrapper"
    "Here we create a retry decorator that wraps functions"
    "The @functools.wraps decorator preserves the original function's metadata"
    "Without it, the wrapper would lose the original function's name and docstring"
    "This is the standard way to create well-behaved decorators in Python"
    "It ensures that decorated functions maintain their original identity"
    */

    yield* waitUntil('wraps-intro');
    yield* titleText().text('@functools.wraps', 1);
    yield* code().code(CodeSnippets.wraps, 1);

    yield* waitUntil('wraps-decorator');
    yield* code().selection(lines(2, 10), 1);

    yield* waitUntil('wraps-decorator-funcs')
    yield* code().selection(lines(12, 15), 1)

    yield* waitUntil('wraps-preserve');
    yield* code().selection(lines(4), 1);

    yield* waitUntil('wraps-preserve-name')
    yield* code().selection([lines(4), code().findFirstRange(/greet/g)], 1)

    yield* waitUntil('wraps-docstring')
    yield* code().selection(
        [lines(4), code().findFirstRange(/greet/g), lines(14)],
        1
    )

    yield* waitUntil('wraps-wrapper');
    yield* code().selection(lines(17, 18), 1);

    yield* waitUntil('wraps-reset');
    yield* code().selection(DEFAULT, 1);

    yield* waitUntil('end');
    yield* all(
        titleText().opacity(0, 1),
        codeRect().opacity(0, 1)
    );
    //
    finishScene();
});

