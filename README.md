# Sky Portal (dev)

Please read this document carefully before starting any work. Following a consistent workflow is important to avoid conflicts and ensure that all parts of the system integrate correctly.



## Project Overview

We are developing a Django-based web application.

Each team member is responsible for implementing a specific feature (for example: teams, organisation, messages, schedule, reports). However, all features must be integrated into a single, fully functional application.

This means:
- You will work independently on your feature
- Your work must remain compatible with the rest of the system



## Project Structure

Please do not modify the structure below.

Project structure inspired from:
https://medium.com/django-unleashed/django-project-structure-a-comprehensive-guide-4b2ddbf2b6b8

```bash
sky-portal/
│
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── config/                  # Django project (settings, urls)
│
├── apps/                    # ALL FEATURES (modular)
│   ├── teams/               # Vinicius
│   ├── organisation/        # Suraj Shaw
│   ├── messages/            # Hamdan
│   ├── schedule/            # Shqipdon
│   ├── users/               # AUTH (shared)
│   ├── core/                # homepage, navbar, base logic
│       ├── reports/         # Mohammad
│
├── templates/
│   ├── base.html            # ONE shared layout
│   ├── components/          # navbar, footer
│   ├── teams/
│   ├── organisation/
│   ├── messages/
│   ├── schedule/
│
├── static/
│   ├── css/
│   ├── js/
│
├── docs/                    # FOR COURSEWORK MARKS
│   ├── ERD.jpeg
│   ├── test-plans.md
│   ├── meeting-notes.md
│   ├── ui-designs/         # All the figma design
│
├── scripts/                # optional setup scripts
├── reports/                # Reports by Mohammad

```

Explanation:
- `apps/` contains backend logic (views, models, urls)
- `templates/` contains frontend HTML files
- `static/` contains CSS and JavaScript files



## Responsibilities

Each team member should primarily work within their assigned app.

- Teams : `apps/teams` -
- Organisation : `apps/organisation` - 
- Messages : `apps/messages` - 
- Schedule : `apps/schedule` - 

Please avoid modifying other team members code unless it has been discussed with them.



## GitHub Workflow

We are using the following branches:

- `main` → final version (submission)
- `dev` → main working branch
- `feature/*` → individual work branches



## Rules

The following rules must be followed:

1. Do not push directly to the `main` branch  
2. Always create and work on your own feature branch  
3. Always pull the latest changes from `dev` before starting work  
4. Do not modify shared database models without informing the group  
5. Do not edit other team members’ files without agreement  




## Initial Setup

Clone the repository and switch to the develop branch:

```bash
git clone <repository-url>
cd sky-engineering-app
git checkout develop
```

OR use github Desktop to clone (easier).



## Daily Workflow

### 1. Update your local repository

```bash
git checkout dev
git pull origin dev
```

### 2. Create a feature branch

```bash
git checkout -b feature/your-feature-name
```

Example:
- `feature/teams`
- `feature/messages`



### 3. Implement your feature

Work only within your assigned app and related templates.



### 4. Commit your changes

```bash
git add .
git commit -m "Implemented team search functionality"
```

Commit messages should clearly describe the changes made.



### 5. Push your branch

```bash
git push origin feature/your-feature-name
```



### 6. Create a Pull Request

On GitHub:
- Create a Pull Request from your feature branch
- Target branch should be `dev`

---

OR use GitHub Desktop to easily mangae branches and seeing coded chenges before commits (recommended in the begining).

---

## Pull Request Process

- Your code will be reviewed before merging  
- If changes are required, update your branch and push again  
- Once approved, the branch will be merged into `dev`

---

## Integration Notes

All components are connected through:
- URL configurations
- Templates
- Shared database models

Uncoordinated changes (e.g. renaming models, URLs, or templates) may break other parts of the system. Please ensure compatibility.

---

## Common Mistakes to Avoid

- Pushing directly to `main`  
- Working without pulling the latest updates  
- Making large, infrequent commits  
- Modifying shared files without coordination  
- Leaving work until the last stage  

---

## General Guidelines

- Commit regularly with clear messages  
- Test your code before pushing  
- Keep code clean and consistent  
- Communicate any issues early  

---

## Final Note

This is a collaborative project. All parts must be integrated into a single working application, and teamwork is essential for success. And even if any mistake happens in maganing github, we can always reverse it as it has version control.

---
