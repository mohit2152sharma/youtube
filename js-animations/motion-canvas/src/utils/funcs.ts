import { Code, PossibleCodeSelection } from "@motion-canvas/2d";
import { DEFAULT, easeInOutCubic, Reference, SignalValue, TimingFunction } from "@motion-canvas/core";

export function* highlight (
  code: Reference<Code>,
  selection: typeof DEFAULT | SignalValue<PossibleCodeSelection>,
  duration: number = 1, 
  easeFunc: TimingFunction = easeInOutCubic
) {
  yield code().selection(selection, duration, easeFunc)
}


export function* reset(
  code: Reference<Code>,
  duration: number = 1,
  easeFunc: TimingFunction = easeInOutCubic
) {
  yield code().selection(DEFAULT, duration, easeFunc)
}
