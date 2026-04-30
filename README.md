# Sky Portal

A web app for Sky Engineering — lets you search teams, view the org structure, send internal messages, and schedule meetings. Built with Django + SQLite for our 5COSC021W coursework.

## What it does

- **Dashboard** — overview of teams, departments, unread messages and recent activity
- **Teams** — browse and search all engineering teams, view team details, members, repos and dependencies
- **Organisation** — interactive network map showing how teams depend on each other (vis.js), filterable by department and dependency type
- **Messages** — internal messaging between users (inbox, sent, drafts)
- **Schedule** — create and manage team meetings, see upcoming schedule
- **Auth** — register, login, logout, update profile

## Project structure

```
sky-portal/
├── manage.py
├── requirements.txt
│
├── config/               # settings.py, urls.py
│
├── apps/
│   ├── core/             # dashboard / home view
│   ├── teams/            # team directory, team detail, models (Team, Dept, Org, Dependency)
│   ├── organisation/     # org map + JSON graph endpoint
│   ├── mails/            # internal messages
│   ├── schedule/         # meetings and attendees
│   └── users/            # registration, login, profile
│
├── templates/
│   ├── base.html         # shared layout (sidebar + topbar)
│   ├── dashboard.html
│   ├── components/       # left_nav, topbar
│   ├── teams/
│   ├── organisation/
│   ├── mails/
│   ├── schedule/
│   └── users/
│
├── static/
│   ├── css/
│   └── js/
│
└── docs/                 # meeting notes, test plans, UI designs
```

## Who built what

| Feature | Developer |
|---|---|
| Teams | Vinicius |
| Organisation + Dashboard + base template | Suraj Shaw |
| Messages | Hamdan |
| Schedule | Shqipdon |

## Test Accounts

| Role | Username | Password |
|---|---|---|
| User | Hamdankz | group123 |
| User | Shqipdonuk | group123 |
| Admin | SU | SU123 |

## Setup

```bash
git clone https://github.com/shawsuraj/sky-portal.git
cd sky-portal
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

To seed the database from the Excel file (put the file in the project root first):

```bash
python manage.py load_excel
```

## Branching

- `main` — submission branch, don’t push here directly
- `dev` — main working branch, all PRs go here
- `feature/<name>` — your own branch for your feature

Basic flow:

```bash
git checkout dev
git pull origin dev
git checkout -b feature/your-feature
# do your work
git push origin feature/your-feature
# open a PR into dev on GitHub
```

If you’re merging `dev` into your branch to stay up to date:

```bash
git merge dev
```

## Admin

Django admin is at `/admin/`. Log in with your superuser account. All models are registered so you can add/edit/delete teams, departments, messages, meetings etc from there.
