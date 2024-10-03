// Création de la base de données
use telephones_db

// Création de la collection telephones
db.createCollection("telephones")

// Création de la collection marques
db.createCollection("marques")

// Insertion de quelques documents dans la collection telephones
db.telephones.insertMany([
    { modele: "iPhone 12", marque_id: "1", prix: 999, caracteristiques: "Écran Super Retina XDR, 5G, A14 Bionic" },
    { modele: "Galaxy S21", marque_id: "2", prix: 799, caracteristiques: "Écran Dynamic AMOLED, 5G, Exynos 2100" },
    { modele: "Pixel 5", marque_id: "3", prix: 699, caracteristiques: "Écran OLED, 5G, Snapdragon 765G" }
])

// Insertion de quelques documents dans la collection marques
db.marques.insertMany([
    { marque_id: "1", nom: "Apple", pays_origine: "États-Unis", annee_creation: 1976 },
    { marque_id: "2", nom: "Samsung", pays_origine: "Corée du Sud", annee_creation: 1938 },
    { marque_id: "3", nom: "Google", pays_origine: "États-Unis", annee_creation: 1998 }
])

// Dénormalisation des données en utilisant l'opération d'agrégation $lookup
db.telephones.aggregate([
    {
        $lookup: {
            from: "marques",          // La collection à joindre
            localField: "marque_id",  // Le champ local à utiliser pour la jointure
            foreignField: "marque_id",// Le champ de la collection externe pour la jointure
            as: "marque"              // Le nom du nouveau champ qui contiendra les résultats de la jointure
        }
    },
    {
        $unwind: "$marque"  // Décompose le tableau résultant de la jointure pour obtenir un document par élément du tableau
    },
    {
        $project: {
            _id: 0,                     // Exclut le champ _id de la sortie finale
            modele: 1,                  // Inclut le champ modele
            prix: 1,                    // Inclut le champ prix
            caracteristiques: 1,        // Inclut le champ caracteristiques
            "marque.nom": 1,           // Inclut le champ nom de la marque (précisé avec la syntaxe "marque.nom")
            "marque.pays_origine": 1,  // Inclut le champ pays_origine de la marque (précisé avec la syntaxe "marque.pays_origine")
            "marque.annee_creation": 1 // Inclut le champ annee_creation de la marque (précisé avec la syntaxe "marque.annee_creation")
        }
    },
    {
        $out: "telephones_denormalises" // Écrit les résultats dans la collection telephones_denormalises
    }
])

db.telephones_denormalises.find().pretty()
