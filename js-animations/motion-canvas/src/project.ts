import {makeProject} from '@motion-canvas/core';
import funcTools from './functools/funcTools?scene';
import endScene from './common-scenes/endScene?scene';
import introScene from './functools/intro?scene';
// import pyclassMagicMethods from './python-call/pyclassMagicMethods?scene';

export default makeProject({
  scenes: [introScene, funcTools, endScene],
  // scenes: [pyclassMagicMethods]
  audio: '../audio/functools.wav'
});
