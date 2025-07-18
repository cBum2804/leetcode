function combinationSum(candidates: number[], target: number): number[][] {
    const result: number[][] = [];

    function backtrack(start: number, target: number, path: number[]) {
        if (target === 0) {
            result.push([...path]);  // push a copy of the path
            return;
        }
        if (target < 0) return;

        for (let i = start; i < candidates.length; i++) {
            path.push(candidates[i]);
            backtrack(i, target - candidates[i], path);
            path.pop();  // backtrack
        }
    }

    candidates.sort((a, b) => a - b);  // optional for optimization
    backtrack(0, target, []);

    return result;
};
