// function sum(x, y, z) {
//   return x + y + z;
// }

// const numbers = [1, 2, 3];

// console.log(sum(numbers[0],numbers[1],numbers[2]));
// console.log(sum(12,...numbers));

// // Expected output: 6

// console.log(...numbers);


// const num1 = [1,2,3]
// const num2 = [4,5,6]
// // console.log(num1.concat(num2));
// console.log([...num1,...num2]);



// const numbers = [1,2,3,4,5,6]
// const [one,two,...rest] = numbers;
// console.log(rest);

// const obj = {
//     name:"uday"
// }
// const obj1 = {
//     name1:"kundan"
// }

// const ans = {...obj,...obj1}
// console.log(ans);



// function sum(a,...rest){
//     ans = 0
//     for(let i of rest)
//     {
//         ans+=i
//     }
//     return ans
// }

// console.log(sum(1,2));


// console.log(sum(1,2,3));



// const obj = {
//     name1:"Kundanika",
//     age:19,
//     friend :"Uday Kumar",
//     dad:{
//         name:"Dinesh"
//     }
// }

// console.log(obj?.dad?.name); // Optional Chaining


// // const name = obj.name
// // const age = obj.age
// // const friend = obj.friend

// const {name1,age,friend} = obj // Destructering
// console.log(name1,age,friend);



const url = "http://localhost:3001/kundan"
// async function fetchUsersData()
// {
//     const res = await fetch(url)
//     // console.log(res);
    
//     const data  = await res.json()
//     console.log(data);
    

// }

// fetchUsersData()

const res = fetch(url).then(res=>res.json()).then(res=>console.log(res));
