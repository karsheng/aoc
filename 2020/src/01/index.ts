import { readFileSync } from "fs";
import { EOL } from "os";

const parseFile = (path: string) => {
    const content = readFileSync(path, 'utf8').split(EOL);
    content.pop();
    return content
}

const preprocess = (content: string[]) => {
    return content.map(c => parseInt(c));
}

const data = preprocess(parseFile("../../inputs/01/input.txt"));

const part1 = (data: number[]) => {
    const target = 2020;
    const seen = new Set<number>();

    for (let i = 0; i < data.length; i++) {
        const n = data[i];
        if (seen.has(target - n)) {
            return n * (target - n);
        }
        seen.add(n);
    }
}

console.log("p1", part1(data));

const part2 = (data: number[]) => {
    const target = 2020;

    for (let i = 0; i < data.length; i++) {
        for (let j = 0; j < data.length; j++) {
            for (let k = 0; k < data.length; k++) {
                if (data[i] + data[j] + data[k] === target)
                {
                    return data[i] * data[j] * data[k];
                }
            }
        }            
    }
}

console.log("p2", part2(data));