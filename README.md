# KitchenAid Web Scraper

A full-stack web application that scrapes KitchenAid product prices from multiple Australian and New Zealand retailers. Built with Flask backend and React frontend.

## Features

- **Multi-retailer Price Scraping**: Automatically scrapes prices from 8+ retailers including:
  - David Jones
  - Myer
  - JB Hi-Fi
  - The Good Guys
  - Kitchen Warehouse
  - Stevens NZ
  - Harvey Norman (AU/NZ) - Currently disabled due to bot protection

- **Product Management**: Add, edit, and manage KitchenAid products with details like SKU, name, color, and retailer URLs

- **Real-time Scraping**: Trigger price scraping with live progress updates and error reporting

- **Search & Filter**: Search products by SKU/name and filter by retailer

- **Responsive UI**: Modern React frontend with Tailwind CSS styling

## Tech Stack

### Backend
- **Flask** - Python web framework
- **PostgreSQL** - Database for product storage
- **Playwright** - Web scraping with browser automation
- **playwright-stealth** - Anti-bot detection
- **BeautifulSoup4** - HTML parsing
- **psycopg2** - PostgreSQL adapter

### Frontend
- **React 19** - UI framework
- **React Router DOM** - Client-side routing
- **Tailwind CSS** - Utility-first styling
- **Create React App** - Build tooling

## Installation

### Prerequisites
- Python 3.8+
- Node.js 16+
- PostgreSQL database

### Backend Setup

1. Navigate to backend directory:
```bash
cd backend
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install Playwright browsers:
```bash
playwright install
```

5. Create `.env` file with database credentials:
```env
user=your_db_user
password=your_db_password
host=localhost
port=5432
dbname=your_db_name
```

6. Set up PostgreSQL database with required tables:
   - `products` table with columns: id, name, url, company, sku, colour
   - `companies` table with columns: company_id, company_name

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

## Usage

### Starting the Application

1. Start the backend server:
```bash
cd backend
python app.py
```
Backend runs on `http://localhost:5000`

2. Start the frontend development server:
```bash
cd frontend
npm start
```
Frontend runs on `http://localhost:3000`

### Using the Application

1. **Home Page**: Click "Scrape" to run price scraping on all products in the database
2. **Products Page**: 
   - Add new products with retailer URLs
   - Search existing products by SKU/name
   - Filter products by retailer
   - Edit/update existing products

## API Endpoints

- `GET /api/scrape` - Scrape all products
- `GET /api/scrape/single_price` - Scrape single product price
- `GET /api/products` - Get products with optional search/filter
- `POST /api/products` - Add new product
- `POST /api/products/update` - Update existing product
- `GET /api/companies` - Get list of supported retailers

## Project Structure

```
KitchenAide_Scraper/
├── backend/
│   ├── app.py              # Flask API routes
│   ├── scraping.py         # Web scraping logic
│   ├── database.py         # Database operations
│   ├── requirements.txt    # Python dependencies
│   └── venv/              # Virtual environment
├── frontend/
│   ├── src/
│   │   ├── components/    # React components
│   │   ├── pages/         # Page components
│   │   ├── assets/        # Images and static files
│   │   └── App.js         # Main App component
│   ├── package.json       # Node dependencies
│   └── tailwind.config.js # Tailwind configuration
└── README.md
```

## Contributing

This is a defensive web scraping tool for price monitoring purposes only. When contributing:

1. Follow existing code patterns and conventions
2. Test scraping functions with appropriate rate limiting
3. Respect retailer terms of service
4. Do not use for commercial purposes without permission

## Supported Retailers

| Retailer | Status | Notes |
|----------|--------|-------|
| David Jones | ✅ Active | Full price scraping support |
| Myer | ✅ Active | Handles discounted pricing |
| JB Hi-Fi | ✅ Active | Standard price extraction |
| The Good Guys | ✅ Active | Standard price extraction |
| Kitchen Warehouse | ✅ Active | Handles RRP and discounted prices |
| Stevens NZ | ✅ Active | New Zealand retailer |
| Harvey Norman AU | ❌ Disabled | Bot protection enabled |
| Harvey Norman NZ | ❌ Disabled | Bot protection enabled |

## License

This project is for educational and personal use only. Please respect retailer terms of service and implement appropriate rate limiting when scraping.