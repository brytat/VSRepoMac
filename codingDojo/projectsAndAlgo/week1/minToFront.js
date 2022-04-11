var myArr = [2,3,1,5,4]; 

function minToFront(arr) {
    var minNum = arr[0];
    for (var i = arr.length; i > 0; i--) {
        if (arr[i] < arr[i-1]) {
            minIdx = i;
            minNum = arr[i];
        }
    }

    delete arr[minIdx];

    var temp1 = arr[0];
    var temp2 = arr[1];
    for (var i = 0; i < arr.length && temp1 != undefined; i++) {
        arr[i+1] = temp1;
        temp1 = temp2;
        temp2 = arr[i+2];
    }
    arr[0] = minNum;
    console.log(arr);

}

minToFront(myArr)