var validCodeLocal = ["###-###-####","(###)###-####","(###)_###-####","###_###_####","##########"]
var validCodeInternational = ["#_###-###-####","#_(###)_###-####","#(###)###-####", "#_###_###_####"]
var valid = " -()123456789"
var num = "0123456789"
var nonum = "-()"
var char
function telephoneCheck(str) {
    var code = ""
    for (char of str){
        if (valid.indexOf(char) == -1){
            console.log("\n"+ str)
            console.log(code)
            console.log("invalid characters")
            return false
        }else if (num.indexOf(char) > -1){
            code += "#"
        }else if (char == " "){
            code += "_"
        }else if (nonum.indexOf(char) > -1){
            code += char
        }
    }
    if (validCodeLocal.indexOf(code) == -1 && validCodeInternational.indexOf(code) == -1){
        console.log("\n" + str)
        console.log(code)
        console.log("invalid formating")
        return false
    }else if(validCodeInternational.indexOf(code) > -1 && str[0] != "1"){
        console.log("\n" + str)
        console.log(code)
        console.log("Invalid country code : " + str[0])
        return false
    }
    console.log(code)
  return true;
}
telephoneCheck("555-555-5555");