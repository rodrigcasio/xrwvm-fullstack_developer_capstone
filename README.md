# Car Dealership — Full Stack Application Development Capstone

This is my final project for IBM's **Full Stack Application Development Capstone** course. I built a car dealership web app, putting together everything I learned in the program into one working application. The repo came with a starter scaffold, but I implemented all the core functionality — from user auth and API endpoints to React pages, CI/CD, and deployment — to make it fully work.

On the site, users can browse dealerships, filter by state, check out dealer details, read customer reviews (each one gets a sentiment label — positive, negative, or neutral), and post their own review once they're logged in.

## Overview

The app brings together a few different technologies, and Django acts as the main hub. Here's a quick look at what each part does:

- **Django** — serves the static pages, handles user login/register, and proxies requests to the other backend services
- **React** — powers the dynamic pages where users browse dealers and post reviews
- **Express.js + MongoDB** — stores and serves dealership and review data through REST APIs
- **Flask** — a small microservice that analyzes review sentiment using NLTK
- **Docker & Kubernetes** — used to containerize the app and deploy it to IBM Cloud
- **GitHub Actions** — runs automated linting whenever I push changes

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         User Browser                            │
└────────────────────────────┬────────────────────────────────────┘
                             │
         ┌───────────────────┼───────────────────┐
         │                   │                   │
         ▼                   ▼                   ▼
  Static HTML Pages    React SPA (Routes)    Django Auth APIs
  (Home, About,        /dealers, /dealer,    /login, /register,
   Contact)            /postreview           /logout
         │                   │                   │
         └───────────────────┼───────────────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  Django Proxy   │
                    │   (restapis.py) │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
     ┌─────────────┐  ┌─────────────┐  ┌──────────────┐
     │  Express +  │  │   Django    │  │    Flask     │
     │   MongoDB   │  │  SQLite DB  │  │  Sentiment   │
     │  (port 3030)│  │ CarMake/    │  │  Analyzer    │
     │             │  │ CarModel    │  │  (port 5050) │
     └─────────────┘  └─────────────┘  └──────────────┘
```

## What I Built

Here's a breakdown of the main features I implemented throughout the project:

| # | Feature | What I did |
|---|---------|------------|
| 1 | Static pages | Set up `Home.html`, `About.html`, and `Contact.html` with Bootstrap styling |
| 2 | User management | Built register, login, and logout with Django auth and session handling |
| 3 | REST APIs | Created Express + Mongoose endpoints for dealerships and reviews |
| 4 | Django models | Defined `CarMake` and `CarModel` with a foreign key relationship |
| 5 | Proxy services | Wrote `restapis.py` to forward requests to the Express and sentiment APIs |
| 6 | Dynamic pages | Built React components for the dealer list, dealer details, and review form |
| 7 | CI/CD | Set up a GitHub Actions workflow with `flake8` (Python) and `JSHint` (JavaScript) |
| 8 | Containerization | Dockerized the app with `docker-compose` and deployed it to IBM Cloud with Kubernetes |

## Tech Stack

These are the main tools and frameworks I used:

| Layer | Technologies |
|-------|-------------|
| Frontend | React, React Router, HTML, CSS, Bootstrap |
| Backend | Django, Python, Gunicorn |
| API Server | Node.js, Express.js |
| Database | MongoDB (dealerships/reviews), SQLite (Django models) |
| Microservice | Flask, NLTK SentimentIntensityAnalyzer |
| DevOps | Docker, Docker Compose, Kubernetes, IBM Container Registry |
| CI/CD | GitHub Actions |

## Project Structure

The repo is organized like this — most of the work lives inside the `server/` folder:

```
xrwvm-fullstack_developer_capstone/
├── .github/workflows/main.yml    # CI/CD linting pipeline
├── server/
│   ├── djangoapp/                # Django app (views, models, proxy APIs)
│   │   ├── models.py             # CarMake & CarModel models
│   │   ├── views.py              # Auth & dealership proxy views
│   │   ├── restapis.py           # HTTP client for backend services
│   │   └── microservices/        # Flask sentiment analyzer
│   ├── djangoproj/               # Django project settings
│   ├── database/                 # Express + MongoDB API
│   │   ├── app.js                # REST endpoints
│   │   ├── dealership.js         # Dealership Mongoose schema
│   │   ├── review.js             # Review Mongoose schema
│   │   └── data/                 # Seed JSON data
│   ├── frontend/                 # React application
│   │   ├── src/components/
│   │   │   ├── Dealers/          # Dealer list, details, post review
│   │   │   ├── Login/            # Login component
│   │   │   └── Register/         # Registration component
│   │   └── static/               # Static HTML pages
│   ├── Dockerfile                # Django app container
│   ├── deployment.yaml           # Kubernetes deployment manifest
│   └── entrypoint.sh             # DB migrations on container start
└── README.md
```

## API Endpoints

Below are the main endpoints I worked with. The Express API handles the raw data, Django proxies most of it to the frontend, and Flask handles sentiment analysis.

### Express + MongoDB (`database/app.js`)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/fetchDealers` | Returns all dealerships |
| GET | `/fetchDealers/:state` | Filters dealerships by state |
| GET | `/fetchDealer/:id` | Returns a single dealership by ID |
| GET | `/fetchReviews/dealer/:id` | Returns all reviews for a dealer |
| POST | `/insert_review` | Adds a new review |

### Django Proxy (`djangoapp/`)

| Endpoint | Description |
|----------|-------------|
| `/djangoapp/login` | Handles user login |
| `/djangoapp/register` | Handles user registration |
| `/djangoapp/logout` | Handles user logout |
| `/djangoapp/get_dealers` | Fetches all dealers from the Express API |
| `/djangoapp/get_dealers/<state>` | Fetches dealers filtered by state |
| `/djangoapp/dealer/<id>` | Fetches details for a single dealer |
| `/djangoapp/reviews/dealer/<id>` | Fetches reviews and runs sentiment analysis on each one |
| `/djangoapp/add_review` | Posts a new review (requires login) |
| `/djangoapp/get_cars` | Returns car makes and models |

### Flask Sentiment Analyzer

| Endpoint | Description |
|----------|-------------|
| `/analyze/<text>` | Returns whether the text is `positive`, `negative`, or `neutral` |

## Getting Started

If you'd like to run the project locally, here's the setup I followed. You'll need a few things installed first:

### Prerequisites

- Python 3.12+
- Node.js 14+
- MongoDB
- Docker (optional — makes it easier to spin up MongoDB and the Express API)

### Local Development

1. **Clone the repo**
   ```bash
   git clone https://github.com/rodrigcasio/xrwvm-fullstack_developer_capstone.git
   cd xrwvm-fullstack_developer_capstone/server
   ```

2. **Start MongoDB and the Express API**
   ```bash
   cd database
   docker-compose up --build
   ```

3. **Start the Flask sentiment analyzer**
   ```bash
   cd djangoapp/microservices
   pip install -r requirements.txt
   python app.py
   ```

4. **Start the Django server**
   ```bash
   cd server
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver
   ```

5. **Build the React frontend** (if you're running it separately)
   ```bash
   cd frontend
   npm install
   npm run build
   ```

### Environment Variables

I used a `.env` file in `server/djangoapp/` to point Django at the other services:

```env
backend_url=http://localhost:3030
sentiment_analyzer_url=http://localhost:5050/
```

## Deployment

I containerized the app with Docker and deployed it to **IBM Cloud Kubernetes Service**. Here's how that part is set up:

- The Django app image gets pushed to IBM Container Registry (`us.icr.io`)
- `deployment.yaml` handles the Kubernetes deployment with rolling updates
- `entrypoint.sh` runs database migrations and collects static files when the container starts

## CI/CD

I also set up a GitHub Actions workflow (`.github/workflows/main.yml`) that runs on every push to `main`:

- **Python linting** — runs `flake8` on all `.py` files
- **JavaScript linting** — runs `JSHint` on the Express API files in `server/database/`

## Author

**Rodrigo Casio** — Computer Systems Engineering student

- GitHub: [@rodrigcasio](https://github.com/rodrigcasio)
- Portfolio: [rodrigcasio.github.io](https://rodrigcasio.github.io)
- LinkedIn: [Rodrigo Casio](https://www.linkedin.com/in/rodrigo-casio-a93ab91aa/)

## License

See [LICENSE](LICENSE) for details.
