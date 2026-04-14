PRAGMA foreign_keys = OFF;
BEGIN TRANSACTION;

-- Table: User
CREATE TABLE IF NOT EXISTS User (
    userID VARCHAR(20) PRIMARY KEY NOT NULL UNIQUE,
    userName VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    passwordHash VARCHAR(255) NOT NULL,
    fullName VARCHAR(100) NOT NULL,
    createdAt TIMESTAMP NOT NULL,
    updatedAt TIMESTAMP NOT NULL,
    userRole VARCHAR(60) NOT NULL
);

-- Table: Organisation
CREATE TABLE IF NOT EXISTS Organisation (
    organisationID INTEGER PRIMARY KEY NOT NULL UNIQUE,
    orgName VARCHAR(200) NOT NULL UNIQUE
);

-- Table: Department
CREATE TABLE IF NOT EXISTS Department (
    departmentID INTEGER PRIMARY KEY NOT NULL UNIQUE,
    organisationID INTEGER NOT NULL,
    departmentName VARCHAR(200) NOT NULL,
    deptDescription TEXT NOT NULL,
    deptLeaderUserID VARCHAR(20) NOT NULL,
    FOREIGN KEY (organisationID) REFERENCES Organisation(organisationID),
    FOREIGN KEY (deptLeaderUserID) REFERENCES User(userID)
);

-- Table: Team_Type
CREATE TABLE IF NOT EXISTS Team_Type (
    teamTypeID INTEGER PRIMARY KEY NOT NULL UNIQUE,
    typeName VARCHAR(120) NOT NULL UNIQUE,
    typeDescription TEXT NOT NULL
);

-- Table: Team
CREATE TABLE IF NOT EXISTS Team (
    teamID INTEGER PRIMARY KEY NOT NULL UNIQUE,
    departmentID INTEGER NOT NULL,
    teamTypeID INTEGER NOT NULL,
    managerUserID VARCHAR(20) NOT NULL,
    teamName VARCHAR(200) NOT NULL,
    responsibilities TEXT NOT NULL,
    purpose TEXT NOT NULL,
    description TEXT NOT NULL,
    status VARCHAR(60) NOT NULL,
    createdDate DATE NOT NULL,
    disbandedAt TIMESTAMP,
    FOREIGN KEY (departmentID) REFERENCES Department(departmentID),
    FOREIGN KEY (teamTypeID) REFERENCES Team_Type(teamTypeID),
    FOREIGN KEY (managerUserID) REFERENCES User(userID)
);

-- Table: Repository
CREATE TABLE IF NOT EXISTS Repository (
    repoID INTEGER PRIMARY KEY NOT NULL UNIQUE,
    repoName VARCHAR(200) NOT NULL,
    repoUrl TEXT NOT NULL,
    platform VARCHAR(80) NOT NULL
);

-- Table: Skill
CREATE TABLE IF NOT EXISTS Skill (
    skillID INTEGER PRIMARY KEY NOT NULL UNIQUE,
    skillName VARCHAR(120) NOT NULL UNIQUE,
    skillDescription TEXT NOT NULL
);

-- Table: Meeting
CREATE TABLE IF NOT EXISTS Meeting (
    meetingID INTEGER PRIMARY KEY NOT NULL UNIQUE,
    createdByUserID VARCHAR(20) NOT NULL,
    teamID INTEGER NOT NULL,
    title VARCHAR(200) NOT NULL,
    meetingDateTime TIMESTAMP NOT NULL,
    platform VARCHAR(120) NOT NULL,
    agendaMessage TEXT NOT NULL,
    createdAt TIMESTAMP,
    FOREIGN KEY (createdByUserID) REFERENCES User(userID),
    FOREIGN KEY (teamID) REFERENCES Team(teamID)
);

-- Table: Meeting_Attendee
CREATE TABLE IF NOT EXISTS Meeting_Attendee (
    meetingID INTEGER NOT NULL,
    userID VARCHAR(20) NOT NULL,
    attendanceStatus VARCHAR(20) NOT NULL,
    respondedAt TIMESTAMP,
    PRIMARY KEY (meetingID, userID),
    FOREIGN KEY (meetingID) REFERENCES Meeting(meetingID),
    FOREIGN KEY (userID) REFERENCES User(userID)
);

-- Table: Message
CREATE TABLE IF NOT EXISTS Message (
    messageID INTEGER PRIMARY KEY NOT NULL UNIQUE,
    senderUserID VARCHAR(20) NOT NULL,
    subject VARCHAR(200) NOT NULL,
    body TEXT NOT NULL,
    sentAt TIMESTAMP,
    status VARCHAR(60) NOT NULL,
    FOREIGN KEY (senderUserID) REFERENCES User(userID)
);

-- Table: Message_Recipient
CREATE TABLE IF NOT EXISTS Message_Recipient (
    messageID INTEGER NOT NULL,
    recipientUserID VARCHAR(20) NOT NULL,
    folder VARCHAR(60) NOT NULL,
    read_at TIMESTAMP,
    PRIMARY KEY (messageID, recipientUserID),
    FOREIGN KEY (messageID) REFERENCES Message(messageID),
    FOREIGN KEY (recipientUserID) REFERENCES User(userID)
);

-- Table: Audit_Log
CREATE TABLE IF NOT EXISTS Audit_Log (
    auditID INTEGER PRIMARY KEY NOT NULL UNIQUE,
    actorUserID VARCHAR(20) NOT NULL,
    entityType VARCHAR(120) NOT NULL,
    entityID INTEGER NOT NULL,
    action VARCHAR(120) NOT NULL,
    changeSummary TEXT NOT NULL,
    createdAt TIMESTAMP NOT NULL,
    FOREIGN KEY (actorUserID) REFERENCES User(userID)
);

-- Table: Team_Dependency
CREATE TABLE IF NOT EXISTS Team_Dependency (
    upstreamTeamID INTEGER NOT NULL,
    downstreamTeamID INTEGER NOT NULL,
    dependencyType TEXT NOT NULL,
    dependencyDescription TEXT NOT NULL,
    createdAt TIMESTAMP NOT NULL,
    PRIMARY KEY (upstreamTeamID, downstreamTeamID),
    FOREIGN KEY (upstreamTeamID) REFERENCES Team(teamID),
    FOREIGN KEY (downstreamTeamID) REFERENCES Team(teamID)
);

-- Table: Team_Member
CREATE TABLE IF NOT EXISTS Team_Member (
    teamID INTEGER NOT NULL,
    userID VARCHAR(20) NOT NULL,
    userRole VARCHAR(60) NOT NULL,
    joinedDate DATE NOT NULL,
    leftDate DATE,
    PRIMARY KEY (teamID, userID),
    FOREIGN KEY (teamID) REFERENCES Team(teamID),
    FOREIGN KEY (userID) REFERENCES User(userID)
);

-- Table: Team_Repository
CREATE TABLE IF NOT EXISTS Team_Repository (
    teamID INTEGER NOT NULL,
    repoID INTEGER NOT NULL,
    purpose_notes TEXT,
    PRIMARY KEY (teamID, repoID),
    FOREIGN KEY (teamID) REFERENCES Team(teamID),
    FOREIGN KEY (repoID) REFERENCES Repository(repoID)
);

-- Table: Team_Skill
CREATE TABLE IF NOT EXISTS Team_Skill (
    teamID INTEGER NOT NULL,
    skillID INTEGER NOT NULL,
    level NUMERIC,
    PRIMARY KEY (teamID, skillID),
    FOREIGN KEY (teamID) REFERENCES Team(teamID),
    FOREIGN KEY (skillID) REFERENCES Skill(skillID)
);

COMMIT TRANSACTION;
PRAGMA foreign_keys = ON;