#!/usr/bin/env node

const args = process.argv.slice(2);


try{
    args.map(Number);
}catch(e){
    if(e instanceof TypeError){
        console.log(e);
        exit;
    }
}

console.log(args.sort(function (a, b) {return b - a})[1]);
