
export const setup = (input: Array<Array<number>>) => {
    const cont = document.querySelector('main');

    for (let y = 0; y < input.length; y++) {
        const row = document.createElement('article');

        for (let x = 0; x < input[0].length; x++) {
            const item = document.createElement('div');
            const text = document.createElement('p');
            const num = document.createElement('p');
            num.classList.add('num');
            item.id = `${x}:${y}`;
            num.textContent = input[y][x].toString();
            text.textContent = '🦑';
            item.appendChild(text);
            item.appendChild(num);
            row.appendChild(item)
        }

        cont.appendChild(row);
    }
}

let queue: any = []
export const queueRender = (input: Array<Array<number>>, flashCount: number) => {
    queue.push([input.map(x => x.slice()).slice(), flashCount]);
}

let fpsInterval = 0;
let then = 0;
let startTime = 0;

export function startAnimating() {
    let flashCount = 0;
    console.log('before', queue.length);
    queue = queue.reduce((acc: any, n: any) => {
        if (flashCount >= n[1]) {
            return acc;
        }
        flashCount = n[1];
        acc.push(n);

        return acc;
    }, [])
    console.log('after', queue.length);

    fpsInterval = 1000 / 120;
    then = Date.now();
    startTime = then;
    animate();
}
console.log(queue.length);

function animate() {

    if (queue.length == 0) {
        return;
    }
    // request another frame

    requestAnimationFrame(animate);

    // calc elapsed time since last loop

    const now = Date.now();
    const elapsed = now - then;

    // if enough time has elapsed, draw the next frame

    // if (elapsed > fpsInterval) {

        // Get ready for next frame by setting then=now, but also adjust for your
        // specified fpsInterval not being a multiple of RAF's interval (16.7ms)
        then = now - (elapsed % fpsInterval);

        // Put your drawing code here
        render()
    // }
}

const render = () => {
    if (queue.length == 0) {
        return;
    }

    const step = queue.splice(0, 1)[0];

    const flashCountElm = document.getElementById('flash-count');
    flashCountElm.textContent = step[1].toString();

    for (let y = 0; y < step[0].length; y++) {
        for (let x = 0; x < step[0][0].length; x++) {
            const item = document.getElementById(`${x}:${y}`);
            const val = step[0][y][x];
            if (val > 9) {
                const flash = document.createElement('div');
                flash.textContent = '⚡';
                item.appendChild(flash)
                flash.classList.add('glow');
            }
            let num = item.querySelector('.num');
            num.textContent = step[0][y][x];
        }
    }
}
