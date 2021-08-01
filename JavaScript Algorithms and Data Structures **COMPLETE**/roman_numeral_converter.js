function convertToRoman(num) {
    var thousands = ["", "M", "MM", "MMM"]
    var hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    var tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC",]
    var ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    var n = String(num)
    var T = thousands[(n[n.length -4])]
    var H = hundreds[(n[n.length -3])]
    var t = tens[(n[n.length -2])]
    var O = ones[(n[n.length -1])]
    if (n.length == 4){
        return T+H+t+O
    }else if (n.length == 3){
        return H+t+O
    }else if (n.length == 2){
        return t+O
    }else if (n.length == 1){
        return O
    }
}

convertToRoman(36);