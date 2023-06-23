

function padLeft(padding:string|number, input:string):string{
    if(typeof padding === "string"){
        return padding + input
    }else{
        return String(padding) + input
    }
}

console.log(padLeft(100,'px'))