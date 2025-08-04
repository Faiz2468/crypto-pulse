# CryptoPulse — Real-Time Cryptocurrency Price Tracker

**CryptoPulse** is a lightweight, real-time data pipeline that collects current cryptocurrency prices using the CoinGecko API and stores them in a Supabase-hosted PostgreSQL database.

This project demonstrates cloud integration, API consumption, and scalable data ingestion — ideal for data engineering, cloud development, or backend portfolio showcases.

---

## Key Features

- Real-time price fetching from [CoinGecko API](https://www.coingecko.com/en/api)
- Seamless integration with [Supabase](https://supabase.com/)
- Clean, modular Python codebase
- Easily extensible to more assets or time intervals
- Environment variables and Git best practices implemented

---

## Tech Stack

| Tool         | Purpose                                |
|--------------|----------------------------------------|
| Python       | Core scripting language                |
| CoinGecko API| Real-time crypto market data           |
| Supabase     | Cloud database (PostgreSQL + REST)     |
| Dotenv       | Secure environment variable management |

---

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Faiz2468/crypto-pulse.git
   cd crypto-pulse