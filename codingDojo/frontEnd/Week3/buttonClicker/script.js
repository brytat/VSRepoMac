//Liking stuff function
var num = 0;

function flike(element) {
    num++;
    element.innerText = `${num} likes`;
    console.log("You clicked the like button " + element.innerText + " times!");
    window.alert ('Ninja was liked');
}

function fhide(element) {
    element.remove();
    console.log("The Add Definition has been hidden")
}

function logInOut(element) {
    if(element.innerText == "Login") {
        element.innerText = "Logout";
    } else {
        element.innerText = "Login";
    }
}