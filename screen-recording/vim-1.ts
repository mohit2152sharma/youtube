const words = ["Many", "Programmers", "Know", "This", "In", "Python"] 


// const words = [{text: "Many", size: 30, font: "Mono"}, {text: "Programmers", size: 30, font: "Mono"}, {text: "Know", size: 30, font: "Mono"} ...] 























// Command
// :s/\v"([^"]+)"/\='{ text: "' . submatch(1) . '", size: 30, font: "Mono"}'/g
// :s -> to start substitute command on the current line
// \v -> enables very magic mode
// "([^"]+)" -> Regex to select words inside double quotes
// \= -> Tells vim to treat the replacement as expression
// { text: "' . submatch(1) . '", fontStyle: "Mono", fontSize: "30"} -> string replacement expression
// . -> string concatenation operator
// submatch(1) -> content in first capture group
