import {makeProject} from '@motion-canvas/core';
import video from './for-else/forElse?scene'
import intro from './for-else/intro?scene'
// import thumbnail from './for-else/thumbnail?scene'
// import video from './functools/funcTools?scene'
// import video from './shorts/print-even/video?scene'
import end from './for-else/end?scene'
import audio from './for-else/audio/original-enhanced-v2.wav'

// import pyclassMagicMethods from './python-call/pyclassMagicMethods?scene';

export default makeProject({
  scenes: [intro, video, end],
  // scenes: [pyclassMagicMethods]
  audio: audio
});
