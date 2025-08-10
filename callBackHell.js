// function x()
// {
//     console.log("x");

// }

// function y(x)
// {



//     console.log("ok");
//     console.log("uday");
//     console.log("kundan");

//     x()
// }
// y(x)


// console.log("Uday Kumar");
// setTimeout(() => {
//     console.log("Dinesh");

// }, 0);

// console.log("Kundan");



// const cart = ["shoes", "pants", "jewellery"]

// api.createOrder(cart, () => {
//     api.ProceedToPayment(() => {
//         api.showOrderSummary(() => {
//             api.updateWallet()
//         })
//     })
// })

// createOrder().then(ProceedToPayment()).then(showOrderSummary()).then(updateWallet())


// Inversion of Control


// const promise = createOrder(cart)

// {data: orderDetails}

// promise.then(function (orderId)
// {
//     ProceedToPayment(orderId)
// })


// const products = fetch("https://dummyjson.com/products")
// products.then(function (data) {
//     return data.json()
// }).then(function (res) {
//     console.log(res);

// })




const cart = ["shoes", "pants", "jewellery"]

// const promise = createOrder(cart) // orderId

createOrder(cart)
.then(function (orderId) {
    return proceedToPayment(orderId)
})
.catch(err => console.log("kundan", err))
.then(function (msg) {
    return paymentInfo(msg)
})
.catch(err=>console.log("uday",err))
.then(function (time) {
    console.log(time);
})
.catch(err => console.log(err))



function createOrder(cart) {
    const pr = new Promise(function (resolve, reject) {
        // createOrder
        // Validatecart
        // OrderID

        if (!validatecart(cart)) {
            // const err = new Error("Cart is not valid")
            reject("Cart is not valid")
        }

        const orderId = "12345"
        if (orderId) {
            setTimeout(() => {
                resolve(orderId)
            }, 1000);
        }

    })

    return pr
}


function validatecart(cart) {
    return true
}

function proceedToPayment(orderId) {
    return new Promise(function (resolve, reject) {
        console.log(orderId);

        resolve("Payment is Successful")
    })
}
function paymentInfo(msg) {
    return new Promise(function (resolve, reject) {
        console.log("msg recived is", msg);
        reject(Date.now())
    })
}