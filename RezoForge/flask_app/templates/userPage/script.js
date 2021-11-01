function flike(number) {
    let likesCountInput = document.getElementById("likesCount" + number).innerHTML;
    likesCountInput++;
    document.getElementById("likesCount"+ number).innerHTML = likesCountInput;
}