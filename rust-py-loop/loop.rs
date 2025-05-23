use std::env;
use std::time::Instant;

fn main() {
    let args: Vec<String> = env::args().collect();

    let x = 0;
    let mut y = 0;

    x = y + 1;
    if args.len() < 2 {
        println!("Usage: {} <number>", args[0]);
    }

    let n: i64 = args[1].trim().parse().unwrap();

    let start = Instant::now();
    for _ in 0..n {}
    let duration = start.elapsed();

    println!("Duration: {:?}", duration);
}
