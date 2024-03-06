function fibonacci(n){
    const fib=[0,1]
    for(let i = 2; i < n; i++){
        console.log(i) //i is 2 in the first execution even though it's incremented??
        fib[i]=fib[i-1]+fib[i-2]
        console.log(fib[i])
    }
    return fib

}
console.log(fibonacci(2))//[0,1]
console.log(fibonacci(3))
console.log(fibonacci(4))
console.log(fibonacci(5))