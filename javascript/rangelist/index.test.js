import {InvalidRange, RangeList} from "./index.js";


test("invalid range parameter will throws InvalidRange", () => {
    const rangeList = new RangeList();

    expect(() => {
        rangeList.add(null);
    }).toThrow(InvalidRange);

    expect(() => {
        rangeList.add([]);
    }).toThrow(InvalidRange);

    expect(() => {
        rangeList.add([1]);
    }).toThrow(InvalidRange);

    expect(() => {
        rangeList.add([1, 2, 3]);
    }).toThrow(InvalidRange);

    expect(() => {
        rangeList.add([3, 2]);
    }).toThrow(InvalidRange);
});

test("range is empty", () => {
    expect(RangeList.isRangeEmpty([10, 10])).toBeTruthy();
    expect(RangeList.isRangeEmpty([10, 11])).toBeFalsy();
});

test("ranges merging", () => {
    expect(RangeList.merge([1, 2], [5, 6])).toBeTruthy();
    expect(RangeList.merge([9, 10], [5, 6])).toBeFalsy();

    expect(RangeList.merge([5, 17], [9, 10])).toEqual([5, 17]);
    expect(RangeList.merge([9, 10], [5, 17])).toEqual([5, 17]);

    expect(RangeList.merge([2, 3], [4, 5])).toEqual([2, 5]);
    expect(RangeList.merge([2, 4], [4, 5])).toEqual([2, 5]);
    expect(RangeList.merge([2, 5], [4, 5])).toEqual([2, 5]);
    expect(RangeList.merge([2, 6], [4, 5])).toEqual([2, 6]);
    expect(RangeList.merge([1, 2], [4, 5])).toBeTruthy();

    expect(RangeList.merge([5, 11], [3, 4])).toEqual([3, 11]);
    expect(RangeList.merge([4, 11], [3, 4])).toEqual([3, 11]);
    expect(RangeList.merge([3, 11], [3, 4])).toEqual([3, 11]);
    expect(RangeList.merge([2, 11], [3, 4])).toEqual([2, 11]);
    expect(RangeList.merge([6, 11], [3, 4])).toBeFalsy();
});

test("add range to list", () => {
    const rangeList = new RangeList();

    rangeList.add([13, 14]);
    expect(rangeList.entries()).toEqual([[13, 14]]);

    rangeList.add([12, 13]);
    expect(rangeList.entries()).toEqual([[12, 14]]);

    rangeList.add([13, 15]);
    expect(rangeList.entries()).toEqual([[12, 15]]);

    rangeList.add([11, 11]);
    expect(rangeList.entries()).toEqual([[12, 15]]);

    rangeList.add([16, 16]);
    expect(rangeList.entries()).toEqual([[12, 15]]);

    rangeList.add([7, 8]);
    expect(rangeList.entries()).toEqual([[7, 8], [12, 15]]);

    rangeList.add([21, 25]);
    expect(rangeList.entries()).toEqual([[7, 8], [12, 15], [21, 25]]);

    rangeList.add([11, 15]);
    expect(rangeList.entries()).toEqual([[7, 8], [11, 15], [21, 25]]);

    rangeList.add([11, 16]);
    expect(rangeList.entries()).toEqual([[7, 8], [11, 16], [21, 25]]);

    rangeList.add([10, 17]);
    expect(rangeList.entries()).toEqual([[7, 8], [10, 17], [21, 25]]);

    rangeList.add([6, 9]);
    expect(rangeList.entries()).toEqual([[6, 17], [21, 25]]);

    rangeList.add([27, 29]);
    expect(rangeList.entries()).toEqual([[6, 17], [21, 25], [27, 29]]);

    rangeList.add([24, 26]);
    expect(rangeList.entries()).toEqual([[6, 17], [21, 29]]);

    rangeList.add([8, 23]);
    expect(rangeList.entries()).toEqual([[6, 29]]);
});

test("range subtraction", () => {
    expect(RangeList.subtract([23, 30], [40, 44])).toBeTruthy();
    expect(RangeList.subtract([23, 30], [8, 13])).toBeFalsy();
    expect(RangeList.subtract([23, 30], [13, 44])).toEqual([]);

    expect(RangeList.subtract([1, 50], [49, 50])).toEqual([[1, 49]]);
    expect(RangeList.subtract([1, 50], [1, 3])).toEqual([[3, 50]]);
    expect(RangeList.subtract([1, 50], [13, 19])).toEqual([[1, 13], [19, 50]]);
});

test("remove range from list", () => {
    const rangeList = new RangeList();
    rangeList.add([1, 50]);
    expect(rangeList.entries()).toEqual([[1, 50]]);

    rangeList.remove([1, 3]);
    expect(rangeList.entries()).toEqual([[3, 50]]);

    rangeList.remove([45, 50]);
    expect(rangeList.entries()).toEqual([[3, 45]]);

    rangeList.remove([33, 39]);
    expect(rangeList.entries()).toEqual([[3, 33], [39, 45]]);

    rangeList.remove([25, 30]);
    expect(rangeList.entries()).toEqual([[3, 25], [30, 33], [39, 45]]);

    rangeList.remove([20, 40]);
    expect(rangeList.entries()).toEqual([[3, 20], [40, 45]]);
});

test("toString", () => {
    const rangeList = new RangeList();
    rangeList.add([1, 5]);
    expect(rangeList.toString()).toEqual("[1, 5)");
    rangeList.print();

    rangeList.add([10, 20]);
    expect(rangeList.toString()).toEqual("[1, 5) [10, 20)");
    rangeList.print();

    rangeList.add([20, 20]);
    expect(rangeList.toString()).toEqual("[1, 5) [10, 20)");
    rangeList.print();

    rangeList.add([20, 21]);
    expect(rangeList.toString()).toEqual("[1, 5) [10, 21)");
    rangeList.print();

    rangeList.add([2, 4]);
    expect(rangeList.toString()).toEqual("[1, 5) [10, 21)");
    rangeList.print();

    rangeList.add([3, 8]);
    expect(rangeList.toString()).toEqual("[1, 8) [10, 21)");
    rangeList.print();

    rangeList.remove([10, 10]);
    expect(rangeList.toString()).toEqual("[1, 8) [10, 21)");
    rangeList.print();

    rangeList.remove([10, 11]);
    expect(rangeList.toString()).toEqual("[1, 8) [11, 21)");
    rangeList.print();

    rangeList.remove([15, 17]);
    expect(rangeList.toString()).toEqual("[1, 8) [11, 15) [17, 21)");
    rangeList.print();

    rangeList.remove([3, 19]);
    expect(rangeList.toString()).toEqual("[1, 3) [19, 21)");
    rangeList.print();
});
