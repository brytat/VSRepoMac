//Mythic, Rare, Uncommon
var fiveCMDR= [0,0,0];
var fourCMDR= [0,0,0];
var threeCMDR= [2.5,12.5,15];
var twoCMDR= [4.5,12.5,26];
var oneCMDR= [0,6,0];
var allCMDR = [fiveCMDR,fourCMDR,threeCMDR,twoCMDR,oneCMDR];
var setCards = [22,77,120];
var setCMDR = [0,0,0];
// Sample Size: 144

// Foils
// FU=7
// FR=3
// FM=2

// UU=81
// UR=49
// RR=6 
// MU=5 
// MR=3

// uncommons= 223
// Rares= 79
// mythics= 10

function calcPullRate(allCMDR) {
    for (var i = 0; i < allCMDR.length; i++){
        var colorCMDR = arr[i];
        console.log(colorCMDR);
        //Mythic
        colorM=colorCMDR[0]*0.069;
        //Rare
        colorR=colorCMDR[1]*0.547;
        //Uncommon
        colorU=colorCMDR[2]*1.549;
        colorTot=colorM+colorR+colorU;
        console.log(colorTot);
    }
}
