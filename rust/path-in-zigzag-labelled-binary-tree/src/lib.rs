#[cfg(test)]
mod path_in_zigzag_labelled_binary_tree {
    pub fn generate_path(label: i32) -> Vec<i32> {
        if 1 == label {
            return vec![1];
        } else if label < 1 {
            return vec![];
        }

        return vec![1];
    }

    pub fn count_bits(num: u32) -> u8 {
        return (32 - num.leading_zeros()) as u8;
    }

    #[test]
    fn test_count_bits() {
        assert_eq!(count_bits(0b0000_0000_0000_0000_0000_0000_0000_0000), 0);
        assert_eq!(count_bits(0b1111_1111_1111_1111_1111_1111_1111_1111), 32);

        assert_eq!(count_bits(0b1111_1111), 8);
        assert_eq!(count_bits(0b0111_1111), 7);
        assert_eq!(count_bits(0b0011_1111), 6);
        assert_eq!(count_bits(0b0001_1111), 5);

        assert_eq!(count_bits(0b1111), 4);
        assert_eq!(count_bits(0b0111), 3);
        assert_eq!(count_bits(0b0011), 2);
        assert_eq!(count_bits(0b0001), 1);
    }
}
