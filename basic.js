const divBox = document.createElement("div")
const body = document.getElementsByTagName("body")[0]
const btn1 = document.createElement("button")
const btn2 = document.createElement("button")
const btn3 = document.createElement("button")
const divP = document.createElement("div")
divP.style.display = "flex"
divP.style.gap = "20px"
btn1.innerText = "Red"
btn2.innerText = "Green"
btn3.innerText = "Blue"
divBox.style.height = "200px"
divBox.style.width = "200px"
divBox.style.backgroundColor = "yellow"
body.style.display = "flex"
body.style.justifyContent = "center"
body.style.alignItems = "center"
body.style.gap = "100px"
body.style.flexDirection = "column"
body.appendChild(divBox)
body.appendChild(divP)
divP.appendChild(btn1)
divP.appendChild(btn2)
divP.appendChild(btn3)
btn1.addEventListener("click",()=>
{
    divBox.style.backgroundColor = "Red"
})
btn2.addEventListener("click",()=>
{
    divBox.style.backgroundColor = "Green"
})
btn3.addEventListener("click",()=>
{
    divBox.style.backgroundColor = "Blue"
})
const ans = document.createElement("h1")
const inp = document.createElement("input")
const btn4 = document.createElement("button")
btn4.innerText = "Submit"
body.appendChild(inp)
body.appendChild(btn4)
body.appendChild(ans)



btn4.addEventListener("click",()=>
{
    console.log(inp.value)
ans.innerText = parseInt(inp.value, 2)
})