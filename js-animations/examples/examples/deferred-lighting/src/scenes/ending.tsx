import {makeScene2D} from '@motion-canvas/2d';
import {waitFor} from '@motion-canvas/core/lib/flow';
import {slideTransition} from '@motion-canvas/core/lib/transitions';
import {useContext} from '@motion-canvas/core/lib/utils';
import {applyViewStyles} from '../styles';

export default makeScene2D(function* (view) {
  applyViewStyles(view);
  useContext(ctx => ctx.clearRect(-1920 / 2, -1080 / 2, 1920, 1080));
  yield* slideTransition();
  yield* waitFor(5);
});
