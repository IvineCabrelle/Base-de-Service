// Création de la base de données
use bibliotheque2

// Création de la collection livres
db.createCollection("livres")

// Création de la collection auteurs
db.createCollection("auteurs")


// Insertion de quelques documents dans la collection livres
db.livres.insertMany([
    { titre: "Le Petit Prince", auteur_id: "1", genre: "Conte", année: 1943 },
    { titre: "L'Étranger", auteur_id: "2", genre: "Roman", année: 1942 },
    { titre: "Les Misérables", auteur_id: "3", genre: "Roman", année: 1862 }
])

// Insertion de quelques documents dans la collection auteurs
db.auteurs.insertMany([
    { auteur_id: "1", nom: "Antoine de Saint-Exupéry", nationalité: "Français", date_naissance: "1900-06-29" },
    { auteur_id: "2", nom: "Albert Camus", nationalité: "Français", date_naissance: "1913-11-07" },
    { auteur_id: "3", nom: "Victor Hugo", nationalité: "Français", date_naissance: "1802-02-26" }
])


// Dénormalisation des données en utilisant l'opération d'agrégation $lookup
db.livres.aggregate([
    {
        $lookup: {                  // Elle permet de joindre les documents de la collection auteurs avec ceux de la collection livres
            from: "auteurs",        // La collection à joindre
            localField: "auteur_id", // Le champ dans la collection livres à utiliser pour la jointure
            foreignField: "auteur_id", // Le champ dans la collection externe auteurs pour la jointure
            as: "auteur"             // Le nom du nouveau champ qui contiendra les résultats de la jointure
        }
    },
    {
        $unwind: "$auteur"   // Décompose le tableau résultant de la jointure pour obtenir un document par élément du tableau
    },
    {
        $project: {
            _id: 0,                    // Exclut le champ _id de la sortie finale
            titre: 1,                  // Inclut le champ titre
            genre: 1,                  // Inclut le champ genre
            année: 1,                  // Inclut le champ année
            "auteur.nom": 1,           // Inclut le champ nom de l'auteur (précisé avec la syntaxe "auteur.nom")
            "auteur.nationalité": 1,   // Inclut le champ nationalité de l'auteur (précisé avec la syntaxe "auteur.nationalité")
            "auteur.date_naissance": 1 // Inclut le champ date de naissance de l'auteur (précisé avec la syntaxe "auteur.date_naissance")
        }
    },
    {
        $out: "livres_denormalises" // Écrit les résultats dans la collection livres_denormalises
    }
])


// Affichage des documents de la collection livres_denormalises
db.livres_denormalises.find().pretty()
