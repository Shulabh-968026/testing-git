function padLeft(padding, input) {
    if (typeof padding === "string") {
        return padding + input;
    }
    else {
        return String(padding) + input;
    }
}
console.log(padLeft(100, 'px'));
