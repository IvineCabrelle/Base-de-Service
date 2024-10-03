--Normalisation de la Table Commandes
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY,
    Nom VARCHAR(100) NOT NULL,
    Adresse VARCHAR(255) NOT NULL
);

CREATE TABLE Produits (
    ProduitID INT PRIMARY KEY,
    Nom VARCHAR(100) NOT NULL,
    PrixUnitaire DECIMAL(10, 2) NOT NULL
);

CREATE TABLE Commandes (
    CommandeID INT PRIMARY KEY,
    ClientID INT NOT NULL,
    DateCommande DATE NOT NULL,
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID)
);

CREATE TABLE DetailsCommandes (
    DetailCommandeID INT PRIMARY KEY,
    CommandeID INT NOT NULL,
    ProduitID INT NOT NULL,
    Quantite INT NOT NULL,
    PrixUnitaire DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (CommandeID) REFERENCES Commandes(CommandeID),
    FOREIGN KEY (ProduitID) REFERENCES Produits(ProduitID)
);

--Insertion de Données

INSERT INTO Clients (ClientID, Nom, Adresse) VALUES
(1, 'John Doe', '123 Main St'),
(2, 'Jane Smith', '456 Maple Ave');

INSERT INTO Produits (ProduitID, Nom, PrixUnitaire) VALUES
(1, 'Produit A', 10.00),
(2, 'Produit B', 15.50);


INSERT INTO Commandes (CommandeID, ClientID, DateCommande) VALUES
(1, 1, '2024-06-01'),
(2, 2, '2024-06-02');

INSERT INTO DetailsCommandes (DetailCommandeID, CommandeID, ProduitID, Quantite, PrixUnitaire) VALUES
(1, 1, 1, 2, 10.00),
(2, 1, 2, 1, 15.50),
(3, 2, 1, 1, 10.00);

--Requête pour Récupérer tous les Détails des Commandes
SELECT 
    Commandes.CommandeID,
    Clients.Nom AS NomClient,
    Clients.Adresse AS AdresseClient,
    Produits.Nom AS NomProduit,
    DetailsCommandes.Quantite,
    DetailsCommandes.PrixUnitaire
FROM 
    Commandes
JOIN 
    Clients ON Commandes.ClientID = Clients.ClientID
JOIN 
    DetailsCommandes ON Commandes.CommandeID = DetailsCommandes.CommandeID
JOIN 
    Produits ON DetailsCommandes.ProduitID = Produits.ProduitID;

--Requête pour Calculer le Montant Total de Chaque Commande

	SELECT 
    Commandes.CommandeID,
    SUM(DetailsCommandes.Quantite * DetailsCommandes.PrixUnitaire) AS MontantTotal
FROM 
    Commandes
JOIN 
    DetailsCommandes ON Commandes.CommandeID = DetailsCommandes.CommandeID
GROUP BY 
    Commandes.CommandeID;
