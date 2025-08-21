let button = document.getElementById("button");
let body = document.getElementById("body");
let close = document.getElementById("close");

console.log(button) ;
console.log(body) ;
console.log(close) ;

// button.addEventListener("click",()=>{
//     body.classList.toggle("bodychang");
// })


button.addEventListener("click",()=>{
    body.classList.toggle("bodychang");
})


close.addEventListener("click",function(){
    body.classList.remove("bodychang");
})
