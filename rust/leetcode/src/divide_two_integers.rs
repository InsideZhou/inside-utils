// https://leetcode.cn/problems/divide-two-integers/

use std::panic;

// 处理边界情况；转为减法；使用移位操作加速。
pub fn divide(dividend: i32, divisor: i32) -> i32 {
    if 0 == divisor {
        panic!("divisor can't be zero")
    }

    match divisor {
        0 => panic!("divisor can't be zero"),
        1 => return dividend,
        -1 => return if i32::MIN == dividend {
            i32::MAX
        } else {
            -dividend
        },
        _ => {}
    }

    if 0 == dividend {
        return 0;
    }

    let negative_dividend = if dividend < 0 { dividend } else { -dividend };
    let negative_divisor = if divisor < 0 { divisor } else { -divisor };

    if negative_dividend > negative_divisor {
        return 0;
    }

    let result = calculate_result(negative_dividend, negative_divisor) as i32;

    let negative_result = (dividend > 0 && divisor < 0) || (dividend < 0 && divisor > 0);
    if negative_result {
        return -result;
    }

    return result;
}

fn calculate_result(negative_dividend: i32, negative_divisor: i32) -> u32 {
    let mut prev_remaining = negative_dividend;
    let mut prev_result = 0_u32;

    let mut remaining = negative_dividend - negative_divisor;
    let mut result = 1_u32;

    let mut counter = 1_u32;

    loop {
        if remaining == negative_divisor {
            result += 1;
            break;
        }

        if remaining > negative_divisor {
            if prev_remaining == negative_dividend {
                break;
            }

            result = prev_result + calculate_result(prev_remaining, negative_divisor);
            break;
        }

        prev_remaining = remaining;
        prev_result = result;

        log::debug!("counter={}, remaining={}, result={}, dividend={}, divisor={}", counter, remaining, result, negative_dividend, negative_divisor);
        remaining -= negative_divisor << counter;
        result += 2_u32.pow(counter);
        counter += 1;
    }

    return result;
}

#[cfg(test)]
mod tests {
    use std::sync::Once;

    use crate::divide_two_integers::*;

    static INIT: Once = Once::new();

    /// Setup function that is only run once, even if called multiple times.
    fn setup_test() {
        INIT.call_once(|| {
            let _ = env_logger::builder().is_test(true).try_init();
        });
    }

    #[test]
    fn it_works() {
        setup_test();

        assert_eq!(2_i32.pow(0), 1);
        assert_eq!(-3 << 1, -6);
        assert_eq!(-3 << 2, -12);

        assert_eq!(divide(-4, -3), 1);
        assert_eq!(divide(10, 3), 3);
        assert_eq!(divide(7, -3), -2);

        assert_eq!(divide(1100540749, -1090366779), -1);
        assert_eq!(divide(-1139973263, -1119586052), 1);

        assert_eq!(divide(i32::MIN, 1), i32::MIN);
        assert_eq!(divide(i32::MIN, 2), i32::MIN / 2);
        assert_eq!(divide(i32::MIN, 3), i32::MIN / 3);
        assert_eq!(divide(i32::MIN, 4), i32::MIN / 4);
        assert_eq!(divide(i32::MIN, 5), i32::MIN / 5);
    }

    #[test]
    fn overflow() {
        setup_test();

        assert_eq!(divide(i32::MIN, -1), i32::MAX);
    }
}
