// https://leetcode.cn/problems/maximum-binary-tree/

use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
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

    pub fn clone(&self) -> Self {
        TreeNode {
            val: self.val,
            left: self.left.clone(),
            right: self.right.clone(),
        }
    }

    pub fn rc_wrap(&self) -> Option<Rc<RefCell<TreeNode>>> {
        Some(Rc::new(RefCell::new(self.clone())))
    }

    pub fn add(mut self, val: i32) -> Self {
        if val == self.val { return self; }

        if val > self.val {
            let mut new_node = TreeNode::new(val);
            new_node.left = self.rc_wrap();
            return new_node;
        }

        let new_node = if self.right.is_some() {
            let rc = self.right.unwrap();
            let right = rc.borrow();
            right.clone().add(val)
        } else {
            TreeNode::new(val)
        };

        self.right = Some(Rc::new(RefCell::new(new_node)));

        return self;
    }

    pub fn to_vec_in_level_order(&self) -> Vec<Option<i32>> {
        let root_node = self.rc_wrap();

        let mut nums: Vec<Option<i32>> = [].to_vec();
        let mut nodes = [root_node].to_vec();

        while let Some(option) = nodes.pop() {
            if option.is_none() {
                nums.push(None);
                continue;
            }

            let rc = option.unwrap();
            let node = rc.borrow();
            nums.push(Some(node.val));

            if node.left.is_some() {
                nodes.insert(0, Some(node.left.clone().unwrap()));
            } else {
                nodes.insert(0, None)
            }

            if node.right.is_some() {
                nodes.insert(0, Some(node.right.clone().unwrap()));
            } else {
                nodes.insert(0, None)
            }

            if nodes.iter().all(|item| item.is_none()) {
                break;
            }
        }

        return nums;
    }
}

pub fn construct_maximum_binary_tree(nums: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
    if 0 == nums.len() {
        return None;
    }

    let mut node = TreeNode::new(nums[0]);
    for n in nums {
        node = node.add(n);
    }

    return Some(Rc::new(RefCell::new(node)));
}

#[cfg(test)]
mod tests {
    use std::sync::Once;

    use crate::maximum_binary_tree::construct_maximum_binary_tree;

    static INIT: Once = Once::new();

    /// Setup function that is only run once, even if called multiple times.
    fn setup_test() {
        INIT.call_once(|| {
            let _ = env_logger::builder().is_test(true).try_init();
        });
    }

    #[test]
    fn basic() {
        setup_test();

        let tree_option = construct_maximum_binary_tree([3, 2, 1, 6, 0, 5].to_vec());
        let root = tree_option.unwrap();
        let root = root.borrow().clone();

        let nums = root.to_vec_in_level_order();

        let root_left = root.left.unwrap();
        let root_left = root_left.borrow().clone();
        let root_right = root.right.unwrap();
        let root_right = root_right.borrow().clone();

        assert_eq!(root.val, 6);
        assert_eq!(root_left.val, 3);
        assert_eq!(root_right.val, 5);
        assert_eq!(nums, [Some(6), Some(3), Some(5), None, Some(2), Some(0), None, None, Some(1)]);
    }

    #[test]
    fn minimum() {
        setup_test();

        let tree_option = construct_maximum_binary_tree([3, 2, 1].to_vec());
        let root = tree_option.unwrap();
        let root = root.borrow().clone();

        let nums = root.to_vec_in_level_order();

        let root_left = root.left;
        let root_right = root.right.unwrap();
        let root_right = root_right.borrow().clone();

        assert_eq!(root.val, 3);
        assert!(root_left.is_none());
        assert_eq!(root_right.val, 2);
        assert_eq!(nums, [Some(3), None, Some(2), None, Some(1)]);
    }


    #[test]
    fn single() {
        setup_test();

        let tree_option = construct_maximum_binary_tree([3].to_vec());
        let root = tree_option.unwrap();
        let root = root.borrow().clone();

        let nums = root.to_vec_in_level_order();

        let root_left = root.left;
        let root_right = root.right;

        assert_eq!(root.val, 3);
        assert!(root_left.is_none());
        assert!(root_right.is_none());
        assert_eq!(nums, [Some(3)]);
    }
}
