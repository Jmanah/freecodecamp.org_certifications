function rot13(str) {
    var ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMN"
    var ret = ""
    var char = ""
    for (char of str){
        if (ABC.indexOf(char) > -1){
            var rot = ABC.charAt(ABC.indexOf(char)+13)
            ret += rot
        }else{
            ret += char
        }
    }
    return ret;
}

rot13("SERR PBQR PNZC");