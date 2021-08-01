function palindrome(str) {
    var valid = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    var naked = ""
    for (var letter of str){
        if (valid.indexOf(letter) > -1)
            naked += letter
    }
    var check = (naked.toUpperCase())
    var rev = check.split("").reverse().join("")
    console.log(check)
    console.log(rev)
    if (check == rev){
        return true
    }else{
        return false
    }
  }

palindrome("eye");