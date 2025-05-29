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
  { tag: tags.keyword, color: DraculaColors.pink },
  { tag: tags.function(tags.variableName), color: DraculaColors.green },
  { tag: tags.function(tags.definition(tags.variableName)), color: DraculaColors.green },
  { tag: tags.variableName, color: DraculaColors.foreground },
  { tag: tags.string, color: DraculaColors.yellow },
  { tag: tags.comment, color: DraculaColors.comment },
  { tag: tags.number, color: DraculaColors.purple },
  { tag: tags.operator, color: DraculaColors.pink },
  { tag: tags.punctuation, color: DraculaColors.foreground },
  { tag: tags.bracket, color: DraculaColors.foreground },
  { tag: tags.definition(tags.variableName), color: DraculaColors.cyan },
  { tag: tags.className, color: DraculaColors.cyan },
  { tag: tags.typeName, color: DraculaColors.cyan },
  { tag: tags.propertyName, color: DraculaColors.green },
  { tag: tags.literal, color: DraculaColors.purple },
  { tag: tags.special(tags.string), color: DraculaColors.yellow },
]);

export const PythonHighlighter = new LezerHighlighter(parser, DraculaHighlightStyle);

export const PythonCode = withDefaults(Code, {
  highlighter: PythonHighlighter,
  fontFamily: 'JetBrains Mono',
})
