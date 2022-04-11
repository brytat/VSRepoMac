var myArr = [1,2,3,4,5]; 

function pushFront(arr, val) {
    var temp1 = arr[0];
    var temp2 = arr[1];
    for (var i = 0; i < arr.length && temp1 != undefined; i++) {
        arr[i+1] = temp1;
        temp1 = temp2;
        temp2 = arr[i+2];
    }
    arr[0] = val;
}

pushFront(myArr, 0)

console.log(myArr);

function popFront(arr) {
    var returnVal = arr[0];
    for (var i = 1; i < arr.length; i++) {
        arr[i-1] = arr[i];
    }
    arr.pop();
    return returnVal;
}

function insertAt(arr, val, ind) {
    for (var i = arr.length - 1; i >= ind; i--) {
        arr[i+1] = arr[i];
    }
    arr[ind] = val;
}