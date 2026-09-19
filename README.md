# MedSupplyAI V2

A professional-style healthcare supply chain intelligence prototype for HE-03.

## What changed

- Batch/lot traceability and supply-chain event timeline
- Storage locations and temperature log support
- Inventory KPIs: days of supply, reorder point, safety stock, projected stockout
- Random Forest demand forecasting with transparent model metadata
- Consumption anomaly detection
- FEFO-oriented batch visibility
- Procurement recommendations and purchase orders
- Audit log for stock changes
- Modern multi-page dashboard UI
- Clear provenance labels: DEMO, USER ENTERED, SOURCE, AI-DERIVED

## Important data rule

The demo seed data is explicitly synthetic. Manufacturer, origin, storage requirements and traceability facts are not invented as real-world facts. Replace demo fields with verified product-label or regulatory data when available.

## Run

1. Install Python 3.10+.
2. Open PowerShell in the project root.
3. Create/activate a virtual environment or run its Python directly.
4. Install dependencies:

   pip install -r requirements.txt

5. Copy `.env.example` to `.env` and enter your MySQL password.
6. Start the server:

   python backend/app.py

7. Open http://127.0.0.1:5000

The application creates the `medsupplyai` database and the required tables automatically. It also upgrades an existing V1 inventory table without dropping existing data.

## Deploy to Vercel

This repository includes a Vercel Python entry point and route configuration. Vercel runs the Flask app as a serverless function; use a hosted MySQL-compatible database because Vercel's filesystem is ephemeral.

1. Create or import the project in Vercel with this repository as the root directory.
2. Add these Vercel environment variables for the Production, Preview and Development environments: `MYSQL_HOST`, `MYSQL_PORT`, `MYSQL_USER`, `MYSQL_PASSWORD`, and `MYSQL_DATABASE`.
3. Deploy. The frontend and `/api/*` routes are served by the Flask function.

For a first-time database, provision the database/schema with a user that has the required tables or temporarily set `MEDSUPPLYAI_INIT_DB=true` for one deployment. Set `MEDSUPPLYAI_SEED_DEMO=true` as well only when synthetic demo history is wanted. Leave both variables unset or false for normal production deployments.

The local `.env` file is ignored by Git and must not be uploaded as a deployment secret.

## Real-world data integration path

The schema includes provenance/source fields so verified data can later be imported from public sources such as DailyMed/FDA Structured Product Labeling and applicable Indian regulatory sources. The prototype does not claim that seed records are sourced from those services.


### 2.1.3 correction pass
- Procurement recommendations now subtract active outstanding purchase-order quantities, so a placed order covers the recommendation instead of remaining in the queue.
- New procurement orders created from recommendations are immediately marked `PLACED`.
- Added procurement status lifecycle endpoint for later operational states.
- API error responses are JSON-safe and frontend reports the actual HTTP failure instead of a JSON parse error caused by an HTML error page.
- Disabled stale browser caching for API, CSS and JavaScript resources during local development.
- Supply Chain and Procurement pages include retry/API-health controls.
