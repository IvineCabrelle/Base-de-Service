// Creation de database
use gestion_voyage
// Cr�ation de la collection "destinations" et insertion de donn�es
db.destinations.insertMany([
    {
        "nom": "Paris",
        "description": "Ville de l'amour",
        "prix_moyen_par_jour": 100,
        "attractions_principales": ["Tour Eiffel", "Mus�e du Louvre", "Cath�drale Notre-Dame"]
    },
    {
        "nom": "New York",
        "description": "La ville qui ne dort jamais",
        "prix_moyen_par_jour": 150,
        "attractions_principales": ["Statue de la Libert�", "Times Square", "Central Park"]
    },
    {
        "nom": "Tokyo",
        "description": "Capitale du Japon",
        "prix_moyen_par_jour": 120,
        "attractions_principales": ["Tour de Tokyo", "Temple Senso-ji", "Quartier de Shibuya"]
    }
])

//Cr�ation de la collection "voyages" et insertion de donn�es :

db.voyages.insertMany([
    {
        "destination": ObjectId("6664cb573e5ce2aba641fc43"),
        "dates_depart": ISODate("2024-07-01"),
        "dates_retour": ISODate("2024-07-10"),
        "participants": [
            { "nom": "Alice", "email": "alice@example.com", "num�ro_telephone": "1234567890" },
            // Autres participants...
        ],
        "prix_total": 1500
    },
    {
        "destination": ObjectId("6664cb573e5ce2aba641fc44"),
        "dates_depart": ISODate("2024-08-15"),
        "dates_retour": ISODate("2024-08-25"),
        "participants": [
            { "nom": "Bob", "email": "bob@example.com", "num�ro_telephone": "9876543210" },
            // Autres participants...
        ],
        "prix_total": 2000
    },
    {
        "destination": ObjectId("6664cb573e5ce2aba641fc45"),
        "dates_depart": ISODate("2024-09-20"),
        "dates_retour": ISODate("2024-09-30"),
        "participants": [
            { "nom": "Charlie", "email": "charlie@example.com", "num�ro_telephone": "5551234567" },
            // Autres participants...
        ],
        "prix_total": 1800
    }
])
//Cr�ation de la collection "clients" et insertion de donn�es :
db.clients.insertMany([
    { "nom": "Alice", "email": "alice@example.com", "num�ro_telephone": "1234567890" },
    { "nom": "Bob", "email": "bob@example.com", "num�ro_telephone": "9876543210" },
    { "nom": "Charlie", "email": "charlie@example.com", "num�ro_telephone": "5551234567" }
])

//Cr�ation de la collection "factures" et insertion de donn�es :

db.factures.insertMany([
    {
        "numero_facture": "INV001",
        "id_voyage": ObjectId("6664cba93e5ce2aba641fc46"),
        "montant_total": 1500,
        "date_facturation": ISODate("2024-07-12")
    },
    {
        "numero_facture": "INV002",
        "id_voyage": ObjectId("6664cbc93e5ce2aba641fc4a"),
        "montant_total": 2000,
        "date_facturation": ISODate("2024-08-30")
    },
    {
        "numero_facture": "INV003",
        "id_voyage": ObjectId("6664cbc93e5ce2aba641fc4b"),
        "montant_total": 1800,
        "date_facturation": ISODate("2024-10-05")
    }
])
//Afficher la liste de toutes les destinations avec leurs d�tails :
db.destinations.find({})
//Afficher les d�tails d'un voyage avec la liste des participants :
db.voyages.aggregate([
    { $match: { "_id": ObjectId("6664cba93e5ce2aba641fc46") } },
    { $lookup: { from: "clients", localField: "participants.nom", foreignField: "nom", as: "participants" } }
])
//Calculer le montant total des factures �mises pour une p�riode donn�e :
db.factures.aggregate([
    { $match: { "date_facturation": { $gte: ISODate("2024-08-01"), $lte: ISODate("2024-09-01") } } },
    { $group: { _id: null, montant_total: { $sum: "$montant_total" } } }
])

//Mettre � jour la date de retour d'un voyage :

db.voyages.updateOne(
    { "_id": ObjectId("ID_DU_VOYAGE") },
    { $set: { "dates_retour": ISODate("NOUVELLE_DATE_RET0UR") } }
)

//Supprimer un client et toutes ses factures associ�es:

db.clients.deleteOne({ "_id": ObjectId("ID_DU_CLIENT") })
db.factures.deleteMany({ "id_client": ObjectId("ID_DU_CLIENT") })
