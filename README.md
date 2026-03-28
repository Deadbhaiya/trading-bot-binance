# 🚀 Binance Futures Trading Bot (Testnet)

## 👨‍💻 Author

**Jay (BTech Student | Developer | Tech Enthusiast)**

This project is fully designed and developed by me as part of a technical evaluation to demonstrate my ability to build real-world API-based systems with clean architecture, validation, logging, and error handling.

---

## 📌 Project Overview

This is a **command-line based trading bot** built using Python that interacts with the Binance Futures Testnet API.

The bot allows users to:

* Place **MARKET orders**
* Place **LIMIT orders**
* Execute both **BUY and SELL trades**
* Validate user input before execution
* Log all requests, responses, and errors

The project is structured in a modular way, separating concerns like API handling, validation, and CLI interaction.

---

## 🎯 Problem It Solves

Placing trades manually or writing unstructured scripts can lead to:

* Invalid inputs causing failed trades
* Lack of visibility into API responses
* No tracking of errors or execution history
* Poor code maintainability

This bot solves these problems by:

* ✅ Validating all inputs before execution
* ✅ Providing clear output of order status
* ✅ Logging all activities for debugging and tracking
* ✅ Using a clean, reusable architecture

---

## ⚙️ Features

* ✅ Market & Limit Order Support
* ✅ BUY and SELL functionality
* ✅ CLI-based user input (argparse)
* ✅ Input validation with meaningful errors
* ✅ Logging of API requests, responses, and failures
* ✅ Structured and modular codebase

---

## 🏗️ Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py          # Binance API connection
│   ├── orders.py          # Order execution logic
│   ├── validators.py      # Input validation
│   ├── logging_config.py  # Logging setup
│
├── logs/
│   └── app.log            # Execution logs
│
├── cli.py                 # CLI entry point
├── requirements.txt
└── README.md
```

---

## 🧠 How It Works

1. User runs a command from terminal
2. CLI parses inputs (symbol, side, type, quantity, price)
3. Inputs are validated
4. Order request is sent to Binance Futures Testnet API
5. Response is received and displayed
6. Logs are saved for tracking and debugging

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```
git clone <your-repo-link>
cd trading_bot
```

---

### 2. Install Dependencies

```
pip install -r requirements.txt
```

---

### 3. Configure Environment Variables

Create a `.env` file in root directory:

```
API_KEY=your_api_key
API_SECRET=your_secret_key
BASE_URL=https://testnet.binancefuture.com
```

---

### 4. Run the Application

#### ▶️ MARKET ORDER

```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

#### ▶️ LIMIT ORDER

```
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000
```

---

## 📊 Example Output

```
Order Summary:
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.001

Order Successful
Order ID: 123456
Status: FILLED
Executed Qty: 0.001
Avg Price: 58000
```

---

## 📄 Logs

All activities are recorded in:

```
logs/app.log
```

Includes:

* Order requests
* API responses
* Errors (if any)

---

## ⚠️ Important Notes

* This project uses **Binance Futures Testnet** (no real money involved)
* API keys must not be shared publicly
* Ensure sufficient testnet balance before placing orders

---

## 🧪 Testing

The bot has been tested with:

* ✅ MARKET orders
* ✅ LIMIT orders
* ✅ Valid and invalid inputs
* ✅ Error scenarios (API + validation)

---

## 🚀 Future Improvements

* Add Stop-Limit / OCO orders
* Improve CLI with interactive UI
* Add retry mechanism for failed requests
* Build a web-based dashboard

---

## 🙌 Final Note

This project reflects my understanding of:

* API integration
* Clean code architecture
* Error handling & validation
* Logging systems
* Real-world application design

---

⭐ If you found this project useful or interesting, feel free to connect or give feedback!
