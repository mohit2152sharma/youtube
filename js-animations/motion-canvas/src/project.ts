import {makeProject} from '@motion-canvas/core';
import pyclassMagicMethods from './scenes/pyclassMagicMethods?scene'
import endScene from './scenes/endScene?scene';

export default makeProject({
  scenes: [pyclassMagicMethods, endScene],
  audio: '../audio/original-enhanced-v2.wav'
});
