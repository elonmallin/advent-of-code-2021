import data from './input.txt'
import * as renderer from './renderer'

const input = data.trim().split('\n').map(x => x.trim().split('').map(x => parseInt(x)));

function inc(x: number, y: number, input: Array<Array<number>>, flashMemo: any, totFlashCount: number): number {
    let flashCount = 0;

    const flashKey = `${x}:${y}`;

    if (flashMemo[flashKey]) {
        return 0;
    }

    input[y][x]++;
    renderer.queueRender(input, totFlashCount + flashCount, 0);

    const colLen = input.length;
    const rowLen = input[0].length;

    if (input[y][x] > 9) {
        input[y][x] = 0;
        flashCount++;
        flashMemo[flashKey] = 1;
        
        const adjacents = [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]
        for (const adjacent of adjacents) {
            if (x + adjacent[0] < 0 || x + adjacent[0] >= rowLen || y + adjacent[1] < 0 || y + adjacent[1] >= colLen) {
                continue; // Out of range
            }

            flashCount += inc(x + adjacent[0], y + adjacent[1], input, flashMemo, totFlashCount + flashCount);
        }
    }

    return flashCount;
}

function solvePart1(input: Array<Array<number>>): number {
    renderer.setup(input);

    let flashCount = 0;

    for (let i = 0; i < 100; ++i) {
        const flashMemo = {};
        for (let y = 0; y < input.length; y++) {
            for (let x = 0; x < input[0].length; x++) {
                flashCount += inc(x, y, input, flashMemo, flashCount);
            }
        }
    }

    renderer.startAnimating();

    return flashCount;
}

function inc2(x: number, y: number, input: Array<Array<number>>, flashMemo: any, totFlashCount: number, step: number): number {
    let flashCount = 0;

    const flashKey = `${x}:${y}`;

    if (flashMemo[flashKey]) {
        return 0;
    }

    input[y][x]++;
    renderer.queueRender(input, totFlashCount + flashCount, step);

    const colLen = input.length;
    const rowLen = input[0].length;

    if (input[y][x] > 9) {
        input[y][x] = 0;
        flashCount++;
        flashMemo[flashKey] = 1;

        // Part 2 start
        const allInSync = input.reduce((acc, rows) => acc.concat(rows), []).reduce((acc, n) => acc && n == 0, true)
        if (allInSync) {
            return -1;
        }
        // Part 2 end
        
        const adjacents = [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]
        for (const adjacent of adjacents) {
            if (x + adjacent[0] < 0 || x + adjacent[0] >= rowLen || y + adjacent[1] < 0 || y + adjacent[1] >= colLen) {
                continue; // Out of range
            }

            let incRes = inc2(x + adjacent[0], y + adjacent[1], input, flashMemo, totFlashCount + flashCount, step);
            if (incRes == -1) {
                return -1;
            }

            flashCount += incRes;
        }
    }

    return flashCount;
}

function solvePart2(input: Array<Array<number>>): number {
    renderer.setup(input);

    let syncIdx = -1;
    let flashCount = 0;

    for (let i = 0; i < 1000; ++i) {
        const flashMemo = {};
        for (let y = 0; y < input.length; y++) {
            for (let x = 0; x < input[0].length; x++) {
                const incRes = inc2(x, y, input, flashMemo, flashCount, i);
                if (incRes == -1) {
                    syncIdx = i;
                    i = y = x = Infinity;
                    break;
                }

                flashCount += incRes;
            }
        }
    }

    renderer.startAnimating();

    return syncIdx + 1;
}

// console.log(solvePart1(input));
console.log(solvePart2(input));
