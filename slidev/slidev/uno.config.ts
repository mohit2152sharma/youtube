import {
  defineConfig,
  presetAttributify,
  presetIcons,
  presetTypography,
  presetWebFonts,
  presetWind3,
  transformerDirectives,
  transformerVariantGroup
} from 'unocss'

export default defineConfig({
  theme: {
    animation: {
      keyframes: {
        'typewriter': '{from{width:0}to{width:100%}}',
        'blink-caret': '{from,to{border-color:transparent}50%{border-color:orange}}'
      },
      durations: {
        'typewriter': '3.5s',
        'blink-caret': '0.75s'
      },
      timingFns: {
        'typewriter': 'steps(40,end)',
        'blink-caret': 'step-end'
      },
      counts: {
        'blink-caret': 'infinite'
      }
    }
  },
  shortcuts: {
    'typewriter-text': 'overflow-hidden whitespace-nowrap m-auto tracking-wider border-r-2 border-r-orange-500'
  },
  rules: [
    ['animate-typewriter', { animation: 'typewriter 3.5s steps(40,end), blink-caret 0.75s step-end infinite' }]
  ],
  presets: [
    presetWind3(),
    presetAttributify(),
    presetIcons(),
    presetTypography(),
    presetWebFonts({
      fonts: {
        // ...
      },
    }),
  ],
  transformers: [
    transformerDirectives(),
    transformerVariantGroup(),
  ],
})