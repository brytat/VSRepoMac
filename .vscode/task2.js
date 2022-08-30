function solution(S) {

    // write your code in JavaScript (Node.js 8.9.4)
    //convert string into int
    var V = parseInt(S, 2);
    var steps = 0;
    //check if done
    while (V > 0) {
        //check if even
        if (V % 2 == 0) {
            V /= 2;
            steps += 1;
        //if odd and over one then...
        } else {
            V = V - 1;
            steps = steps + 1;
            solution(V);
        }
    }
    return steps;
}

console.log(solution("11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"));



function solution(S) {

    // write your code in JavaScript (Node.js 8.9.4)
    //convert string into int
    var V = parseInt(S, 2);
    var steps = 0;
    //check if done
    while (V > 0) {
        //check if even
        if (V % 2 == 0) {
            V /= 2;
        //if odd and over one then...
        } else if (V != 1) {
            V -= 1;
            V /= 2;
            steps = steps + 1;
        } else {
            V -= 1;
        }
        steps += 1;
    }
    return steps;
}
