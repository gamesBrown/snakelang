coins = {
    "q":[0,25],
    "d":[0,10],
    "n":[0,5],
    "p":[0,1]
}
//coins object with key value pair of arrays where array[0] is amount of coin and array[1] is value of coin

num = 63

for (property in coins){

    coins[property][0]=Math.floor(num/coins[property][1])
    num = num%coins[property][1]
    console.log(`${coins['q'][0]},${coins['d'][0]},${coins['n'][0]},${coins['p'][0]}`)
    
    
    
}

