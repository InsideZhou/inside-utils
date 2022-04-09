/**
 * Problem Set below:
 * Task: Implement a class named 'RangeList'
 * A pair of integers define a range, for example: [1, 5). This range includes integers: 1, 2, 3, and 4.
 * A range list is an aggregate of these ranges: [1, 5), [10, 11), [100, 201)
 *
 * NOTE: Feel free to add any extra member variables/functions you like.
 */

const InvalidRange = new Error("range should be [beginning, end], and beginning lte end");

class RangeList {
    /**
     * a range is valid or not.
     *
     * @param {Array<number>} range - Array of two integers that specify beginning(inclusive) and end(exclusive) of range.
     * @return boolean
     */
    static isRangeValid(range) {
        if (!Array.isArray(range)) {
            return false;
        }

        if (2 !== range.length) { // hardcode 2 comes from "range definition: a pair of integers define a range"
            return false;
        }

        const beginning = range[0];
        const end = range[1];

        if (beginning > end) {
            return false;
        }

        return Number.isSafeInteger(beginning) && Number.isSafeInteger(end);
    }

    /**
     * a range is empty or not, empty range looks like [10, 10].
     *
     * @param {Array<number>} range - Array of two integers that specify beginning(inclusive) and end(exclusive) of range.
     * @return boolean
     */
    static isRangeEmpty(range) {
        const beginning = range[0];
        const end = range[1];

        return beginning === end;
    }

    /**
     * merge two range into one.
     *
     * @param {Array<number>} src
     * @param {Array<number>} target
     * @return {Array<number>|boolean} if two range merged successfully, return new range, or true when src is on the left of target, false when src on the right of target.
     */
    static merge(src, target) {
        const srcBeginning = src[0];
        const srcEnd = src[1];
        const targetBeginning = target[0];
        const targetEnd = target[1];

        if (srcEnd < targetBeginning) {
            if (srcEnd + 1 === targetBeginning) {
                return [srcBeginning, targetEnd];
            }

            return true;
        }

        if (srcBeginning > targetEnd) {
            if (targetEnd + 1 === srcBeginning) {
                return [targetBeginning, srcEnd];
            }

            return false;
        }

        let beginning, end;

        if (srcBeginning > targetBeginning) {
            beginning = targetBeginning;
        }
        else {
            beginning = srcBeginning;
        }

        if (srcEnd > targetEnd) {
            end = srcEnd;
        }
        else {
            end = targetEnd;
        }

        return [beginning, end];
    }

    /**
     * Subtract range by another range.
     *
     * @param {Array<number>} minuend
     * @param {Array<number>} subtrahend
     * @return {Array<Array<number>>|boolean} true when minuend is on the left of subtrahend, false when minuend on the right of subtrahend.
     */
    static subtract(minuend, subtrahend) {
        const minuendBeginning = minuend[0];
        const minuendEnd = minuend[1];
        const subtrahendBeginning = subtrahend[0];
        const subtrahendEnd = subtrahend[1];

        if (minuendEnd <= subtrahendBeginning) {
            return true;
        }

        if (minuendBeginning >= subtrahendEnd) {
            return false;
        }

        const resultRanges = [];

        if (minuendBeginning < subtrahendBeginning) {
            resultRanges.push([minuendBeginning, subtrahendBeginning]);
        }

        if (minuendEnd > subtrahendEnd) {
            resultRanges.push([subtrahendEnd, minuendEnd]);
        }

        return resultRanges;
    }

    /**
     * @type {Array<Array<number>>}
     */
    #ranges = [];

    /**
     * Adds a range to the list.
     *
     * @param  {Array<number>} range - Array of two integers that specify beginning(inclusive) and end(exclusive) of range.
     */
    add(range) {
        if (!RangeList.isRangeValid(range)) {
            throw InvalidRange;
        }

        if (RangeList.isRangeEmpty(range)) {
            return;
        }

        let rangeInserted = false;
        let mergedItem = range;
        let newRanges = [];
        for (let i = 0; i < this.#ranges.length; i++) {
            let item = this.#ranges[i];
            let mergeResult = RangeList.merge(mergedItem, item);

            if (true === mergeResult) {
                newRanges.push(mergedItem);
                newRanges = newRanges.concat(this.#ranges.slice(i));
                rangeInserted = true;
                break;
            }
            else if (false === mergeResult) {
                newRanges.push(item);
            }
            else {
                mergedItem = mergeResult;
            }
        }

        if (!rangeInserted) {
            newRanges.push(mergedItem);
        }

        this.#ranges = newRanges;
    }

    /**
     * Removes a range from the list.
     *
     * @param {Array<number>} range - Array of two integers that specify beginning(inclusive) and end(exclusive) of range.
     */
    remove(range) {
        if (!RangeList.isRangeValid(range)) {
            throw InvalidRange;
        }

        if (RangeList.isRangeEmpty(range)) {
            return;
        }

        let newRanges = [];
        for (let i = 0; i < this.#ranges.length; i++) {
            let item = this.#ranges[i];
            let remainder = RangeList.subtract(item, range);

            if (false === remainder) {
                newRanges = newRanges.concat(this.#ranges.slice(i));
            }
            else if (true === remainder) {
                newRanges.push(item);
            }
            else {
                for (let remainderItem of remainder) {
                    newRanges.push(remainderItem);
                }
            }
        }

        this.#ranges = newRanges;
    }

    /**
     * Get Current range entry list.
     *
     * @return {Array<Array<number>>}
     */
    entries() {
        return this.#ranges.slice();
    }

    toString() {
        let result = "";
        for (let item of this.#ranges) {
            result += `[${item[0]}, ${item[1]}) `;
        }

        return result.trimEnd();
    }

    /**
     * Prints out the list of ranges in the range list.
     */
    print() {
        console.log(this.toString());
    }
}

export {InvalidRange, RangeList};
