import { Code, makeScene2D } from "@motion-canvas/2d";
import { PythonCode } from "../utils/defaults";
import { createRef, waitFor } from "@motion-canvas/core";


const CodeSnippets = {
  databaseConnector : `\
class DatabaseConnector: 
  def __init__(self, connection_str: str):
    self.connection_str = connection_str

  def connect(self) -> None: 
    ...`
}

export default makeScene2D(function* (view) {
  view.fill('#242424')
  const code = createRef<Code>();


  view.add(
    <PythonCode
      code={`class Dummy:
  def main(self): 
    pass`}
      ref={code}
    fontSize={100}
    offsetX={0}
    x={0}></PythonCode>
  )


  yield* code().code.append(`\n\ndummy = Dummy()`, 0.6)

  yield* code().code.append(`\n\ndummy.main()`, 0.6)

  yield* code().code.append(`\n\ndummy()`, 0.6)

  yield* waitFor(0.6);
});
