<script setup lang="ts">
import { ref, onMounted, watch, onUnmounted } from 'vue'

const props = defineProps({
    text: {
        type: [String, Array],
        required: true,
    },
    typeDelay: {
        type: Number,
        default: 70,
    },
    eraseDelay: {
        type: Number,
        default: 250,
    },
    startDelay: {
        type: Number,
        default: 200,
    },
    repeat: {
        type: Boolean,
        default: false,
    },
    shuffle: {
        type: Boolean,
        default: false,
    },
})

const displayedText = ref('')
const currentIndex = ref(0)
const currentPhrase = ref('')
const phrases = ref<string[]>([])
const isTyping = ref(true)
const typewriterRef = ref<HTMLElement | null>(null)
const isVisible = ref(false)
let timeout: number | null = null
let observer: IntersectionObserver | null = null

// Setup phrases from text prop
watch(() => props.text, () => {
    if (Array.isArray(props.text)) {
        phrases.value = [...props.text]
    } else {
        phrases.value = [props.text]
    }

    if (phrases.value.length > 0) {
        currentPhrase.value = phrases.value[0]
    }
}, { immediate: true })

// Start typing animation when component becomes visible
onMounted(() => {
    observer = new IntersectionObserver((entries) => {
        const [entry] = entries
        isVisible.value = entry.isIntersecting

        if (isVisible.value && !timeout) {
            setTimeout(() => {
                typeText()
            }, props.startDelay)
        }
    }, { threshold: 0.1 })

    if (typewriterRef.value) {
        observer.observe(typewriterRef.value)
    }
})

onUnmounted(() => {
    if (timeout) {
        clearTimeout(timeout)
    }

    if (observer) {
        observer.disconnect()
    }
})

function typeText() {
    if (!isVisible.value) return

    if (currentIndex.value < currentPhrase.value.length) {
        displayedText.value = currentPhrase.value.substring(0, currentIndex.value + 1)
        currentIndex.value++
        timeout = setTimeout(typeText, props.typeDelay) as unknown as number
    } else {
        isTyping.value = false
        if (props.repeat || phrases.value.length > 1) {
            timeout = setTimeout(eraseText, props.eraseDelay) as unknown as number
        }
    }
}

function eraseText() {
    if (!isVisible.value) return

    if (currentIndex.value > 0) {
        displayedText.value = currentPhrase.value.substring(0, currentIndex.value - 1)
        currentIndex.value--
        timeout = setTimeout(eraseText, props.typeDelay / 2) as unknown as number
    } else {
        isTyping.value = true
        // Move to next phrase or repeat if at the end
        let nextPhraseIndex = phrases.value.indexOf(currentPhrase.value) + 1

        if (nextPhraseIndex >= phrases.value.length) {
            if (props.repeat) {
                nextPhraseIndex = 0
                // Shuffle if needed
                if (props.shuffle && phrases.value.length > 1) {
                    phrases.value = shuffleArray([...phrases.value])
                }
            } else {
                return // Stop the animation
            }
        }

        currentPhrase.value = phrases.value[nextPhraseIndex]
        timeout = setTimeout(typeText, props.typeDelay) as unknown as number
    }
}

// Fisher-Yates shuffle algorithm
function shuffleArray(array: string[]): string[] {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1))
            ;[array[i], array[j]] = [array[j], array[i]]
    }
    return array
}
</script>

<template>
    <span ref="typewriterRef" class="typewriter">{{ displayedText }}<span class="cursor"
            :class="{ 'typing': isTyping }">|</span></span>
</template>

<style scoped>
.typewriter {
    display: inline-block;
    white-space: normal;
    word-wrap: break-word;
    overflow-wrap: break-word;
    max-width: 100%;
}

.cursor {
    display: inline-block;
    margin-left: 2px;
    opacity: 1;
}

.cursor.typing {
    animation: blink 0.7s infinite;
}

@keyframes blink {

    0%,
    100% {
        opacity: 1;
    }

    50% {
        opacity: 0;
    }
}
</style>
