/**
 * Generates an array of numbers from start to end with a specified number of steps.
 * Each step is evenly distributed across the range and rounded to 2 decimal places.
 * 
 * @param start - The starting value of the sequence
 * @param end - The ending value of the sequence  
 * @param steps - The number of values to generate in the sequence
 * @returns An array of numbers from start to end with the specified number of steps
 * 
 * @example
 * ```typescript
 * sequence(0, 10, 5) // Returns [0, 2.5, 5, 7.5, 10]
 * sequence(1, 3, 3)  // Returns [1, 1.67, 2.34]
 * ```
 */
export const sequence = (start: number, end: number, steps: number): Array<number> => {
  let result = <Array<number>>[]
  let step = (end - start) / steps
  for (let i = 0; i < steps; i++) {
    if (i === 0) {
      result[i] = start
    } else {
      result[i] = Number((result[i - 1] + step).toFixed(2))
    }
  }
  return result
}
