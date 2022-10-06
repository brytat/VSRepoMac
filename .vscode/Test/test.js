function solution(M, A) {
    var N = A.length;
    var count = new Array(M + 1);
    var i;
    for (i = 0; i <= M; i++)
        count[i] = 0;
    var maxOccurence = 0;
    var index = -1;
        if (count[A[i]] + 1 > 0) {
            var tmp = count[A[i]] + 1;
            if (tmp > maxOccurence) {
                maxOccurence = tmp;
                index = i;
            }
            count[A[i]] = tmp;
        } else {
            count[A[i]] = 1;
        }
    }
    return A[index];
}

console.log(solution(3, [2,3,1,3,3,1]))

console.log(solution(5, [1,2,3,4,5]))