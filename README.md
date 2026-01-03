# Barber Shop Appointment System (Week 1)

> Live README: update daily. This file is derived directly from the PRD and reflects the current scope, progress and instructions for contributors.

## Summary
A full-stack barber shop booking system that allows customers to book services with specific barbers, and includes admin/manager controls. This repository follows the Week 1 PRD and is designed to be a complete, deployable product by the end of the 7-day sprint.

## Highlights
* Backend: Django + Django REST Framework ✅
* Frontend: React (Vite / Next.js) + Tailwind CSS ✅
* Development DB: SQLite (Django default) — **PostgreSQL integration moved to Day 7** ✅
* Repo structure (mono repo, atomic design) ✅
* PR template y gitignore ✅
* State management: Zustand ✅
* Auth forms (login/register) ✅
* Auth state management & token persistence ✅
* Data fetching/cache: React Query (planned) 🕐
* Auth: JWT (SimpleJWT) ✅
* Animations: Framer Motion ✅
* Testing: Pytest (backend) / Jest + React Testing Library (frontend) 🕐
* Containerization & Deploy: Docker / Render / Vercel (planned) 🕐

## Architecture & Tech (PRD-aligned)
| LayerTechnologyStatus |                               |    |
| --------------------- | ----------------------------- | -- |
| Backend               | Django, Django REST Framework | ✅  |
| ORM                   | Django ORM (SQLite for dev)   | ✅  |
| Frontend              | React (Vite or Next.js)       | ✅  |
| Styling               | Tailwind CSS                  | ✅  |
| Auth                  | JWT (SimpleJWT)               | ✅ |
| State                 | Zustand                       | 🕐 |
| Data fetching         | React Query                   | 🕐 |
| Testing               | Pytest / Jest + RTL           | 🕐 |
| CI/CD                 | GitHub Actions                | 🕐 |

## Development Status & 7-Day Plan (PRD)
* **Day 1:** Project initialization (React + Tailwind, Django + DRF, SQLite, repo structure, PR template, gitignore) — ✅ completed.
* **Day 2:** Auth (JWT) + Login/Register UI — ✅ completed.
* **Day 3:** Services & Barbers CRUD (API + UI) — 🕐 planned.
* **Day 4:** Appointment model, availability validation, booking UI — 🕐 planned.
* **Day 5:** Layout, protected routes, client dashboard — 🕐 planned.
* **Day 6:** Admin dashboard, metrics, barber agenda — 🕐 planned.
* **Day 7:** Tests, seed data, PostgreSQL production integration and deploy — 🕐 planned.

## How to run locally

**Backend**
```
cd backend
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

**Frontend**
```
cd frontend
npm install
npm run dev
```

## Notes
* The repository is intentionally using SQLite for development to accelerate day-to-day work. Production-grade PostgreSQL integration is scheduled for Day 7 to avoid blocking development.
* Keep PRs small and tied to issues from the PRD. Use the PR template (see `.github/pull_request_template.md`).

## PR Template (short)
Create the file at `.github/pull_request_template.md` and use the following content:
```
## Description
Short description of the changes.

## Related issue
Closes #<issue-number>

## Changes
- Backend
- Frontend
- Docs

## How to test
Steps to verify locally.

## Checklist
- [ ] Tests added / updated
- [ ] Lint passes
- [ ] README updated (if needed)
```

> This README is kept in sync with the PRD document.
