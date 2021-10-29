

function addOneLike(number) {
    let likesCountInput = document.querySelector("#user" + number).innerText;
    let likesNum = likesCountInput.match(/\d+/g);
    likesNum[0]++;
    document.querySelector('#user' + number).innerHTML = `${likesNum[0]} like(s)`;

    console.log("You liked user " + number + ", " + likesNum[0]+ " time(s)!");
}