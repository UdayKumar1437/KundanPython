const element = document.getElementById("name")
// element.innerHTML = "<p>Kundan</p>"
const element1 = document.getElementById("uday")
// element1.style.color = "red"
// const element = document.getElementsByTagName("h1")
// const element = document.getElementsByClassName("myname")[0]
const anc = document.getElementsByTagName("a")[0]
// Element.style.property = value
element.style.color = "blue"

element1.setAttribute("class", "uday1")

element1.className = "kundan"
anc.href = "https://www.udaykumar.tech"
// console.log(element1);


const newH1 = document.createElement("h1")
const newP = document.createElement("p")
const udayP = document.createElement("p")
udayP.innerText = "Uday Kumar"
newP.innerText = "Kundan H1 tag"
newH1.appendChild(newP)
newH1.replaceChild(udayP, newP)
const body = document.getElementsByTagName("body")[0]
body.appendChild(newH1)
// body.removeChild(newH1)

const list = document.createElement("ul")
const l1 = document.createElement("li")
const l2 = document.createElement("li")
l2.innerText = "list 2"
l1.innerText = "List 1"
list.appendChild(l1)
list.appendChild(l2)

body.appendChild(list)

// console.log(newH1);


const uday = document.querySelector("#ptag #idtag p")

console.log(uday);



const button = document.getElementsByTagName("button")[0]
// button.addEventListener("click",()=>
// {
//     alert("ok")
// })

button.addEventListener("mouseover",()=>
{
    button.style.backgroundColor = "yellow"
    button.style.cursor = "pointer"
}
)

button.addEventListener("mouseout",()=>
{
    button.style.backgroundColor = ""
}
)

button.addEventListener("dblclick",()=>
{
    alert("Kundanika")
})

const inp = document.getElementsByTagName("input")[0]
inp.addEventListener("change",(event)=>
{
    console.log(event.target.value);
    
})

inp.addEventListener("keypress",()=>
{
    console.log("kundan");
    
})