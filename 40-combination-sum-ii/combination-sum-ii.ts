function combinationSum2(candidates: number[], target: number): number[][] {
    candidates.sort((a, b) => a - b);
    let answer: number[][] = [];

    function backtracker(arr: number[], start: number, currentSum: number) {
        if (currentSum === target) {
            answer.push([...arr]);
            return;
        }

        for (let i = start; i < candidates.length; i++) {
            let sum = currentSum + candidates[i];
            if ((i === start || candidates[i - 1] != candidates[i]) && sum <= target) {
                arr.push(candidates[i]);
                backtracker([...arr], i + 1, sum);
                arr.pop();
            }
        }
    }

    backtracker([], 0, 0);
    return answer;
};