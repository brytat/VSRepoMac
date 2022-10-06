function solution(1, (2, (1, None, None), (2, None, None)), (2, (4, None, None), (1, None, None))) {
    // write your code in JavaScript (Node.js 8.9.4)
    if (T == null ) {
        var path = [];
        return path;
    }
    var right = solution(T.r);
    var left = solution(T.l);
    if (right.length < left.length) {
        left.push(T.x);
        return left;
    } else {
        right.push(T.x);
        return right;
    }
}