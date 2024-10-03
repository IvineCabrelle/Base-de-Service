// Cr�ation de la base de donn�es
use bibliotheque2

// Cr�ation de la collection livres
db.createCollection("livres")

// Cr�ation de la collection auteurs
db.createCollection("auteurs")


// Insertion de quelques documents dans la collection livres
db.livres.insertMany([
    { titre: "Le Petit Prince", auteur_id: "1", genre: "Conte", ann�e: 1943 },
    { titre: "L'�tranger", auteur_id: "2", genre: "Roman", ann�e: 1942 },
    { titre: "Les Mis�rables", auteur_id: "3", genre: "Roman", ann�e: 1862 }
])

// Insertion de quelques documents dans la collection auteurs
db.auteurs.insertMany([
    { auteur_id: "1", nom: "Antoine de Saint-Exup�ry", nationalit�: "Fran�ais", date_naissance: "1900-06-29" },
    { auteur_id: "2", nom: "Albert Camus", nationalit�: "Fran�ais", date_naissance: "1913-11-07" },
    { auteur_id: "3", nom: "Victor Hugo", nationalit�: "Fran�ais", date_naissance: "1802-02-26" }
])


// D�normalisation des donn�es en utilisant l'op�ration d'agr�gation $lookup
db.livres.aggregate([
    {
        $lookup: {                  // Elle permet de joindre les documents de la collection auteurs avec ceux de la collection livres
            from: "auteurs",        // La collection � joindre
            localField: "auteur_id", // Le champ dans la collection livres � utiliser pour la jointure
            foreignField: "auteur_id", // Le champ dans la collection externe auteurs pour la jointure
            as: "auteur"             // Le nom du nouveau champ qui contiendra les r�sultats de la jointure
        }
    },
    {
        $unwind: "$auteur"   // D�compose le tableau r�sultant de la jointure pour obtenir un document par �l�ment du tableau
    },
    {
        $project: {
            _id: 0,                    // Exclut le champ _id de la sortie finale
            titre: 1,                  // Inclut le champ titre
            genre: 1,                  // Inclut le champ genre
            ann�e: 1,                  // Inclut le champ ann�e
            "auteur.nom": 1,           // Inclut le champ nom de l'auteur (pr�cis� avec la syntaxe "auteur.nom")
            "auteur.nationalit�": 1,   // Inclut le champ nationalit� de l'auteur (pr�cis� avec la syntaxe "auteur.nationalit�")
            "auteur.date_naissance": 1 // Inclut le champ date de naissance de l'auteur (pr�cis� avec la syntaxe "auteur.date_naissance")
        }
    },
    {
        $out: "livres_denormalises" // �crit les r�sultats dans la collection livres_denormalises
    }
])


// Affichage des documents de la collection livres_denormalises
db.livres_denormalises.find().pretty()
