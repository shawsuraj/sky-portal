import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from django.contrib.auth.models import User
from apps.teams.models import Organisation, Department, Team, Repository, TeamDependency
from apps.users.models import Profile


def create_or_update_user(username, email, password, first_name, last_name):
    user, created = User.objects.get_or_create(username=username)

    user.email = email
    user.first_name = first_name
    user.last_name = last_name
    user.is_active = True

    if created:
        user.set_password(password)
    else:
        # keep it simple for demo/testing so passwords stay known
        user.set_password(password)

    user.save()
    return user


def create_or_update_profile(user, phone):
    profile, _ = Profile.objects.get_or_create(user=user)
    profile.name = f"{user.first_name} {user.last_name}".strip()
    profile.email = user.email
    profile.phone = phone
    profile.save()
    return profile


def run():
    # -------------------------
    # USERS
    # -------------------------
    users_data = [
        ("sebastian.holt", "sebastian.holt@sky.local", "Password123", "Sebastian", "Holt", "07000 000001"),
        ("mason.briggs", "mason.briggs@sky.local", "Password123", "Mason", "Briggs", "07000 000002"),
        ("olivia.carter", "olivia.carter@sky.local", "Password123", "Olivia", "Carter", "07000 000003"),
        ("james.bennett", "james.bennett@sky.local", "Password123", "James", "Bennett", "07000 000004"),
        ("emma.richardson", "emma.richardson@sky.local", "Password123", "Emma", "Richardson", "07000 000005"),
        ("liam.turner", "liam.turner@sky.local", "Password123", "Liam", "Turner", "07000 000006"),
        ("ava.hughes", "ava.hughes@sky.local", "Password123", "Ava", "Hughes", "07000 000007"),
        ("noah.ward", "noah.ward@sky.local", "Password123", "Noah", "Ward", "07000 000008"),
        ("mia.reed", "mia.reed@sky.local", "Password123", "Mia", "Reed", "07000 000009"),
        ("ethan.brooks", "ethan.brooks@sky.local", "Password123", "Ethan", "Brooks", "07000 000010"),
        ("grace.foster", "grace.foster@sky.local", "Password123", "Grace", "Foster", "07000 000011"),
        ("lucas.price", "lucas.price@sky.local", "Password123", "Lucas", "Price", "07000 000012"),
        ("ella.bailey", "ella.bailey@sky.local", "Password123", "Ella", "Bailey", "07000 000013"),
        ("henry.cox", "henry.cox@sky.local", "Password123", "Henry", "Cox", "07000 000014"),
        ("sophie.gray", "sophie.gray@sky.local", "Password123", "Sophie", "Gray", "07000 000015"),
        ("jack.morris", "jack.morris@sky.local", "Password123", "Jack", "Morris", "07000 000016"),
        ("chloe.bell", "chloe.bell@sky.local", "Password123", "Chloe", "Bell", "07000 000017"),
    ]

    created_users = {}

    for username, email, password, first_name, last_name, phone in users_data:
        user = create_or_update_user(username, email, password, first_name, last_name)
        create_or_update_profile(user, phone)
        created_users[username] = user

    print("Users and profiles added/updated")

    # -------------------------
    # ORGANISATION
    # -------------------------
    org, _ = Organisation.objects.get_or_create(org_name="Sky Engineering")
    org.org_name = "Sky Engineering"
    org.save()

    # -------------------------
    # MAIN USERS
    # -------------------------
    sebastian = created_users["sebastian.holt"]
    mason = created_users["mason.briggs"]
    olivia = created_users["olivia.carter"]
    james = created_users["james.bennett"]
    emma = created_users["emma.richardson"]

    # -------------------------
    # DEPARTMENTS
    # -------------------------
    dept1, _ = Department.objects.get_or_create(
        organisation=org,
        department_name="xTV_Web"
    )
    dept1.dept_leader_user = sebastian
    dept1.dept_description = "Department focused on xTV web platform delivery, streaming interfaces, and related engineering support."
    dept1.specialisation = "Web Platforms"
    dept1.save()

    dept2, _ = Department.objects.get_or_create(
        organisation=org,
        department_name="Native TVs"
    )
    dept2.dept_leader_user = mason
    dept2.dept_description = "Department focused on native TV applications, device integrations, and platform optimisation."
    dept2.specialisation = "Native TV Apps"
    dept2.save()

    print("Departments added/updated")

    # -------------------------
    # TEAMS
    # -------------------------
    team1, _ = Team.objects.get_or_create(
        department=dept1,
        team_name="Code Warriors"
    )
    team1.manager_user = olivia
    team1.status = "Active"
    team1.responsibilities = "Build and maintain xTV web services, deployment pipelines, and platform stability."
    team1.purpose = "Deliver reliable web-based streaming platform features."
    team1.description = "Cross-functional engineering team working on xTV web delivery."
    team1.skills = "AWS, Django, CI/CD, Reliability"
    team1.save()

    team2, _ = Team.objects.get_or_create(
        department=dept1,
        team_name="Bit Masters"
    )
    team2.manager_user = james
    team2.status = "Active"
    team2.responsibilities = "Support feature development, debugging, observability, and software quality for xTV web."
    team2.purpose = "Improve product quality and speed of delivery for xTV web."
    team2.description = "Engineering team focused on debugging, delivery, and software support."
    team2.skills = "Debugging, QA, Observability, Software Engineering"
    team2.save()

    team3, _ = Team.objects.get_or_create(
        department=dept2,
        team_name="Data Wranglers"
    )
    team3.manager_user = emma
    team3.status = "Active"
    team3.responsibilities = "Support data, security, QA, and operational work across native TV systems."
    team3.purpose = "Improve reliability and delivery across native TV products."
    team3.description = "Engineering team supporting native TV delivery and platform operations."
    team3.skills = "Security, QA, Support, Delivery"
    team3.save()

    # -------------------------
    # TEAM MEMBERS
    # always overwrite members properly
    # -------------------------
    team1.members.set([
        created_users["olivia.carter"],
        created_users["liam.turner"],
        created_users["ava.hughes"],
        created_users["noah.ward"],
        created_users["mia.reed"],
    ])

    team2.members.set([
        created_users["james.bennett"],
        created_users["ethan.brooks"],
        created_users["grace.foster"],
        created_users["lucas.price"],
        created_users["ella.bailey"],
    ])

    team3.members.set([
        created_users["emma.richardson"],
        created_users["henry.cox"],
        created_users["sophie.gray"],
        created_users["jack.morris"],
        created_users["chloe.bell"],
    ])

    print("Teams and members added/updated")

    # -------------------------
    # REPOSITORIES
    # -------------------------
    repo_data = [
        (team1, "xtv-web-frontend", "https://github.com/sky-engineering/xtv-web-frontend"),
        (team1, "xtv-web-api", "https://github.com/sky-engineering/xtv-web-api"),

        (team2, "bit-masters-observability", "https://github.com/sky-engineering/bit-masters-observability"),
        (team2, "bit-masters-quality-tools", "https://github.com/sky-engineering/bit-masters-quality-tools"),

        (team3, "native-tv-data-pipeline", "https://github.com/sky-engineering/native-tv-data-pipeline"),
        (team3, "native-tv-security-support", "https://github.com/sky-engineering/native-tv-security-support"),
    ]

    for team, repo_name, repo_url in repo_data:
        repo, _ = Repository.objects.get_or_create(team=team, repo_name=repo_name)
        repo.repo_url = repo_url
        repo.save()

    print("Repositories added/updated")

    # -------------------------
    # TEAM DEPENDENCIES
    # optional but useful for admin/demo
    # -------------------------
    dep1, _ = TeamDependency.objects.get_or_create(
        upstream_team=team1,
        downstream_team=team2,
        dependency_type="Platform Support"
    )
    dep1.dependency_description = "Bit Masters depends on Code Warriors for core xTV web platform updates and service availability."
    dep1.save()

    dep2, _ = TeamDependency.objects.get_or_create(
        upstream_team=team3,
        downstream_team=team1,
        dependency_type="Data Integration"
    )
    dep2.dependency_description = "Code Warriors depends on Data Wranglers for selected native TV data feeds and operational support."
    dep2.save()

    print("Team dependencies added/updated")
    print("All data added successfully")


if __name__ == "__main__":
    run()