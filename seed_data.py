import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from django.contrib.auth.models import User
from apps.teams.models import Organisation, Department, Team, TeamMember
from apps.users.models import Profile


def create_or_update_user(username, email, password, first_name, last_name):
    user, created = User.objects.get_or_create(username=username)

    user.email = email
    user.first_name = first_name
    user.last_name = last_name
    user.is_active = True

    user.set_password(password)
    user.save()
    return user


def create_or_update_profile(user, phone):
    profile, created = Profile.objects.get_or_create(user=user)

    profile.name = f"{user.first_name} {user.last_name}".strip()
    profile.email = user.email
    profile.phone = phone

    profile.save()
    return profile


def add_team_members(team, users):
    # Add users to a team using the TeamMember table
    for user in users:
        TeamMember.objects.get_or_create(
            team=team,
            user=user
        )


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
        ("benjamin.hayes", "benjamin.hayes@sky.local", "Password123", "Benjamin", "Hayes", "07000 000006"),
        ("alexander.perry", "alexander.perry@sky.local", "Password123", "Alexander", "Perry", "07000 000007"),
        ("evelyn.hughes", "evelyn.hughes@sky.local", "Password123", "Evelyn", "Hughes", "07000 000008"),
        ("liam.turner", "liam.turner@sky.local", "Password123", "Liam", "Turner", "07000 000009"),
        ("ava.hughes", "ava.hughes@sky.local", "Password123", "Ava", "Hughes", "07000 000010"),
        ("noah.ward", "noah.ward@sky.local", "Password123", "Noah", "Ward", "07000 000011"),
        ("mia.reed", "mia.reed@sky.local", "Password123", "Mia", "Reed", "07000 000012"),
        ("ethan.brooks", "ethan.brooks@sky.local", "Password123", "Ethan", "Brooks", "07000 000013"),
        ("grace.foster", "grace.foster@sky.local", "Password123", "Grace", "Foster", "07000 000014"),
        ("lucas.price", "lucas.price@sky.local", "Password123", "Lucas", "Price", "07000 000015"),
        ("ella.bailey", "ella.bailey@sky.local", "Password123", "Ella", "Bailey", "07000 000016"),
        ("henry.cox", "henry.cox@sky.local", "Password123", "Henry", "Cox", "07000 000017"),
        ("sophie.gray", "sophie.gray@sky.local", "Password123", "Sophie", "Gray", "07000 000018"),
        ("jack.morris", "jack.morris@sky.local", "Password123", "Jack", "Morris", "07000 000019"),
        ("chloe.bell", "chloe.bell@sky.local", "Password123", "Chloe", "Bell", "07000 000020"),
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
    org, created = Organisation.objects.get_or_create(
        org_name="Sky Engineering"
    )

    # -------------------------
    # MAIN USERS
    # -------------------------
    sebastian = created_users["sebastian.holt"]
    mason = created_users["mason.briggs"]
    olivia = created_users["olivia.carter"]
    james = created_users["james.bennett"]
    emma = created_users["emma.richardson"]
    benjamin = created_users["benjamin.hayes"]
    alexander = created_users["alexander.perry"]
    evelyn = created_users["evelyn.hughes"]

    # -------------------------
    # DEPARTMENTS
    # -------------------------
    dept1, created = Department.objects.get_or_create(
        organisation=org,
        department_name="xTV_Web"
    )
    dept1.dept_leader_user = sebastian
    dept1.save()

    dept2, created = Department.objects.get_or_create(
        organisation=org,
        department_name="Native TVs"
    )
    dept2.dept_leader_user = mason
    dept2.save()

    print("Departments added/updated")

    # -------------------------
    # TEAMS
    # -------------------------
    team1, created = Team.objects.get_or_create(
        department=dept1,
        team_name="Code Warriors"
    )
    team1.manager_user = olivia
    team1.save()

    team2, created = Team.objects.get_or_create(
        department=dept1,
        team_name="Bit Masters"
    )
    team2.manager_user = james
    team2.save()

    team3, created = Team.objects.get_or_create(
        department=dept1,
        team_name="The Debuggers"
    )
    team3.manager_user = benjamin
    team3.save()

    team4, created = Team.objects.get_or_create(
        department=dept2,
        team_name="Data Wranglers"
    )
    team4.manager_user = emma
    team4.save()

    team5, created = Team.objects.get_or_create(
        department=dept2,
        team_name="The Sprint Kings"
    )
    team5.manager_user = alexander
    team5.save()

    team6, created = Team.objects.get_or_create(
        department=dept2,
        team_name="Exception Catchers"
    )
    team6.manager_user = evelyn
    team6.save()

    print("Teams added/updated")

    # -------------------------
    # TEAM MEMBERS
    # -------------------------
    add_team_members(team1, [
        created_users["olivia.carter"],
        created_users["liam.turner"],
        created_users["ava.hughes"],
        created_users["noah.ward"],
        created_users["mia.reed"],
        created_users["ethan.brooks"],
    ])

    add_team_members(team2, [
        created_users["james.bennett"],
        created_users["grace.foster"],
        created_users["lucas.price"],
        created_users["ella.bailey"],
        created_users["henry.cox"],
        created_users["sophie.gray"],
    ])

    add_team_members(team3, [
        created_users["benjamin.hayes"],
        created_users["jack.morris"],
        created_users["chloe.bell"],
        created_users["liam.turner"],
        created_users["ava.hughes"],
        created_users["noah.ward"],
    ])

    add_team_members(team4, [
        created_users["emma.richardson"],
        created_users["mia.reed"],
        created_users["ethan.brooks"],
        created_users["grace.foster"],
        created_users["lucas.price"],
        created_users["ella.bailey"],
    ])

    add_team_members(team5, [
        created_users["alexander.perry"],
        created_users["henry.cox"],
        created_users["sophie.gray"],
        created_users["jack.morris"],
        created_users["chloe.bell"],
        created_users["liam.turner"],
    ])

    add_team_members(team6, [
        created_users["evelyn.hughes"],
        created_users["ava.hughes"],
        created_users["noah.ward"],
        created_users["mia.reed"],
        created_users["ethan.brooks"],
        created_users["grace.foster"],
    ])

    print("Team members added/updated")
    print("All data added successfully")


if __name__ == "__main__":
    run()