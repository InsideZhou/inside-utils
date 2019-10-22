extern crate rand;
extern crate clap;

use rand::distributions::Alphanumeric;
use rand::{thread_rng, Rng};
use clap::{Arg, App};

use std::process;

const DEFAULT_LEN: usize = 16;

fn main() {
    let default_len = &DEFAULT_LEN.to_string();
    let options = App::new("Random String Generator")
        .version("0.1.0")
        .arg(Arg::with_name("length").default_value(default_len))
        .get_matches();

    let len: usize;

    match options.value_of("length") {
        Some(arg) => match arg.parse::<usize>() {
            Ok(arg_len) => match arg_len {
                0 => {
                    len = DEFAULT_LEN;
                }
                _ => len = arg_len,
            }
            _ => {
                eprintln!("(len must be usize, got {})", arg);
                process::abort();
            }
        },
        _ => len = DEFAULT_LEN,
    }

    let rand_string: String = thread_rng()
        .sample_iter(&Alphanumeric)
        .skip(len)
        .take(len)
        .collect();

    println!("{}", rand_string)
}
