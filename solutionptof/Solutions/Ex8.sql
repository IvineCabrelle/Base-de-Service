-- Table Clients
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY IDENTITY,
    Nom NVARCHAR(100) NOT NULL,
    Adresse NVARCHAR(255) NOT NULL
);

-- Table Produits
CREATE TABLE Produits (
    ProduitID INT PRIMARY KEY IDENTITY,
    Nom NVARCHAR(100) NOT NULL,
    PrixUnitaire DECIMAL(10, 2) NOT NULL
);

-- Table Commandes
CREATE TABLE Commandes (
    CommandeID INT PRIMARY KEY IDENTITY,
    ClientID INT NOT NULL,
    DateCommande DATE NOT NULL,
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID)
);

-- Table D�tailsCommandes
CREATE TABLE DetailsCommandes (
    CommandeID INT NOT NULL,
    ProduitID INT NOT NULL,
    Quantit� INT NOT NULL,
    PrixUnitaire DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (CommandeID, ProduitID),
    FOREIGN KEY (CommandeID) REFERENCES Commandes(CommandeID),
    FOREIGN KEY (ProduitID) REFERENCES Produits(ProduitID)
);

-- Insertion des donn�es dans la table Clients
INSERT INTO Clients (Nom, Adresse) VALUES
('John Doe', '123 Rue A'),
('Jane Smith', '456 Rue B');

-- Insertion des donn�es dans la table Produits
INSERT INTO Produits (Nom, PrixUnitaire) VALUES
('Produit 1', 10.00),
('Produit 2', 20.00),
('Produit 3', 30.00);

-- Insertion des donn�es dans la table Commandes
INSERT INTO Commandes (ClientID, DateCommande) VALUES
(1, '2023-06-01'),
(2, '2023-06-02');

-- Insertion des donn�es dans la table D�tailsCommandes
INSERT INTO DetailsCommandes (CommandeID, ProduitID, Quantit�, PrixUnitaire) VALUES
(1, 1, 2, 10.00),
(1, 2, 1, 20.00),
(2, 1, 1, 10.00),
(2, 3, 5, 30.00);

--Requ�te pour R�cup�rer Tous les D�tails des Commandes


SELECT 
    c.CommandeID,
    cl.Nom AS ClientNom,
    cl.Adresse AS ClientAdresse,
    p.Nom AS ProduitNom,
    dc.Quantit�,
    dc.PrixUnitaire
FROM 
    Commandes c
JOIN 
    Clients cl ON c.ClientID = cl.ClientID
JOIN 
    DetailsCommandes dc ON c.CommandeID = dc.CommandeID
JOIN 
    Produits p ON dc.ProduitID = p.ProduitID;



--Requ�te pour Calculer le Montant Total de Chaque Commande
SELECT 
    c.CommandeID,
    SUM(dc.Quantit� * dc.PrixUnitaire) AS MontantTotal
FROM 
    Commandes c
JOIN 
    DetailsCommandes dc ON c.CommandeID = dc.CommandeID
GROUP BY 
    c.CommandeID;
