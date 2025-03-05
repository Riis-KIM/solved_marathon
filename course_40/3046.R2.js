const input = require('fs')
.readFileSync(process.platform === "linux" ? "/dev/stdin" : "./JSinput/3046.txt")
.toString()
.trim()
.split(" ")
.map(Number);
// input의 1번은 R1, 2번은 S, (R1+R2)/2=S

console.log((input[1] * 2)-input[0])