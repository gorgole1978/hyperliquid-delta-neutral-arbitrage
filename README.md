# 🚀 Hyperliquid Delta-Neutral Arbitrage Bot (Python Template)

A pure Python boilerplate designed to interact with the [Hyperliquid L1 API](https://hyperliquid.xyz/). 

This repository contains the basic connection structure to fetch funding rates and establish a baseline for automated trading.

## ⚠️ The Async API Challenge
If you are building on Hyperliquid, you already know that execution speed and slippage are the biggest enemies of a Delta-Neutral strategy. Sending a "Short Perp" order and a "Long Spot" order sequentially will expose you to market risk and destroy your funding rate edge. 

Managing WebSockets, `aiohttp` sessions, and mapping `UBTC` / `BTC` cross-margin logic from scratch takes dozens of hours.

## 💎 Get the Production-Ready Source Code
I spent the last few weeks fighting the API quirks so you don't have to. 

If you want to skip the headache and jump straight to printing funding rates, the **Complete Full-Async Version** is available. 

### What's included in the Full Version:
- **Full Async Execution Engine:** Fires both legs (Spot & Perp) concurrently (`asyncio.gather`) to minimize slippage.
- **Built-in Web Dashboard:** A lightweight local `aiohttp` server to monitor your real-time PnL and active hedges visually.
- **Dry-Run Mode:** Safely test the execution logic on live orderbooks without risking a single cent.
- **Robust Error Handling:** Automatic rollbacks if one leg gets rejected by the exchange.

🔗 **[Grab the Full Python Source Code Here (Whop / Gumroad Link)]**  
*https://gbsolutions23.gumroad.com/l/fjdsxv*

---

## 🛠️ Basic Usage (This free repository)
Below is a simple synchronous example of how to pull current funding rates using basic requests.

```python
# Check the demo.py file included in this repo
