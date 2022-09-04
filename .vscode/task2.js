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

console.log(solution(
    "1110101011011000011011010111011011010101101110101110110101010101010110101110111101110111001010101000110101010110110101010111111011001101101011101110110110110101110100011101111101101101001001010101010101001010101010100101010010001111010110100011"
));



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
