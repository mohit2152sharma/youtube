
import { Code, LezerHighlighter, withDefaults } from '@motion-canvas/2d'
import {parser} from '@lezer/python'

export const PythonHighlighter = new LezerHighlighter(parser)

export const PythonCode = withDefaults(Code, {
  highlighter: PythonHighlighter,
})
