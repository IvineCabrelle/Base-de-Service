--1 Creation des Tables 
--Table Etudiants :

CREATE TABLE Etudiants (
    ID_Etudiant INT PRIMARY KEY,
    Nom_Etudiant VARCHAR(100)
);

--Table Cours :
CREATE TABLE Cours (
    ID_Cours INT PRIMARY KEY,
    Nom_Cours VARCHAR(100),
    Professeur VARCHAR(100),
    Salle VARCHAR(10)
);

--Table Inscriptions :
CREATE TABLE Inscriptions (
    ID_Etudiant INT,
    ID_Cours INT,
    Note INT,
    PRIMARY KEY (ID_Etudiant, ID_Cours),
    FOREIGN KEY (ID_Etudiant) REFERENCES Etudiants(ID_Etudiant),
    FOREIGN KEY (ID_Cours) REFERENCES Cours(ID_Cours)
);

--2 Inserstion des données 
--Table Etudiants :

INSERT INTO Etudiants (ID_Etudiant, Nom_Etudiant) VALUES
(1, 'Alice'),
(2, 'Bob'),
(3, 'Charlie');

--Table Cours :
INSERT INTO Cours (ID_Cours, Nom_Cours, Professeur, Salle) VALUES
(1, 'Mathématiques', 'Prof. Dupont', 'A101'),
(2, 'Histoire', 'Prof. Martin', 'B202'),
(3, 'Science', 'Prof. Bernard', 'C303');

--Table Inscriptions :
INSERT INTO Inscriptions (ID_Etudiant, ID_Cours, Note) VALUES
(1, 1, 85),
(2, 1, 78),
(1, 2, 90),
(3, 1, 92),
(2, 2, 85),
(1, 3, 88);

SELECT * FROM Etudiants;
SELECT * FROM Cours;
SELECT * FROM Inscriptions;

--Ajoutez un étudiant nommé "David" avec l'ID 4.
INSERT INTO Etudiants (ID_Etudiant, Nom_Etudiant) VALUES (4, 'David');

--Inscrivez l'étudiant "David" au cours "Mathématiques" avec une note de 95.
INSERT INTO Inscriptions (ID_Etudiant, ID_Cours, Note) VALUES (4, 1, 95);

--Affichez tous les étudiants inscrits.
SELECT * FROM Etudiants;

--Récupérer toutes les inscriptions :
SELECT e.Nom_Etudiant, c.Nom_Cours, i.Note
FROM Inscriptions i
JOIN Etudiants e ON i.ID_Etudiant = e.ID_Etudiant
JOIN Cours c ON i.ID_Cours = c.ID_Cours;

--Changez la note de "David" en "Mathématiques" de 95 à 97.
UPDATE Inscriptions
SET Note = 97
WHERE ID_Etudiant = 4 AND ID_Cours = 1;

--Changez le nom du cours "Science" en "Physique".
UPDATE Cours
SET Nom_Cours = 'Physique'
WHERE ID_Cours = 3;

--Supprimez l'inscription de "Bob" au cours "Histoire".
DELETE FROM Inscriptions
WHERE ID_Etudiant = 2 AND ID_Cours = 2;

--Supprimez l'étudiant "Charlie" et toutes ses inscriptions.
DELETE FROM Inscriptions
WHERE ID_Etudiant = 3;

DELETE FROM Etudiants
WHERE ID_Etudiant = 3;

SELECT * FROM Etudiants;
SELECT * FROM Cours;
SELECT * FROM Inscriptions;



