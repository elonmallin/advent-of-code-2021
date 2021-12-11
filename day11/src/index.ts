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
    renderer.queueRender(input, totFlashCount + flashCount);

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
        // console.log(input.reduce((acc, n) => acc + n.join('')+'\r\n', ''));
        // debugger;
    }

    renderer.startAnimating();

    return flashCount;
}

console.log(solvePart1(input));
