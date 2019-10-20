extern crate rand;

use rand::distributions::Alphanumeric;
use rand::{thread_rng, Rng};

use std::env;
use std::process;

fn main() {
    let mut num: usize = 16;

    match env::args().nth(1) {
        Some(arg) => match arg.parse::<usize>() {
            Ok(n) => num = n,
            _ => {
                eprintln!("(argument must be usize, got {})", arg);
                process::abort();
            }
        },
        _ => println!("(using default n={})", num),
    }

    let rand_string: String = thread_rng()
        .sample_iter(&Alphanumeric)
        .skip(num)
        .take(num)
        .collect();

    println!("{}", rand_string);
}
