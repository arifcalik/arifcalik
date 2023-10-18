function sleepIn(weekday, vacation) {
    if(!weekday || vacation)
        return true;
    return false;
}

console.assert(sleepIn(false, false) == true)
console.assert(sleepIn(true, false) == false)
console.assert(sleepIn(false, true) == true)

function monkeyTrouble(aSmile, bSmile) {
    if((aSmile && bSmile) || (!aSmile && !bSmile)) {
        return true;
    }
    return false;
}

console.assert(monkeyTrouble(true, true) == true)
console.assert(monkeyTrouble(false, false) == true)
console.assert(monkeyTrouble(true, false) == false)
console.assert(monkeyTrouble(false, true) == false)

function stringTimes(str, n) {
    //return str.repeat(n);
    let res ="";
    for(let i=0; i<n; i++)
        res += str;
    return res;
}

console.assert(stringTimes("Hi", 2) == "HiHi")
console.assert(stringTimes("Hi", 3) == "HiHiHi")
console.assert(stringTimes("Hi", 1) == "Hi")
console.assert(stringTimes("ab cd", 2) == "ab cdab cd")
console.assert(stringTimes("a", 0) == "")

function luckySum(a, b, c){
    const UNLUCKY = 13;

    let sum = 0;
    if (a != UNLUCKY)
        sum += a;
    else return sum;
    if (b != UNLUCKY)
        sum += b;
    else return sum;
    if (c != UNLUCKY)
        sum += c;
    else return sum;
    return sum;
}

console.assert(luckySum(1, 2, 3) == 6)
console.assert(luckySum(1, 2, 13) == 3)
console.assert(luckySum(1, 13, 3) == 1)
console.assert(luckySum(13, 103, 3) == 0)
console.assert(luckySum(-1, -7, 3) == -5)

function caught_speeding(speed, is_birthday){
    if((is_birthday && speed <= 65) || speed <= 60)
        return 0;
    else if ((is_birthday && speed <= 85) || speed <= 80)
        return 1;
    else    
        return 2;
}

console.assert(caught_speeding(60, false) == 0)
console.assert(caught_speeding(65, false) == 1)
console.assert(caught_speeding(65, true) == 0)
console.assert(caught_speeding(85, true) == 1)
console.assert(caught_speeding(80, false) == 1)
console.assert(caught_speeding(81, false) == 2)