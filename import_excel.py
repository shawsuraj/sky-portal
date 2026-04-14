from openpyxl import load_workbook
import sqlite3

file_path = "SkyDB.xlsx"
db_path = "db.sqlite3"


def clean(value):
    if value is None:
        return ""
    return str(value).replace("\xa0", " ").strip()


def username_from_name(name):
    return clean(name).lower().replace(" ", ".")


def email_from_name(name):
    return f"{username_from_name(name)}@sky.local"


wb = load_workbook(file_path, data_only=True)
ws = wb.active

rows = []
for row in ws.iter_rows(values_only=True):
    rows.append([clean(x) for x in row])

conn = sqlite3.connect(db_path)
cur = conn.cursor()
cur.execute("PRAGMA foreign_keys = ON;")

# --------------------------
# Base records
# --------------------------
cur.execute("""
    INSERT OR IGNORE INTO Organisation (organisationID, orgName)
    VALUES (1, 'Sky Engineering')
""")

cur.execute("""
    INSERT OR IGNORE INTO Team_Type (teamTypeID, typeName, typeDescription)
    VALUES (1, 'Default Team Type', 'Imported from spreadsheet')
""")

# --------------------------
# Section parsing
# --------------------------
mode = None
department_rows = []
team_rows = []
workstream_rows = []
skill_dep_rows = []

for row in rows:
    c1 = row[0] if len(row) > 0 else ""
    c2 = row[1] if len(row) > 1 else ""
    c3 = row[2] if len(row) > 2 else ""

    if c1 == "Department" and "Team Leader" in c2 and "Department Head" in c3:
        mode = "departments"
        continue

    if "Team Name" in c1 and "Jira Project Name" in c2:
        mode = "teams"
        continue

    if "Workstream" in c1:
        mode = "workstreams"
        continue

    if "Development Focus Areas" in c1:
        mode = None
        continue

    if "Key Skills" in c1 and "Downstream" in c2:
        mode = "skills_deps"
        continue

    if "Software Owned" in c1:
        mode = None
        continue

    if mode == "departments":
        if c1 and c2 and c3:
            department_rows.append((c1, c2, c3))

    elif mode == "teams":
        if c1:
            team_rows.append((c1, c2))

    elif mode == "workstreams":
        if c1 or c2 or c3:
            workstream_rows.append((c1, c2, c3))

    elif mode == "skills_deps":
        if c1 or c2 or c3:
            skill_dep_rows.append((c1, c2, c3))

# --------------------------
# Users
# --------------------------
user_ids = {}

def get_user_id(full_name, role):
    full_name = clean(full_name)
    if full_name in user_ids:
        return user_ids[full_name]

    user_id = f"U{len(user_ids)+1:03d}"
    user_ids[full_name] = user_id

    cur.execute("""
        INSERT OR IGNORE INTO User
        (userID, userName, email, passwordHash, fullName, createdAt, updatedAt, userRole)
        VALUES (?, ?, ?, ?, ?, datetime('now'), datetime('now'), ?)
    """, (
        user_id,
        username_from_name(full_name),
        email_from_name(full_name),
        "hash123",
        full_name,
        role
    ))
    return user_id

# --------------------------
# Departments
# --------------------------
department_head_map = {}

for dept_name, team_leader, dept_head in department_rows:
    get_user_id(team_leader, "Team Leader")
    dept_head_id = get_user_id(dept_head, "Department Head")
    if dept_name not in department_head_map:
        department_head_map[dept_name] = dept_head_id

department_ids = {}
next_department_id = 1

for dept_name, dept_head_id in department_head_map.items():
    department_ids[dept_name] = next_department_id
    cur.execute("""
        INSERT OR IGNORE INTO Department
        (departmentID, organisationID, departmentName, deptDescription, deptLeaderUserID)
        VALUES (?, 1, ?, ?, ?)
    """, (
        next_department_id,
        dept_name,
        f"{dept_name} department imported from Excel",
        dept_head_id
    ))
    next_department_id += 1

# --------------------------
# Teams
# --------------------------
def guess_department_id(jira_name):
    jira_name = clean(jira_name)

    if "Lightning Xtv" in jira_name or jira_name == "Client Web":
        return department_ids.get("xTV_Web", 1)
    if "Roku TV" in jira_name or "Apple TV" in jira_name:
        return department_ids.get("Native TVs", 1)
    if "Mobile" in jira_name:
        return department_ids.get("Mobile", 1)
    if "Automation QA" in jira_name:
        return department_ids.get("Reliability_Tool", 1)
    if "Device as a Service" in jira_name or "SRE" in jira_name or "Apps Tooling" in jira_name or "CLIP Backend for Frontend" in jira_name:
        return department_ids.get("Arch", 1)
    if "Support" in jira_name:
        return department_ids.get("Programme", 1)

    return department_ids.get("xTV_Web", 1)

leader_names = [clean(r[1]) for r in department_rows]
leader_names = list(dict.fromkeys(leader_names))

team_ids = {}
next_team_id = 1

for i, (team_name, jira_name) in enumerate(team_rows):
    manager_name = leader_names[i % len(leader_names)]
    manager_id = user_ids[manager_name]
    dept_id = guess_department_id(jira_name)

    cur.execute("""
        INSERT OR IGNORE INTO Team
        (teamID, departmentID, teamTypeID, managerUserID, teamName,
         responsibilities, purpose, description, status, createdDate, disbandedAt)
        VALUES (?, ?, 1, ?, ?, ?, ?, ?, ?, date('now'), NULL)
    """, (
        next_team_id,
        dept_id,
        manager_id,
        team_name,
        jira_name if jira_name else "Imported responsibilities",
        "Imported from spreadsheet",
        "Imported from SkyDB conv.xlsx",
        "Active"
    ))
    team_ids[team_name] = next_team_id
    next_team_id += 1

# --------------------------
# Repositories
# --------------------------
next_repo_id = 1
repo_ids = {}

for workstream, repo_url, jira_link in workstream_rows:
    if not (workstream or repo_url or jira_link):
        continue

    repo_name = workstream if workstream else f"Repository {next_repo_id}"
    repo_url_final = repo_url if repo_url else (jira_link if jira_link else "N/A")
    platform = "Unknown"

    if "github" in repo_url_final.lower():
        platform = "GitHub"
    elif "bit.ly" in repo_url_final.lower() or "tiny" in repo_url_final.lower() or "short" in repo_url_final.lower():
        platform = "Link"

    cur.execute("""
        INSERT OR IGNORE INTO Repository (repoID, repoName, repoUrl, platform)
        VALUES (?, ?, ?, ?)
    """, (
        next_repo_id,
        repo_name[:200],
        repo_url_final,
        platform
    ))
    repo_ids[repo_name] = next_repo_id
    next_repo_id += 1

# --------------------------
# Skills
# --------------------------
skill_ids = {}
next_skill_id = 1

for skill_text, downstream, dependency_type in skill_dep_rows:
    if not skill_text:
        continue

    skill_name = skill_text[:120]

    if skill_name not in skill_ids:
        cur.execute("""
            INSERT OR IGNORE INTO Skill (skillID, skillName, skillDescription)
            VALUES (?, ?, ?)
        """, (
            next_skill_id,
            skill_name,
            skill_text
        ))
        skill_ids[skill_name] = next_skill_id
        next_skill_id += 1

# --------------------------
# Team_Skill
# simple best-effort linking
# --------------------------
team_name_list = list(team_ids.keys())
skill_name_list = list(skill_ids.keys())

for i, team_name in enumerate(team_name_list):
    if not skill_name_list:
        break

    skill_name = skill_name_list[i % len(skill_name_list)]
    cur.execute("""
        INSERT OR IGNORE INTO Team_Skill (teamID, skillID, level)
        VALUES (?, ?, ?)
    """, (
        team_ids[team_name],
        skill_ids[skill_name],
        3
    ))

# --------------------------
# Team_Dependency
# best-effort linking from downstream names
# --------------------------
for i, (skill_text, downstream, dependency_type) in enumerate(skill_dep_rows):
    if not dependency_type:
        continue

    upstream_team = team_name_list[i % len(team_name_list)] if team_name_list else None
    if not upstream_team:
        continue

    upstream_team_id = team_ids[upstream_team]

    downstream_names = [x.strip() for x in clean(downstream).split(",") if x.strip()]
    for dn in downstream_names:
        if dn in team_ids and team_ids[dn] != upstream_team_id:
            cur.execute("""
                INSERT OR IGNORE INTO Team_Dependency
                (upstreamTeamID, downstreamTeamID, dependencyType, dependencyDescription, createdAt)
                VALUES (?, ?, ?, ?, datetime('now'))
            """, (
                upstream_team_id,
                team_ids[dn],
                dependency_type[:120],
                skill_text[:500] if skill_text else dependency_type
            ))

# --------------------------
# Team_Repository
# simple best-effort linking
# --------------------------
repo_name_list = list(repo_ids.keys())
for i, team_name in enumerate(team_name_list):
    if not repo_name_list:
        break

    repo_name = repo_name_list[i % len(repo_name_list)]
    cur.execute("""
        INSERT OR IGNORE INTO Team_Repository (teamID, repoID, purpose_notes)
        VALUES (?, ?, ?)
    """, (
        team_ids[team_name],
        repo_ids[repo_name],
        "Imported from workstream/repository section"
    ))

# --------------------------
# Team_Member
# link leaders to teams
# --------------------------
for i, team_name in enumerate(team_name_list):
    manager_name = leader_names[i % len(leader_names)]
    manager_id = user_ids[manager_name]

    cur.execute("""
        INSERT OR IGNORE INTO Team_Member (teamID, userID, userRole, joinedDate, leftDate)
        VALUES (?, ?, ?, date('now'), NULL)
    """, (
        team_ids[team_name],
        manager_id,
        "Leader"
    ))

conn.commit()

print("Import complete.")
print(f"Users inserted: {len(user_ids)}")
print(f"Departments inserted: {len(department_ids)}")
print(f"Teams inserted: {len(team_ids)}")
print(f"Repositories inserted: {len(repo_ids)}")
print(f"Skills inserted: {len(skill_ids)}")

conn.close()