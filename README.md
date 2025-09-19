# QA Web3 - Wallet Connection

This project simulates a basic Web3 wallet connection test using HTML and JavaScript.  
It is designed for QA engineers who want to understand and validate how decentralized applications (dApps) interact with browser-based wallets like MetaMask.

## 🧪 What is being tested?

- Detection of Web3 provider (`window.ethereum`)
- Requesting wallet access
- Retrieving and displaying the user's wallet address
- Handling connection errors or rejection by the user

## 📋 Use Case

This type of test is essential in Web3 applications to validate that:

- The user can connect their wallet properly
- The dApp receives the correct wallet address
- There is proper feedback for connection success or failure

## 🚀 How to Run

1. Clone or download this repo
2. Open `index.html` in any browser with MetaMask installed
3. Click on `Connect Wallet`
4. Observe the connection status below the button

## 🛠 Tech Stack

- HTML5
- Vanilla JavaScript (no frameworks)
- MetaMask as Web3 provider

## ✅ Expected Result

If MetaMask is installed and the user accepts the connection, their wallet address will be displayed.  
If MetaMask is not available or the connection is rejected, an error message will be shown.

## 📷 Screenshot

<img width="365" height="400" alt="image" src="https://github.com/user-attachments/assets/6458c34e-6b9d-4acc-a57f-11da283592c3" />


## 🧠 About

This is part of a series of practical Web3 QA examples for showcasing automation and testing logic in decentralized environments.

---

🧑‍💻 Autor:

Raúl Casado – GaslessQA
🔗 https://www.linkedin.com/in/gaslessqa/

**License:** MIT
