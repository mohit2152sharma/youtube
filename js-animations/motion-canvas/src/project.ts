import {makeProject} from '@motion-canvas/core';
import video from './shorts/print-even/video?scene'
import end from './shorts/end?scene'
import audio from './shorts/print-even/original-enhanced-v2.wav'

// import pyclassMagicMethods from './python-call/pyclassMagicMethods?scene';

export default makeProject({
  scenes: [video, end],
  // scenes: [pyclassMagicMethods]
  audio: audio
});
