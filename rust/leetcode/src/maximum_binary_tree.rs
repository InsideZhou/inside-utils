// https://leetcode.cn/problems/maximum-binary-tree/


use std::rc::Rc;
use std::cell::RefCell;

pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}

pub fn construct_maximum_binary_tree(nums: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
    if 0 == nums.len() {
        panic!("nums length must >= 1")
    }

    return None;
}

#[cfg(test)]
mod tests {
    use std::sync::Once;

    use crate::maximum_binary_tree::*;

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
    }
}
