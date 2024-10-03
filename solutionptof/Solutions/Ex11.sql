--1 Creation des Tables 
--Table Clients :
CREATE TABLE Clients (
    ID_Client INT PRIMARY KEY,
    Nom_Client VARCHAR(100),
    Adresse_Client VARCHAR(255)
);


--Table Voitures :
CREATE TABLE Voitures (
    ID_Voiture INT PRIMARY KEY,
    Marque VARCHAR(100),
    Modèle VARCHAR(100),
    Année INT,
    Couleur VARCHAR(50),
    Prix DECIMAL(10, 2)
);


--Table Ventes :
CREATE TABLE Ventes (
    ID_Vente INT PRIMARY KEY,
    ID_Client INT,
    ID_Voiture INT,
    Date_Vente DATE,
    FOREIGN KEY (ID_Client) REFERENCES Clients(ID_Client),
    FOREIGN KEY (ID_Voiture) REFERENCES Voitures(ID_Voiture)
);


--2 Inserstion des données 
--Table Clients :

INSERT INTO Clients (ID_Client, Nom_Client, Adresse_Client) VALUES
(1, 'Alice', '123 Rue A'),
(2, 'Bob', '456 Rue B'),
(3, 'Charlie', '789 Rue C');


--Table Voitures :
INSERT INTO Voitures (ID_Voiture, Marque, Modèle, Année, Couleur, Prix) VALUES
(101, 'Toyota', 'Corolla', 2020, 'Rouge', 20000),
(102, 'Honda', 'Civic', 2019, 'Bleu', 18000),
(103, 'Ford', 'Fiesta', 2021, 'Noir', 22000),
(104, 'Nissan', 'Sentra', 2022, 'Blanc', 21000);


--Table Ventes :
INSERT INTO Ventes (ID_Vente, ID_Client, ID_Voiture, Date_Vente) VALUES
(1, 1, 101, '2023-01-15'),
(2, 2, 102, '2023-02-20'),
(3, 3, 103, '2023-03-10'),
(4, 1, 104, '2023-04-05');


--Ajoutez un client nommé "David" avec l'ID 4 et l'adresse "321 Rue D".
INSERT INTO Clients (ID_Client, Nom_Client, Adresse_Client) VALUES (4, 'David', '321 Rue D');

--IAjoutez une vente pour le client "David" de la voiture "Toyota Corolla" le 2023-05-15.
INSERT INTO Ventes (ID_Vente, ID_Client, ID_Voiture, Date_Vente) VALUES (5, 4, 101, '2023-05-15');

--Affichez tous les clients inscrits.

SELECT * FROM Clients;


--Affichez toutes les ventes avec les noms des clients et les détails des voitures.

SELECT v.ID_Vente, c.Nom_Client, c.Adresse_Client, vo.Marque, vo.Modèle, vo.Année, vo.Couleur, vo.Prix, v.Date_Vente
FROM Ventes v
JOIN Clients c ON v.ID_Client = c.ID_Client
JOIN Voitures vo ON v.ID_Voiture = vo.ID_Voiture;


--CChangez l'adresse de "Bob" en "456 Rue B2".

UPDATE Clients
SET Adresse_Client = '456 Rue B2'
WHERE ID_Client = 2;


--Changez le prix de la "Toyota Corolla" à 20500.
UPDATE Voitures
SET Prix = 20500
WHERE ID_Voiture = 101;


--Supprimez la vente de "Charlie" pour la voiture "Ford Fiesta".
DELETE FROM Ventes
WHERE ID_Vente = 3;


--Supprimez le client "Alice" et toutes ses ventes.
DELETE FROM Ventes
WHERE ID_Client = 1;

DELETE FROM Clients
WHERE ID_Client = 1;


SELECT * FROM Ventes;
SELECT * FROM Voitures;
SELECT * FROM Clients;



