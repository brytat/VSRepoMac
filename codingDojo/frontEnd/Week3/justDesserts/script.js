//Search popup function
function fsearch() {
    let recipeInput = document.getElementById("recipeSearch").value;
    window.alert ('You searched for "' + recipeInput + '"');
    console.log ('searched for "' + recipeInput + '"');
}

//Join button hiding function
function fhide(element) {
    element.remove();
    console.log("The join button has gone into the void! What does it mean to be nothing? What does it mean to be?")
}

//Liking stuff function
function flike(number) {
    let likesCountInput = document.getElementById("likesCount" + number).innerHTML;
    let dessertName = document.getElementById("dessertEntryName" + number).innerHTML;
    likesCountInput++;
    document.getElementById("likesCount"+ number).innerHTML = likesCountInput;
    console.log("You liked " + dessertName + " " + likesCountInput + " time(s)!"); 
}