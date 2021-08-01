const dValue = [10000 , 2000 , 1000 , 500 , 100 , 25 , 10 , 5 , 1]
function checkCashRegister(price, cash, cid) {
    let changerev = [["PENNY", 0], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]];
    let change = changerev.reverse()
    let cidfix = cid.reverse()
    let refund = cash*100 - price*100
    for (var denomination in cidfix){
        cidfix[denomination][1] *= 100
    }

    if (refund < 0){
        console.log({status: "INSUFFICIENT_FUNDS", change: []})
        return {status: "INSUFFICIENT_FUNDS", change: []}
    }
    if (refund == 0){
        console.log({status: "INSUFFICIENT_FUNDS", change: []})
        return {status: "INSUFFICIENT_FUNDS", change: []}
    }

    for (var denomination in cidfix){
        while (refund >= dValue[denomination] && cidfix[denomination][1] >= dValue[denomination]){
            cidfix[denomination][1] -= dValue[denomination]
            change[denomination][1] += dValue[denomination]
            refund -= dValue[denomination]
        }
    }

    for (var denomination in change){
        change[denomination][1] /= 100
    }

    if (refund > 0){
        console.log({status: "INSUFFICIENT_FUNDS", change: []})
        return {status: "INSUFFICIENT_FUNDS", change: []}
    return change;
    }

    if (change[8][1] > 0 && change[7][1] == 0 && change[6][1] == 0 && change[5][1] == 0 && change[4][1] == 0 && change[3][1] == 0 && change[2][1] == 0 && change[1][1] == 0 && change[0][1] == 0) {
        let specchange = change.reverse()
        console.log({status: "CLOSED", change: specchange})
        return {status: "CLOSED", change: specchange}
    }

    for (var denomination in change){
        if (change[denomination][1] == 0) {
            change.splice(denomination,1)
        }
    }
    for (var denomination in change){
        if (change[denomination][1] == 0) {
            change.splice(denomination,1)
        }
    }
    for (var denomination in change){
        if (change[denomination][1] == 0) {
            change.splice(denomination,1)
        }
    }

    console.log({status: "OPEN", change: change})
    return {status: "OPEN", change: change}
  }

checkCashRegister(19.5, 20, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]);