import { HighlightStyle } from '@codemirror/language';
import { tags } from '@lezer/highlight';
import { parser } from '@lezer/python';
import { Code, LezerHighlighter, withDefaults } from '@motion-canvas/2d';

// Dracula theme colors for syntax highlighting
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

const DraculaHighlightStyle = HighlightStyle.define([
  // Keywords and operators first (highest precedence)
  { tag: tags.keyword, color: DraculaColors.pink },
  { tag: tags.operator, color: DraculaColors.pink },
  { tag: tags.processingInstruction, color: DraculaColors.pink },

  // Functions and definitions
  { tag: tags.function(tags.variableName), color: DraculaColors.green },
  { tag: tags.function(tags.definition(tags.variableName)), color: DraculaColors.green },
  { tag: tags.definition(tags.variableName), color: DraculaColors.cyan },
  { tag: tags.className, color: DraculaColors.cyan },
  { tag: tags.typeName, color: DraculaColors.cyan },

  // Variables and names
  { tag: tags.variableName, color: DraculaColors.foreground },
  { tag: tags.name, color: DraculaColors.foreground },
  { tag: tags.propertyName, color: DraculaColors.green },
  { tag: tags.attributeName, color: DraculaColors.green },

  // Literals
  { tag: tags.string, color: DraculaColors.yellow },
  { tag: tags.special(tags.string), color: DraculaColors.yellow },
  { tag: tags.number, color: DraculaColors.purple },
  { tag: tags.literal, color: DraculaColors.purple },

  // Punctuation and brackets
  { tag: tags.punctuation, color: DraculaColors.foreground },
  { tag: tags.bracket, color: DraculaColors.foreground },
  { tag: tags.special(tags.punctuation), color: DraculaColors.cyan },

  // Decorators and meta (high precedence)
  { tag: tags.meta, color: DraculaColors.cyan },
  { tag: tags.annotation, color: DraculaColors.cyan },
  { tag: tags.special(tags.variableName), color: DraculaColors.cyan },
  { tag: tags.modifier, color: DraculaColors.orange },

  // Comments last (lowest precedence)
  { tag: tags.lineComment, color: DraculaColors.comment },
  { tag: tags.blockComment, color: DraculaColors.comment },
  { tag: tags.docComment, color: DraculaColors.comment },
  { tag: tags.comment, color: DraculaColors.comment },
]);

export const PythonHighlighter = new LezerHighlighter(parser, DraculaHighlightStyle);

export const PythonCode = withDefaults(Code, {
  highlighter: PythonHighlighter,
  fontFamily: 'JetBrains Mono',
})
