// https://leetcode.cn/problems/path-in-zigzag-labelled-binary-tree/

#[allow(dead_code)]
pub fn path_in_zig_zag_tree(label: i32) -> Vec<i32> {
    let path = generate_path(label as usize);
    return path.iter().map(|l| *l as i32).collect();
}

pub fn generate_path(label: usize) -> Vec<usize> {
    if 1 == label {
        return vec![1];
    }

    let mut vec = vec![];
    let mut l = label;
    loop {
        vec.insert(0, l);
        l = get_parent_label(l);
        if 1 == l {
            vec.insert(0, 1);
            break;
        }
    }

    return vec;
}

pub fn count_used_bits(num: usize) -> usize {
    let sizeof_usize = std::mem::size_of::<usize>();
    let leading_zeros = (num as usize).leading_zeros() as usize;

    return sizeof_usize * 8 - leading_zeros;
}

#[allow(dead_code)]
fn get_row_separate_label(row: usize) -> usize {
    let row_start = 2usize.pow(row as u32);
    return row_start + row_start / 2;
}

fn get_parent_label(label: usize) -> usize {
    let row = count_used_bits(label) - 1;
    let row_start = 2usize.pow(row as u32);
    let index_of_row = label - row_start;

    let parent_row_start = 2usize.pow(row as u32 - 1);
    let parent_index_max = row_start - parent_row_start - 1;
    let parent_index = parent_index_max - index_of_row / 2;

    return parent_row_start + parent_index;
}

#[cfg(test)]
mod tests {
    use std::sync::{Once};
    use crate::path_in_zigzag_labelled_binary_tree::*;

    static INIT: Once = Once::new();

    /// Setup function that is only run once, even if called multiple times.
    fn setup_test() {
        INIT.call_once(|| {
            let _ = env_logger::builder().is_test(true).try_init();
        });
    }

    #[test]
    fn test_count_used_bits() {
        setup_test();

        assert_eq!(count_used_bits(0b0000_0000_0000_0000_0000_0000_0000_0000), 0);
        assert_eq!(count_used_bits(0b1111_1111_1111_1111_1111_1111_1111_1111), 32);

        assert_eq!(count_used_bits(0b1111_1111), 8);
        assert_eq!(count_used_bits(0b1101_1111), 8);
        assert_eq!(count_used_bits(0b1101_1110), 8);

        assert_eq!(count_used_bits(0b0111_1111), 7);
        assert_eq!(count_used_bits(0b0011_1111), 6);
        assert_eq!(count_used_bits(0b0001_1111), 5);

        assert_eq!(count_used_bits(0b1111), 4);
        assert_eq!(count_used_bits(0b0111), 3);
        assert_eq!(count_used_bits(0b0011), 2);
        assert_eq!(count_used_bits(0b0010), 2);
        assert_eq!(count_used_bits(0b0001), 1);
    }

    #[test]
    fn test_get_row_separate_label() {
        setup_test();

        assert_eq!(get_row_separate_label(2), 6);
        assert_eq!(get_row_separate_label(3), 12);
        assert_eq!(get_row_separate_label(5), 48);
    }

    #[test]
    fn test_get_parent_label() {
        setup_test();

        assert_eq!(get_parent_label(11), 6);
        assert_eq!(get_parent_label(10), 6);
        assert_eq!(get_parent_label(9), 7);
        assert_eq!(get_parent_label(8), 7);

        assert_eq!(get_parent_label(21), 13);
        assert_eq!(get_parent_label(22), 12);
    }

    #[test]
    fn test_generate_path() {
        setup_test();

        assert_eq!(generate_path(14), [1, 3, 4, 14]);
        assert_eq!(generate_path(14), [1, 3, 4, 14]);
        assert_eq!(generate_path(26), [1, 2, 6, 10, 26]);

        assert_eq!(generate_path(1), [1]);

        assert_eq!(generate_path(13), [1, 3, 5, 13]);
        assert_eq!(generate_path(9), [1, 2, 7, 9]);

        assert_eq!(generate_path(69), [1, 3, 4, 15, 17, 61, 69]);

        let max_label_vec = generate_path(10usize.pow(6) as usize);
        let mut max_label_vec_str = vec![];
        for v in max_label_vec {
            max_label_vec_str.push(v.to_string())
        }
        log::debug!("10^6={}", max_label_vec_str.join(","));
    }
}
