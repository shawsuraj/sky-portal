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

INSERT INTO Organisation VALUES (1, 'Sky Engineering');

-- Users
INSERT INTO "User" VALUES ('U001','olivia.carter','olivia.carter@sky.local','hash123','Olivia Carter','Team Leader');
INSERT INTO "User" VALUES ('U002','sebastian.holt','sebastian.holt@sky.local','hash123','Sebastian Holt','Department Head');
INSERT INTO "User" VALUES ('U003','james.bennett','james.bennett@sky.local','hash123','James Bennett','Team Leader');
INSERT INTO "User" VALUES ('U004','emma.richardson','emma.richardson@sky.local','hash123','Emma Richardson','Team Leader');
INSERT INTO "User" VALUES ('U005','benjamin.hayes','benjamin.hayes@sky.local','hash123','Benjamin Hayes','Team Leader');
INSERT INTO "User" VALUES ('U006','sophia.mitchell','sophia.mitchell@sky.local','hash123','Sophia Mitchell','Team Leader');
INSERT INTO "User" VALUES ('U007','william.cooper','william.cooper@sky.local','hash123','William Cooper','Team Leader');
INSERT INTO "User" VALUES ('U008','isabella.ross','isabella.ross@sky.local','hash123','Isabella Ross','Team Leader');
INSERT INTO "User" VALUES ('U009','elijah.parker','elijah.parker@sky.local','hash123','Elijah Parker','Team Leader');
INSERT INTO "User" VALUES ('U010','ava.sullivan','ava.sullivan@sky.local','hash123','Ava Sullivan','Team Leader');
INSERT INTO "User" VALUES ('U011','noah.campbell','noah.campbell@sky.local','hash123','Noah Campbell','Team Leader');
INSERT INTO "User" VALUES ('U012','mia.henderson','mia.henderson@sky.local','hash123','Mia Henderson','Team Leader');
INSERT INTO "User" VALUES ('U013','nora.chandler','nora.chandler@sky.local','hash123','Nora Chandler','Department Head');
INSERT INTO "User" VALUES ('U014','lucas.foster','lucas.foster@sky.local','hash123','Lucas Foster','Team Leader');
INSERT INTO "User" VALUES ('U015','charlotte.murphy','charlotte.murphy@sky.local','hash123','Charlotte Murphy','Team Leader');
INSERT INTO "User" VALUES ('U016','henry.ward','henry.ward@sky.local','hash123','Henry Ward','Team Leader');
INSERT INTO "User" VALUES ('U017','amelia.brooks','amelia.brooks@sky.local','hash123','Amelia Brooks','Team Leader');

INSERT INTO "User" VALUES ('U018','alexander.perry','alexander.perry@sky.local','hash123','Alexander Perry','Team Leader');
INSERT INTO "User" VALUES ('U019','mason.briggs','mason.briggs@sky.local','hash123','Mason Briggs','Department Head');
INSERT INTO "User" VALUES ('U020','evelyn.hughes','evelyn.hughes@sky.local','hash123','Evelyn Hughes','Team Leader');
INSERT INTO "User" VALUES ('U021','daniel.scott','daniel.scott@sky.local','hash123','Daniel Scott','Team Leader');
INSERT INTO "User" VALUES ('U022','harper.lewis','harper.lewis@sky.local','hash123','Harper Lewis','Team Leader');
INSERT INTO "User" VALUES ('U023','matthew.reed','matthew.reed@sky.local','hash123','Matthew Reed','Team Leader');
INSERT INTO "User" VALUES ('U024','scarlett.edwards','scarlett.edwards@sky.local','hash123','Scarlett Edwards','Team Leader');
INSERT INTO "User" VALUES ('U025','jack.turner','jack.turner@sky.local','hash123','Jack Turner','Team Leader');
INSERT INTO "User" VALUES ('U026','lily.phillips','lily.phillips@sky.local','hash123','Lily Phillips','Team Leader');
INSERT INTO "User" VALUES ('U027','samuel.morgan','samuel.morgan@sky.local','hash123','Samuel Morgan','Team Leader');
INSERT INTO "User" VALUES ('U028','grace.patterson','grace.patterson@sky.local','hash123','Grace Patterson','Team Leader');

INSERT INTO "User" VALUES ('U029','owen.barnes','owen.barnes@sky.local','hash123','Owen Barnes','Team Leader');
INSERT INTO "User" VALUES ('U030','violet.ramsey','violet.ramsey@sky.local','hash123','Violet Ramsey','Department Head');
INSERT INTO "User" VALUES ('U031','chloe.hall','chloe.hall@sky.local','hash123','Chloe Hall','Team Leader');
INSERT INTO "User" VALUES ('U032','nathan.fisher','nathan.fisher@sky.local','hash123','Nathan Fisher','Team Leader');
INSERT INTO "User" VALUES ('U033','zoey.stevens','zoey.stevens@sky.local','hash123','Zoey Stevens','Team Leader');
INSERT INTO "User" VALUES ('U034','caleb.bryant','caleb.bryant@sky.local','hash123','Caleb Bryant','Team Leader');
INSERT INTO "User" VALUES ('U035','hannah.simmons','hannah.simmons@sky.local','hash123','Hannah Simmons','Team Leader');
INSERT INTO "User" VALUES ('U036','isaac.jenkins','isaac.jenkins@sky.local','hash123','Isaac Jenkins','Team Leader');
INSERT INTO "User" VALUES ('U037','madison.clarke','madison.clarke@sky.local','hash123','Madison Clarke','Team Leader');
INSERT INTO "User" VALUES ('U038','gabriel.coleman','gabriel.coleman@sky.local','hash123','Gabriel Coleman','Team Leader');
INSERT INTO "User" VALUES ('U039','riley.sanders','riley.sanders@sky.local','hash123','Riley Sanders','Team Leader');
INSERT INTO "User" VALUES ('U040','leo.watson','leo.watson@sky.local','hash123','Leo Watson','Team Leader');
INSERT INTO "User" VALUES ('U041','victoria.price','victoria.price@sky.local','hash123','Victoria Price','Team Leader');
INSERT INTO "User" VALUES ('U042','adam.sinclair','adam.sinclair@sky.local','hash123','Adam Sinclair','Department Head');
INSERT INTO "User" VALUES ('U043','julian.bell','julian.bell@sky.local','hash123','Julian Bell','Team Leader');

INSERT INTO "User" VALUES ('U044','layla.russell','layla.russell@sky.local','hash123','Layla Russell','Team Leader');
INSERT INTO "User" VALUES ('U045','lucy.vaughn','lucy.vaughn@sky.local','hash123','Lucy Vaughn','Department Head');
INSERT INTO "User" VALUES ('U046','ethan.griffin','ethan.griffin@sky.local','hash123','Ethan Griffin','Team Leader');
INSERT INTO "User" VALUES ('U047','aurora.cooper','aurora.cooper@sky.local','hash123','Aurora Cooper','Team Leader');
INSERT INTO "User" VALUES ('U048','dylan.spencer','dylan.spencer@sky.local','hash123','Dylan Spencer','Team Leader');
INSERT INTO "User" VALUES ('U049','stella.martinez','stella.martinez@sky.local','hash123','Stella Martinez','Team Leader');

INSERT INTO "User" VALUES ('U050','levi.bishop','levi.bishop@sky.local','hash123','Levi Bishop','Team Leader');
INSERT INTO "User" VALUES ('U051','theodore.knox','theodore.knox@sky.local','hash123','Theodore Knox','Department Head');
INSERT INTO "User" VALUES ('U052','eleanor.freeman','eleanor.freeman@sky.local','hash123','Eleanor Freeman','Team Leader');

INSERT INTO "User" VALUES ('U053','hudson.ford','hudson.ford@sky.local','hash123','Hudson Ford','Team Leader');
INSERT INTO "User" VALUES ('U054','bella.monroe','bella.monroe@sky.local','hash123','Bella Monroe','Department Head');

-- Departments
INSERT INTO Department VALUES (1,1,'xTV_Web','U002');
INSERT INTO Department VALUES (2,1,'Native TVs','U019');
INSERT INTO Department VALUES (3,1,'Mobile','U030');
INSERT INTO Department VALUES (4,1,'Reliability_Tool','U045');
INSERT INTO Department VALUES (5,1,'Arch','U051');
INSERT INTO Department VALUES (6,1,'Programme','U054');

-- Teams
INSERT INTO Team VALUES (1,1,'U001','Code Warriors','Active','Client Lightning Xtv');
INSERT INTO Team VALUES (2,1,'U003','The Debuggers','Active','Client Lightning Xtv');
INSERT INTO Team VALUES (3,1,'U004','Bit Masters','Active','Client Lightning Xtv');
INSERT INTO Team VALUES (4,1,'U005','Agile Avengers','Active','Client Lightning Xtv');
INSERT INTO Team VALUES (5,1,'U006','Syntax Squad','Active','Client Lightning Xtv');
INSERT INTO Team VALUES (6,1,'U007','The Codebreakers','Active','Client Lightning Xtv');
INSERT INTO Team VALUES (7,1,'U008','DevOps Dynasty','Active',NULL);
INSERT INTO Team VALUES (8,1,'U009','Byte Force','Active','Client Lightning Xtv');
INSERT INTO Team VALUES (9,1,'U010','The Cloud Architects','Active','Client Lightning Xtv');
INSERT INTO Team VALUES (10,1,'U011','Full Stack Ninjas','Active','Client Lightning Xtv');
INSERT INTO Team VALUES (11,1,'U012','The Error Handlers','Active','Client Web');
INSERT INTO Team VALUES (12,1,'U014','Stack Overflow Survivors','Active','Client Web');
INSERT INTO Team VALUES (13,1,'U015','The Binary Beasts','Active','Client Web');
INSERT INTO Team VALUES (14,1,'U016','API Avengers','Active','Client Web');
INSERT INTO Team VALUES (15,1,'U017','The Algorithm Alliance','Active','Client Web');

INSERT INTO Team VALUES (16,2,'U018','Data Wranglers','Active','Client Roku TV');
INSERT INTO Team VALUES (17,2,'U020','The Sprint Kings','Active','Client Roku TV');
INSERT INTO Team VALUES (18,2,'U021','Exception Catchers','Active','Client Roku TV');
INSERT INTO Team VALUES (19,2,'U022','Code Monkeys','Active','Client Roku TV');
INSERT INTO Team VALUES (20,2,'U023','The Compile Crew','Active','Client Roku TV');
INSERT INTO Team VALUES (21,2,'U024','Git Good','Active','Client Apple TV');
INSERT INTO Team VALUES (22,2,'U025','The CI/CD Squad','Active','Client Apple TV');
INSERT INTO Team VALUES (23,2,'U026','Bug Exterminators','Active','Client Apple TV');
INSERT INTO Team VALUES (24,2,'U027','The Agile Alchemists','Active','Client Apple TV');
INSERT INTO Team VALUES (25,2,'U028','The Hotfix Heroes','Active','Client Apple TV');

INSERT INTO Team VALUES (26,3,'U029','Cache Me Outside','Active','Client Mobile');
INSERT INTO Team VALUES (27,3,'U031','The Scrum Lords','Active','Client Mobile');
INSERT INTO Team VALUES (28,3,'U032','The 404 Not Found','Active','Client Mobile');
INSERT INTO Team VALUES (29,3,'U033','The Version Controllers','Active','Client Mobile');
INSERT INTO Team VALUES (30,3,'U034','DevNull Pioneers','Active','Client Mobile');
INSERT INTO Team VALUES (31,3,'U035','The Code Refactors','Active','Client Mobile Commerce');
INSERT INTO Team VALUES (32,3,'U036','The Jenkins Juggernauts','Active','Client Mobile');
INSERT INTO Team VALUES (33,3,'U037','Infinite Loopers','Active','Client Mobile');
INSERT INTO Team VALUES (34,3,'U038','The Feature Crafters','Active','Client Mobile');
INSERT INTO Team VALUES (35,3,'U039','The Bit Manipulators','Active','Client Mobile');
INSERT INTO Team VALUES (36,3,'U040','Kernel Crushers','Active','Client Mobile');
INSERT INTO Team VALUES (37,3,'U041','The Git Masters','Active',NULL);
INSERT INTO Team VALUES (38,3,'U043','The API Explorers','Active','Client Automation QA');

INSERT INTO Team VALUES (39,4,'U044','The Lambda Legends','Active',NULL);
INSERT INTO Team VALUES (40,4,'U046','The Encryption Squad','Active','Client Device as a Service');
INSERT INTO Team VALUES (41,4,'U047','The UX Wizards','Active','Client SRE');
INSERT INTO Team VALUES (42,4,'U048','The Hackathon Hustlers','Active','Client Apps Tooling');
INSERT INTO Team VALUES (43,4,'U049','The Frontend Phantoms','Active',NULL);

INSERT INTO Team VALUES (44,5,'U050','The Dev Dragons','Active','Client CLIP Backend for Frontend');
INSERT INTO Team VALUES (45,5,'U052','The Microservice Mavericks','Active','Client Support');

INSERT INTO Team VALUES (46,6,'U053','The Quantum Coders','Active',NULL);

-- Team members
INSERT INTO Team_Member VALUES (1,'U001','Leader');
INSERT INTO Team_Member VALUES (2,'U003','Leader');
INSERT INTO Team_Member VALUES (3,'U004','Leader');
INSERT INTO Team_Member VALUES (4,'U005','Leader');
INSERT INTO Team_Member VALUES (5,'U006','Leader');
INSERT INTO Team_Member VALUES (6,'U007','Leader');
INSERT INTO Team_Member VALUES (7,'U008','Leader');
INSERT INTO Team_Member VALUES (8,'U009','Leader');
INSERT INTO Team_Member VALUES (9,'U010','Leader');
INSERT INTO Team_Member VALUES (10,'U011','Leader');
INSERT INTO Team_Member VALUES (11,'U012','Leader');
INSERT INTO Team_Member VALUES (12,'U014','Leader');
INSERT INTO Team_Member VALUES (13,'U015','Leader');
INSERT INTO Team_Member VALUES (14,'U016','Leader');
INSERT INTO Team_Member VALUES (15,'U017','Leader');
INSERT INTO Team_Member VALUES (16,'U018','Leader');
INSERT INTO Team_Member VALUES (17,'U020','Leader');
INSERT INTO Team_Member VALUES (18,'U021','Leader');
INSERT INTO Team_Member VALUES (19,'U022','Leader');
INSERT INTO Team_Member VALUES (20,'U023','Leader');
INSERT INTO Team_Member VALUES (21,'U024','Leader');
INSERT INTO Team_Member VALUES (22,'U025','Leader');
INSERT INTO Team_Member VALUES (23,'U026','Leader');
INSERT INTO Team_Member VALUES (24,'U027','Leader');
INSERT INTO Team_Member VALUES (25,'U028','Leader');
INSERT INTO Team_Member VALUES (26,'U029','Leader');
INSERT INTO Team_Member VALUES (27,'U031','Leader');
INSERT INTO Team_Member VALUES (28,'U032','Leader');
INSERT INTO Team_Member VALUES (29,'U033','Leader');
INSERT INTO Team_Member VALUES (30,'U034','Leader');
INSERT INTO Team_Member VALUES (31,'U035','Leader');
INSERT INTO Team_Member VALUES (32,'U036','Leader');
INSERT INTO Team_Member VALUES (33,'U037','Leader');
INSERT INTO Team_Member VALUES (34,'U038','Leader');
INSERT INTO Team_Member VALUES (35,'U039','Leader');
INSERT INTO Team_Member VALUES (36,'U040','Leader');
INSERT INTO Team_Member VALUES (37,'U041','Leader');
INSERT INTO Team_Member VALUES (38,'U043','Leader');
INSERT INTO Team_Member VALUES (39,'U044','Leader');
INSERT INTO Team_Member VALUES (40,'U046','Leader');
INSERT INTO Team_Member VALUES (41,'U047','Leader');
INSERT INTO Team_Member VALUES (42,'U048','Leader');
INSERT INTO Team_Member VALUES (43,'U049','Leader');
INSERT INTO Team_Member VALUES (44,'U050','Leader');
INSERT INTO Team_Member VALUES (45,'U052','Leader');
INSERT INTO Team_Member VALUES (46,'U053','Leader');

COMMIT;
PRAGMA foreign_keys = ON;