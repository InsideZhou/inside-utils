#!/usr/bin/env python
# https://leetcode.cn/problems/container-with-most-water/

import unittest
from typing import List


def max_area(height: List[int]) -> int:
    """
    全遍历：
        左边界逐次右移，每次移动后进入运算。
    运算过程：
        右边界逐次向左靠拢。
    剪枝：
        左边界右移时，剪去不必要的进入。
        右边界移动时，剪去不必要的靠拢，中途就可以停止。
    """

    height_len = len(height)

    if height_len <= 1:
        raise ValueError

    left, right = 0, height_len - 1
    container_height = min(height[left], height[right])
    result = container_height * (height_len - 1)
    while left < right:
        left_height = height[left]

        if left_height > container_height:
            while right > left:
                right_height = height[right]
                if right_height > container_height:
                    container_height = min(left_height, right_height)
                    result = max(result, container_height * (right - left))

                    if right_height >= left_height:
                        break

                right -= 1

        left += 1

    return result


def max_area_2(height: List[int]) -> int:
    """
    双边界轮流向内遍历，左右边界比较，每次都移动较短的边界。
    关键要证明：为什么必定是移动较短的边界。
    因为容器的高度已经被较短的边界限定，而每次移动都意味着容器的宽在缩短，所以移动较长的边界时，不可能得到更大的容器。
    """
    left, right, container_height, container_area = 0, len(height) - 1, 0, 0

    while left < right:
        left_height, right_height = height[left], height[right]

        if left_height < container_height:
            left += 1
        elif right_height < container_height:
            right -= 1
        elif left_height < right_height:
            container_height = left_height
            container_area = max(container_area, container_height * (right - left))
            left += 1
        else:
            container_height = right_height
            container_area = max(container_area, container_height * (right - left))
            right -= 1

    return container_area


class TestContainerWithMostWater(unittest.TestCase):
    def testBasic(self):
        self.assertEqual(2, max_area([1, 2, 1]))
        self.assertEqual(2, max_area_2([1, 2, 1]))

    def testStandard(self):
        self.assertEqual(49, max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
        self.assertEqual(49, max_area_2([1, 8, 6, 2, 5, 4, 8, 3, 7]))

    def testPyramid(self):
        top = 1000
        left = [i for i in range(top)]
        right = left[::-1]

        self.assertEqual(500000, max_area(left + [top] + right))
        self.assertEqual(500000, max_area_2(left + [top] + right))


if __name__ == "__main__":
    unittest.main()
