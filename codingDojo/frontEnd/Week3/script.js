var arr = [2,4,6,8,-2,-5,4,9,-60]
function positiveNegative(){
    var positive = []
    var negative = []
    for(let i = 0; i< arr.length; i++){
        if(arr[i]<0){
        negative.push(arr[i])
        }
    }
    console.log(negative)
}
positiveNegative()    