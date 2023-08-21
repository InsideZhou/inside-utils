// https://leetcode.cn/problems/majority-element-ii/

use std::collections::HashMap;

pub fn majority_element_one_third(nums: Vec<usize>) -> Vec<usize> {
    let one_third = nums.len() / 3;
    let mut num_counts = HashMap::new();
    for num in nums {
        let count = num_counts.entry(num).or_insert(0usize);
        *count += 1;
    }

    let mut result = num_counts.iter()
        .filter(|(_, v)| **v > one_third)
        .map(|(k, _)| *k)
        .collect::<Vec<usize>>();

    result.sort();
    return result;
}

#[cfg(test)]
mod tests {
    use crate::majority_element_ii::*;

    #[test]
    fn test_majority_element_one_third() {
        assert_eq!(majority_element_one_third(vec![1usize, 1, 2, 3, 1, 4, 5, 6, 1, 1]), [1usize]);

        assert_eq!(majority_element_one_third(vec![1usize, 1, 1, 1, 2, 2, 2, 2, 3, 1, 4, 2, 2, 1, 1]), [1usize, 2]);
    }
}
