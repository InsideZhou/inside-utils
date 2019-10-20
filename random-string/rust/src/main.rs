extern crate rand;

use rand::distributions::Alphanumeric;
use rand::{thread_rng, Rng};

use std::env;
use std::process;

const DEFAULT_LEN: usize = 16;

fn main() {
    let mut len: usize = DEFAULT_LEN;

    match env::args().nth(1) {
        Some(arg) => match arg.parse::<usize>() {
            Ok(arg_len) => len = arg_len,
            _ => {
                eprintln!("(len must be usize, got {})", arg);
                process::abort();
            }
        },
        _ => println!("(using default len={})", DEFAULT_LEN),
    }

    if 0 == len {
        len = DEFAULT_LEN;
        println!("(got len=0, using default len={})", len)
    }

    let rand_string: String = thread_rng()
        .sample_iter(&Alphanumeric)
        .skip(len)
        .take(len)
        .collect();

    println!("{}", rand_string)
}
