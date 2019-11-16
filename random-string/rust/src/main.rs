extern crate clap;
extern crate rand;

use std::process;

use clap::{App, Arg};
use rand::{Rng, thread_rng};
use rand::distributions::Alphanumeric;

const DEFAULT_LEN: usize = 16;

fn main() {
    let default_len = &DEFAULT_LEN.to_string();
    let app = App::new("Random alphanumeric string generator")
        .version("0.0.1")
        .arg(
            Arg::with_name("length")
                .default_value(default_len)
                .help("string length"),
        );

    let mut app_for_write_help = app.clone();

    let options = app.get_matches();
    let len: usize;

    match options.value_of("length") {
        Some(arg) => match arg.parse::<usize>() {
            Ok(arg_len) => match arg_len {
                0 => {
                    len = DEFAULT_LEN;
                }
                _ => len = arg_len,
            },
            _ => {
                let _result = app_for_write_help.print_help();
                process::exit(1)
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
