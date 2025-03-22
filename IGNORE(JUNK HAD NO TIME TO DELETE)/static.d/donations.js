const stripe = Stripe("pk_test_51R4qU2QwgHTPOE7UZUQLE9Yrj8AJTeZa336Zz8lffxt0k8MkjvNJdH4mY2p9TFFK9G7IiLb6vgMs90e6XF8ZSo8v007GbeaCeF");
const elements = stripe.elements();

const card = elements.create("card");
card.mount("#card-element");

document.getElementById("donation-form").addEventListener("submit", async (e) => {
    e.preventDefault();

    const { token, error } = await stripe.createToken(card);

    if (error) {
        document.getElementById("card-errors").textContent = error.message;
    } else {
        processPayment(token);
    }
});

async function processPayment(token) {
    const amount = document.getElementById("amount").value;
    
    if (amount < 1) {
        alert("Please enter a valid donation amount.");
        return;
    }

    const response = await fetch("/charge", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ token: token.id, amount: amount }),
    });

    const result = await response.json();

    if (result.success) {
        alert("Thank you for your donation!");
        location.reload();
    } else {
        alert("Payment failed. Please try again.");
    }
}
