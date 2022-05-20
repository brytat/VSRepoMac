//Mythic, Rare, Uncommon
var fiveCMDR= [0,0,0];
var fourCMDR= [0,0,0];
var threeCMDR= [2.5,12.5,15];
var twoCMDR= [4.5,12.5,26];
var oneCMDR= [0,6,0];
var zeroCMDR= [0,0,0];
var allCMDR = [zeroCMDR, oneCMDR,twoCMDR,threeCMDR,fourCMDR,fiveCMDR];
//all card in set ("normal")
var setCards = [22,77,120];
//all commanders in set
var setCMDR = [0,0,0];
var foilTwoCMDR = [16.5,12.5,25];
var foilThreeCMDR = [19.5,2.5,15];
var foilFourCMDR = [8,0,0]
// Sample Size: 144

// Foils
// FU=7
// FR=3
// FM=2 Maybe one of these was a 2C partner commander or a 5 color? this is negligable

//legendary slot distribution
// UU=81
// UR=49
// RR=6 
// MU=5 
// MR=3

//card pull totals over all samples
// uncommons= 223
// Rares= 79
// mythics= 10

//Each pack has an average of 2.16 commanders

function calcPullRate(allCMDR) {
    for (var i = 0; i < allCMDR.length; i++){
        var colorCMDR = allCMDR[i];
        console.log(colorCMDR);
        //Mythic
        colorM=colorCMDR[0]*0.069;
        //Rare
        colorR=colorCMDR[1]*0.547;
        //Uncommon
        colorU=colorCMDR[2]*1.549;
        colorTot=colorM+colorR+colorU;
        console.log("Rarity index for color: " + i + ", is: " + colorTot);
    }
}

calcPullRate(allCMDR);
