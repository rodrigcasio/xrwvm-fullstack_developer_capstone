# Car Dealership — Full Stack Application Development Capstone

This is my final project for IBM's **Full Stack Application Development Capstone** course. I built a car dealership web app across eight hands-on labs, putting together everything I learned in the program into one working application.

On the site, users can browse dealerships, filter by state, check out dealer details, read customer reviews (each one gets a sentiment label — positive, negative, or neutral), and post their own review once they're logged in.

## Overview

Here's how the different pieces fit together:

- **Django** — static pages, user login/register, and a proxy layer to the backend APIs
- **React** — the dynamic pages for browsing dealers and posting reviews
- **Express.js + MongoDB** — REST APIs for dealership and review data
- **Flask** — a small microservice that analyzes review sentiment with NLTK
- **Docker & Kubernetes** — containerized and deployed to IBM Cloud
- **GitHub Actions** — automated linting on every push

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

## Features by Lab

| Lab | Feature | Implementation |
|-----|---------|----------------|
| 1 | Static pages | `Home.html`, `About.html`, `Contact.html` with Bootstrap styling |
| 2 | User management | Django auth — register, login, logout with session handling |
| 3 | REST APIs | Express + Mongoose endpoints for dealerships and reviews |
| 4 | Django models | `CarMake` and `CarModel` with foreign key relationships |
| 5 | Proxy services | `restapis.py` forwards requests to Express and sentiment APIs |
| 6 | Dynamic pages | React components for dealer listing, details, and review posting |
| 7 | CI/CD | GitHub Actions workflow with `flake8` (Python) and `JSHint` (JavaScript) |
| 8 | Containerization | Dockerfiles, `docker-compose`, Kubernetes deployment on IBM Cloud |

## Tech Stack

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

## Key API Endpoints

### Express + MongoDB (`database/app.js`)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/fetchDealers` | List all dealerships |
| GET | `/fetchDealers/:state` | Filter dealerships by state |
| GET | `/fetchDealer/:id` | Get dealership by ID |
| GET | `/fetchReviews/dealer/:id` | Get reviews for a dealer |
| POST | `/insert_review` | Submit a new review |

### Django Proxy (`djangoapp/`)

| Endpoint | Description |
|----------|-------------|
| `/djangoapp/login` | User authentication |
| `/djangoapp/register` | User registration |
| `/djangoapp/logout` | User logout |
| `/djangoapp/get_dealers` | Proxy to fetch all dealers |
| `/djangoapp/get_dealers/<state>` | Proxy to filter dealers by state |
| `/djangoapp/dealer/<id>` | Proxy to fetch dealer details |
| `/djangoapp/reviews/dealer/<id>` | Proxy reviews with sentiment analysis |
| `/djangoapp/add_review` | Post review (authenticated users only) |
| `/djangoapp/get_cars` | List car makes and models |

### Flask Sentiment Analyzer

| Endpoint | Description |
|----------|-------------|
| `/analyze/<text>` | Returns `positive`, `negative`, or `neutral` sentiment |

## Getting Started

### Prerequisites

- Python 3.12+
- Node.js 14+
- MongoDB
- Docker (optional, for containerized setup)

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/rodrigcasio/xrwvm-fullstack_developer_capstone.git
   cd xrwvm-fullstack_developer_capstone/server
   ```

2. **Start MongoDB + Express API**
   ```bash
   cd database
   docker-compose up --build
   ```

3. **Start Flask sentiment analyzer**
   ```bash
   cd djangoapp/microservices
   pip install -r requirements.txt
   python app.py
   ```

4. **Start Django server**
   ```bash
   cd server
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver
   ```

5. **Build React frontend** (if running separately)
   ```bash
   cd frontend
   npm install
   npm run build
   ```

### Environment Variables

Create a `.env` file in `server/djangoapp/`:

```env
backend_url=http://localhost:3030
sentiment_analyzer_url=http://localhost:5050/
```

## Deployment

The application is containerized with Docker and deployed to **IBM Cloud Kubernetes Service**:

- Django app image pushed to IBM Container Registry (`us.icr.io`)
- Kubernetes `deployment.yaml` manages rolling updates
- `entrypoint.sh` runs migrations and collects static files on startup

## CI/CD

The GitHub Actions workflow (`.github/workflows/main.yml`) runs on every push to `main`:

- **Python linting** — `flake8` across all `.py` files
- **JavaScript linting** — `JSHint` on Express API files in `server/database/`

## Author

**Rodrigo Casio** — Computer Systems Engineering student

- GitHub: [@rodrigcasio](https://github.com/rodrigcasio)
- Portfolio: [rodrigcasio.github.io](https://rodrigcasio.github.io)
- LinkedIn: [Rodrigo Casio](https://www.linkedin.com/in/rodrigo-casio-a93ab91aa/)

## License

See [LICENSE](LICENSE) for details.
