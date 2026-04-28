PRAGMA foreign_keys = OFF;
BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS "User" (
    userID VARCHAR(20) PRIMARY KEY,
    userName VARCHAR(50) UNIQUE,
    email VARCHAR(255) UNIQUE,
    passwordHash VARCHAR(255),
    fullName VARCHAR(100),
    userRole VARCHAR(60)
);

CREATE TABLE IF NOT EXISTS Organisation (
    organisationID INTEGER PRIMARY KEY,
    orgName VARCHAR(200) UNIQUE
);

CREATE TABLE IF NOT EXISTS Department (
    departmentID INTEGER PRIMARY KEY,
    organisationID INTEGER,
    departmentName VARCHAR(200),
    deptLeaderUserID VARCHAR(20),
    FOREIGN KEY (organisationID) REFERENCES Organisation(organisationID),
    FOREIGN KEY (deptLeaderUserID) REFERENCES "User"(userID)
);

CREATE TABLE IF NOT EXISTS Team (
    teamID INTEGER PRIMARY KEY,
    departmentID INTEGER,
    managerUserID VARCHAR(20),
    teamName VARCHAR(200),
    status VARCHAR(60),
    jiraProjectName VARCHAR(200),
    FOREIGN KEY (departmentID) REFERENCES Department(departmentID),
    FOREIGN KEY (managerUserID) REFERENCES "User"(userID)
);

CREATE TABLE IF NOT EXISTS Team_Member (
    teamID INTEGER,
    userID VARCHAR(20),
    userRole VARCHAR(60),
    PRIMARY KEY (teamID, userID),
    FOREIGN KEY (teamID) REFERENCES Team(teamID),
    FOREIGN KEY (userID) REFERENCES "User"(userID)
);

-- =========================================
-- ORGANISATION
-- =========================================
INSERT INTO Organisation VALUES (1, 'Sky Engineering');

-- =========================================
-- USERS
-- password for all users = Password123
-- =========================================

-- Department Heads
INSERT INTO "User" VALUES ('U001','sebastian.holt','sebastian.holt@sky.local','Password123','Sebastian Holt','Department Head');
INSERT INTO "User" VALUES ('U002','mason.briggs','mason.briggs@sky.local','Password123','Mason Briggs','Department Head');

-- Team Leaders
INSERT INTO "User" VALUES ('U003','olivia.carter','olivia.carter@sky.local','Password123','Olivia Carter','Team Leader');
INSERT INTO "User" VALUES ('U004','james.bennett','james.bennett@sky.local','Password123','James Bennett','Team Leader');
INSERT INTO "User" VALUES ('U005','emma.richardson','emma.richardson@sky.local','Password123','Emma Richardson','Team Leader');
INSERT INTO "User" VALUES ('U006','benjamin.hayes','benjamin.hayes@sky.local','Password123','Benjamin Hayes','Team Leader');

INSERT INTO "User" VALUES ('U007','alexander.perry','alexander.perry@sky.local','Password123','Alexander Perry','Team Leader');
INSERT INTO "User" VALUES ('U008','evelyn.hughes','evelyn.hughes@sky.local','Password123','Evelyn Hughes','Team Leader');
INSERT INTO "User" VALUES ('U009','daniel.scott','daniel.scott@sky.local','Password123','Daniel Scott','Team Leader');
INSERT INTO "User" VALUES ('U010','harper.lewis','harper.lewis@sky.local','Password123','Harper Lewis','Team Leader');

-- xTV_Web engineers
INSERT INTO "User" VALUES ('U011','liam.turner','liam.turner@sky.local','Password123','Liam Turner','DevOps Engineer');
INSERT INTO "User" VALUES ('U012','ava.hughes','ava.hughes@sky.local','Password123','Ava Hughes','Cloud Engineer');
INSERT INTO "User" VALUES ('U013','noah.ward','noah.ward@sky.local','Password123','Noah Ward','Platform Engineer');
INSERT INTO "User" VALUES ('U014','mia.reed','mia.reed@sky.local','Password123','Mia Reed','Site Reliability Engineer');
INSERT INTO "User" VALUES ('U015','ethan.brooks','ethan.brooks@sky.local','Password123','Ethan Brooks','Infrastructure Engineer');

INSERT INTO "User" VALUES ('U016','grace.foster','grace.foster@sky.local','Password123','Grace Foster','Debug Engineer');
INSERT INTO "User" VALUES ('U017','lucas.price','lucas.price@sky.local','Password123','Lucas Price','Software Engineer');
INSERT INTO "User" VALUES ('U018','ella.bailey','ella.bailey@sky.local','Password123','Ella Bailey','Observability Engineer');
INSERT INTO "User" VALUES ('U019','henry.cox','henry.cox@sky.local','Password123','Henry Cox','QA Automation Engineer');
INSERT INTO "User" VALUES ('U020','sophie.gray','sophie.gray@sky.local','Password123','Sophie Gray','Support Engineer');

INSERT INTO "User" VALUES ('U021','jack.morris','jack.morris@sky.local','Password123','Jack Morris','Security Engineer');
INSERT INTO "User" VALUES ('U022','chloe.bell','chloe.bell@sky.local','Password123','Chloe Bell','Compliance Engineer');
INSERT INTO "User" VALUES ('U023','harry.kelly','harry.kelly@sky.local','Password123','Harry Kelly','Backend Engineer');
INSERT INTO "User" VALUES ('U024','isla.russell','isla.russell@sky.local','Password123','Isla Russell','Penetration Tester');
INSERT INTO "User" VALUES ('U025','oscar.wood','oscar.wood@sky.local','Password123','Oscar Wood','Encryption Engineer');

INSERT INTO "User" VALUES ('U026','amelia.davis','amelia.davis@sky.local','Password123','Amelia Davis','Agile Engineer');
INSERT INTO "User" VALUES ('U027','leo.harris','leo.harris@sky.local','Password123','Leo Harris','Delivery Engineer');
INSERT INTO "User" VALUES ('U028','scarlett.king','scarlett.king@sky.local','Password123','Scarlett King','Release Engineer');
INSERT INTO "User" VALUES ('U029','arthur.evans','arthur.evans@sky.local','Password123','Arthur Evans','Process Engineer');
INSERT INTO "User" VALUES ('U030','lily.cole','lily.cole@sky.local','Password123','Lily Cole','Project Engineer');

-- Native TVs engineers
INSERT INTO "User" VALUES ('U031','freddie.baker','freddie.baker@sky.local','Password123','Freddie Baker','Data Engineer');
INSERT INTO "User" VALUES ('U032','eva.ross','eva.ross@sky.local','Password123','Eva Ross','ETL Engineer');
INSERT INTO "User" VALUES ('U033','alfie.hall','alfie.hall@sky.local','Password123','Alfie Hall','Analytics Engineer');
INSERT INTO "User" VALUES ('U034','ruby.turner','ruby.turner@sky.local','Password123','Ruby Turner','Database Engineer');
INSERT INTO "User" VALUES ('U035','theo.ward','theo.ward@sky.local','Password123','Theo Ward','Streaming Engineer');

INSERT INTO "User" VALUES ('U036','ivy.scott','ivy.scott@sky.local','Password123','Ivy Scott','Scrum Engineer');
INSERT INTO "User" VALUES ('U037','archie.mitchell','archie.mitchell@sky.local','Password123','Archie Mitchell','Delivery Engineer');
INSERT INTO "User" VALUES ('U038','poppy.campbell','poppy.campbell@sky.local','Password123','Poppy Campbell','Release Engineer');
INSERT INTO "User" VALUES ('U039','george.bailey','george.bailey@sky.local','Password123','George Bailey','Project Engineer');
INSERT INTO "User" VALUES ('U040','rosie.hughes','rosie.hughes@sky.local','Password123','Rosie Hughes','Agile Engineer');

INSERT INTO "User" VALUES ('U041','hannah.sanders','hannah.sanders@sky.local','Password123','Hannah Sanders','SRE Engineer');
INSERT INTO "User" VALUES ('U042','isaac.jenkins','isaac.jenkins@sky.local','Password123','Isaac Jenkins','Incident Engineer');
INSERT INTO "User" VALUES ('U043','madison.clarke','madison.clarke@sky.local','Password123','Madison Clarke','Reliability Engineer');
INSERT INTO "User" VALUES ('U044','gabriel.coleman','gabriel.coleman@sky.local','Password123','Gabriel Coleman','Recovery Engineer');
INSERT INTO "User" VALUES ('U045','riley.sanders','riley.sanders@sky.local','Password123','Riley Sanders','Monitoring Engineer');

INSERT INTO "User" VALUES ('U046','victoria.price','victoria.price@sky.local','Password123','Victoria Price','Patch Engineer');
INSERT INTO "User" VALUES ('U047','julian.bell','julian.bell@sky.local','Password123','Julian Bell','Build Engineer');
INSERT INTO "User" VALUES ('U048','mia.owens','mia.owens@sky.local','Password123','Mia Owens','Automation Engineer');
INSERT INTO "User" VALUES ('U049','logan.fisher','logan.fisher@sky.local','Password123','Logan Fisher','CI/CD Engineer');
INSERT INTO "User" VALUES ('U050','ella.morgan','ella.morgan@sky.local','Password123','Ella Morgan','Rollback Engineer');

-- =========================================
-- DEPARTMENTS
-- =========================================
INSERT INTO Department VALUES (1,1,'xTV_Web','U001');
INSERT INTO Department VALUES (2,1,'Native TVs','U002');

-- =========================================
-- TEAMS
-- =========================================
INSERT INTO Team VALUES (1,1,'U003','Code Warriors','Active','Client Lightning Xtv');
INSERT INTO Team VALUES (2,1,'U004','The Debuggers','Active','Client Lightning Xtv');
INSERT INTO Team VALUES (3,1,'U005','Bit Masters','Active','Client Lightning Xtv');
INSERT INTO Team VALUES (4,1,'U006','Agile Avengers','Active','Client Lightning Xtv');

INSERT INTO Team VALUES (5,2,'U007','Data Wranglers','Active','Client Roku TV');
INSERT INTO Team VALUES (6,2,'U008','The Sprint Kings','Active','Client Roku TV');
INSERT INTO Team VALUES (7,2,'U009','Exception Catchers','Active','Client Roku TV');
INSERT INTO Team VALUES (8,2,'U010','Code Monkeys','Active','Client Roku TV');

-- =========================================
-- TEAM MEMBERS
-- each team = 1 leader + 5 engineers
-- =========================================
INSERT INTO Team_Member VALUES (1,'U003','Team Leader');
INSERT INTO Team_Member VALUES (1,'U011','DevOps Engineer');
INSERT INTO Team_Member VALUES (1,'U012','Cloud Engineer');
INSERT INTO Team_Member VALUES (1,'U013','Platform Engineer');
INSERT INTO Team_Member VALUES (1,'U014','Site Reliability Engineer');
INSERT INTO Team_Member VALUES (1,'U015','Infrastructure Engineer');

INSERT INTO Team_Member VALUES (2,'U004','Team Leader');
INSERT INTO Team_Member VALUES (2,'U016','Debug Engineer');
INSERT INTO Team_Member VALUES (2,'U017','Software Engineer');
INSERT INTO Team_Member VALUES (2,'U018','Observability Engineer');
INSERT INTO Team_Member VALUES (2,'U019','QA Automation Engineer');
INSERT INTO Team_Member VALUES (2,'U020','Support Engineer');

INSERT INTO Team_Member VALUES (3,'U005','Team Leader');
INSERT INTO Team_Member VALUES (3,'U021','Security Engineer');
INSERT INTO Team_Member VALUES (3,'U022','Compliance Engineer');
INSERT INTO Team_Member VALUES (3,'U023','Backend Engineer');
INSERT INTO Team_Member VALUES (3,'U024','Penetration Tester');
INSERT INTO Team_Member VALUES (3,'U025','Encryption Engineer');

INSERT INTO Team_Member VALUES (4,'U006','Team Leader');
INSERT INTO Team_Member VALUES (4,'U026','Agile Engineer');
INSERT INTO Team_Member VALUES (4,'U027','Delivery Engineer');
INSERT INTO Team_Member VALUES (4,'U028','Release Engineer');
INSERT INTO Team_Member VALUES (4,'U029','Process Engineer');
INSERT INTO Team_Member VALUES (4,'U030','Project Engineer');

INSERT INTO Team_Member VALUES (5,'U007','Team Leader');
INSERT INTO Team_Member VALUES (5,'U031','Data Engineer');
INSERT INTO Team_Member VALUES (5,'U032','ETL Engineer');
INSERT INTO Team_Member VALUES (5,'U033','Analytics Engineer');
INSERT INTO Team_Member VALUES (5,'U034','Database Engineer');
INSERT INTO Team_Member VALUES (5,'U035','Streaming Engineer');

INSERT INTO Team_Member VALUES (6,'U008','Team Leader');
INSERT INTO Team_Member VALUES (6,'U036','Scrum Engineer');
INSERT INTO Team_Member VALUES (6,'U037','Delivery Engineer');
INSERT INTO Team_Member VALUES (6,'U038','Release Engineer');
INSERT INTO Team_Member VALUES (6,'U039','Project Engineer');
INSERT INTO Team_Member VALUES (6,'U040','Agile Engineer');

INSERT INTO Team_Member VALUES (7,'U009','Team Leader');
INSERT INTO Team_Member VALUES (7,'U041','SRE Engineer');
INSERT INTO Team_Member VALUES (7,'U042','Incident Engineer');
INSERT INTO Team_Member VALUES (7,'U043','Reliability Engineer');
INSERT INTO Team_Member VALUES (7,'U044','Recovery Engineer');
INSERT INTO Team_Member VALUES (7,'U045','Monitoring Engineer');

INSERT INTO Team_Member VALUES (8,'U010','Team Leader');
INSERT INTO Team_Member VALUES (8,'U046','Patch Engineer');
INSERT INTO Team_Member VALUES (8,'U047','Build Engineer');
INSERT INTO Team_Member VALUES (8,'U048','Automation Engineer');
INSERT INTO Team_Member VALUES (8,'U049','CI/CD Engineer');
INSERT INTO Team_Member VALUES (8,'U050','Rollback Engineer');

COMMIT;
PRAGMA foreign_keys = ON; 