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



const cart = ["shoes", "pants", "jewellery"]

api.createOrder(cart, () => {
    api.ProceedToPayment(() => {
        api.showOrderSummary(() => {
            api.updateWallet()
        })
    })
})


// Inversion of Control






