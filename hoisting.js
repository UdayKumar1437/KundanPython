



// // getName();
// // console.log(x);

// // var x = 7;
// // console.log(x);

// // var getName=()=> {
// //     console.log("Kundan");

// // }



// // var x = 1
// // a()
// // b()
// // console.log(x);

// // function a() {
// //     var x = 10;
// //     console.log(x);

// // }

// // function b() {
// //     var x = 100;
// //     console.log(x);

// // }


// // console.log(a);
// // var a =10 ;

// // if (a===undefined)
// // {
// //     console.log("a is undefined");

// // }
// // else{
// //     console.log("a is not defined");

// // }


// // var b =100
// // function a()
// // {
// //     var b = 10;
// //     c()
// //     function c()
// //     {
// //         // console.log(a);

// //         // var b = 1000
// //         d()
// //         function d()
// //         {
// //             console.log(b);
// //         }
// //         console.log(b);
// //     }   
// // }
// // a()

// // console.log(b);
// // Temporal Dead Zone
// // let a = 10
// // const b = 200
// // console.log(a);



// // var b = 200


// // {
// //     const a = 10
// //     var b = 100
// //     console.log(a);

// // }
// // console.log(b);

// // if(true)
// // {
// //     console.log("Kundanika");
// //     console.log("Uday");

// // }

// // let b = 100
// // {
// //     var a = 10
// //     let b = 20
// //     const c = 30
// //     console.log(a);
// //     console.log(b);
// //     console.log(c);
// // }

// // console.log(b);
// // // console.log(b);
// // // console.log(c);
// // for(let i = 0;i<=10;i++)
// // {
// //     console.log(i);

// // }


// // setTimeout(()=>
// // {
// // //    window.location.reload()

// // },1000)

// // let a = 1

// // setInterval(() => {
// // a +=1
// //     console.log(a);

// // }, 1000);



// // function x() {
// //     var a = 10

// //     return function y() {
// //         console.log(a);
// //     }
// // }

// // var z = x()
// // console.log(z);
// // z()


// // function x() {
// //     for (let i = 1; i <= 5; i++) {
// //         setTimeout(function () {
// //             console.log(i);

// //         }, i * 1000)
// //     }

// //     console.log("Kundanika Madireddy");

// // }

// // x()



// // Function Statement
// // a()
// // b()
// function a() {
//     console.log("a called");
// }
// a()

// // Function Expression aka Function Declarations

// var b = function (param1, param2) {
//     param1()
//     param2()
//     // console.log("b Called", param1, param2);

// }
// b(a, function () {
//     console.log("Kundan");

// })

// // arrow function
// var a = ()=>
// {

// }

// //  Anonymous Function

// // function ()
// // {

// // }


// setTimeout(() => {
//     console.log("Kundanika",Date.now());

// }, 10000);

// setTimeout(() => {
//     console.log("Uday");
    
// }, 2000);
// Could be GET or POST/PUT/PATCH/DELETE
// fetch('http://localhost:3001/test')
// .then(res => res.json())
// .then(console.log);

// /* { status: 'ok', method: 'GET' } */
// // Could be GET or POST/PUT/PATCH/DELETE
// fetch('https://dummyjson.com/test')
// .then(res => res.json())
// .then(console.log);

/* { status: 'ok', method: 'GET' } */


// Higher Order Functions
// function x()
// {
//     console.log("Kundan");
// }

// function y(x)
// {
//     x()
// }

// y(x)


const radius = [3,1,2,4]

const area = (radius)=>
{
    return Math.PI*radius*radius
}

const circumference = (radius)=>
{
    return 2*Math.PI*radius
}

const diameter = (radius)=>
{
    return 2*radius
}

function calculate(radius,logic)
{
    const output = []
    for (let rad of radius)
    {
        output.push(logic(rad))
    }
    return output
}
console.log(calculate(radius,area));
console.log(calculate(radius,circumference));
console.log(calculate(radius,diameter));




const calculateArea = (radius) =>
{
    const output = []
    for (let rad of radius)
    {
        output.push(Math.PI*rad*rad)
    }
    return output
}

console.log(calculateArea(radius));

// const calculateCircumference = (radius)=>
// {
//     const output = []
//     for (let rad of radius)
//     {
//         output.push(2*Math.PI*rad)
//     }
//     return output
// }
// console.log(calculateCircumference(radius));

// const calculateDiameter = (radius)=>
// {
//     const output = []
//     for (let rad of radius)
//     {
//         output.push(2*rad)
//     }
//     return output
// }
// console.log(calculateDiameter(radius));