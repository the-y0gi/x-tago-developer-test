# xTago Assignment – Scraping & Data Cleaning Pipeline

This project is a complete implementation of the **xTago Developer Test Task**.  
It demonstrates an end-to-end **scraping → data cleaning → frontend preview** workflow using Python and React, with **automatic backend-to-frontend data synchronization**.

---

## 🚀 Project Overview

### Key Capabilities
- Scrapes product data from https://www.wegetanystock.com/
- Cleans and standardizes product names using rule-based Python logic
- Detects brands from a predefined list
- Extracts volume / weight and identifies multipacks
- Generates SEO-friendly slugs
- Outputs normalized data as JSON
- Automatically syncs backend data to the frontend
- Displays cleaned data in a React UI with filtering and pagination

---

## 🧱 Tech Stack

### Backend
- Python
- Selenium (web scraping)
- Regular Expressions (data cleaning)
- JSON-based processing pipeline

### Frontend
- React (Create React App)
- Functional Components and Hooks

### Automation
- Node.js script for backend → frontend data sync

---

## 📁 Folder Structure


## Project Structure

```
xtago-assignment/
├── backend/
│   ├── scraper/
│   │   └── scraper.py          # Web scraping logic
│   ├── cleaner/
│   │   ├── pipeline.py         # Main data cleaning pipeline
│   │   ├── name_cleaner.py     # Product name cleaning
│   │   ├── brand_map.py        # Brand detection
│   │   ├── volume_parser.py    # Unit extraction
│   │   └── slugger.py          # Slug generation
│   ├── data/
│   │   ├── raw/                # Raw scraped data
│   │   └── processed/          # Cleaned data
│   └── utils/
│       └── file_io.py          # File I/O utilities
├── frontend/
│   ├── src/
│   │   ├── components/         # React components
│   │   ├── pages/              # Page components
│   │   └── data/               # Synced data
│   └── public/                 # Static assets
└── scripts/
    └── syncData.js             # Data sync script
```

## Installation

### Prerequisites

- Python 3.8+
- Node.js 14+
- Chrome browser (for Selenium)

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Install Python dependencies:
   ```bash
   pip install selenium webdriver-manager
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install Node.js dependencies:
   ```bash
   npm install
   ```

## Usage

### 1. Run the Scraper (Optional)

If you need to scrape fresh data:

```bash
cd backend/scraper
python scraper.py
```

This will generate `backend/data/raw/category_products.json`.

### 2. Clean the Data

```bash
cd backend/cleaner
python pipeline.py

or
 python -m cleaner.pipeline

```

This processes the raw data and creates `backend/data/processed/cleaned_products.json`.



### Cleaning Logic
- Removes price-related phrases (PMP, £, etc.)
- Removes unnecessary descriptors (can, bottle, bar, pack, etc.)
- Standardizes text casing
- Extracts volume / weight (g, ml, kg, ltr)
- Detects multipacks (e.g. 6x250ml, 4pk)
- Detects brands using a predefined list
- Generates SEO-friendly slugs



---

## 🏷️ Brand Detection

Brand detection is implemented using a hardcoded list as required by the assignment.

**Examples**
- Coca Cola Zero 330ml → Coca Cola  
- Whiskas Cat Food → Whiskas  
- Unknown brands → "Unknown"

---

## 🔁 Automatic Backend → Frontend Data Sync

To avoid manual copying of JSON files, an automated sync script is provided.

**Script**


### 3. Sync Data to Frontend

- Copies processed data from backend
- Syncs it directly into the React frontend data directory

```bash
cd frontend
npm run sync-data
```

Or manually run:
```bash
node ../scripts/syncData.js
```

### 4. Start the Frontend

```bash
cd frontend
npm start
```

The application will be available at `http://localhost:3000`.

## Data Flow

1. **Scraping**: Collects product data
2. **Cleaning**: 
   - Cleans product names
   - Detects brands
   - Extracts volume units
   - Identifies multipacks
   - Generates URL-friendly slugs
3. **Sync**: Copies cleaned data to frontend
4. **Display**: React app renders products by category

## Development

- Backend scripts can be run independently
- Frontend hot-reloads during development
- Data changes require re-syncing via the sync script

## Thanyou 
