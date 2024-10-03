// Creation des collections
db.createCollection("plats")

db.createCollection("commandes")

db.createCollection("clients")

db.createCollection("factures")

//Créer un plat :

db.plats.insertOne({
    "nom": "Plat A",
    "description": "Description du plat A",
    "prix": 15.99,
    "categorie": "entrée"
})

//Créer une commande :

db.commandes.insertOne({
    "numero_commande": "CMD001",
    "plats": [
        {
            "nom": "Plat A",
            "quantite": 2
        },
        {
            "nom": "Plat B",
            "quantite": 1
        }
    ],
    "statut": "en attente"
})

//Créer un client :
db.clients.insertOne({
    "nom": "John Doe",
    "email": "john.doe@example.com",
    "numero_telephone": "1234567890"
})

//Créer une facture :

db.factures.insertOne({
    "numero_facture": "INV001",
    "numero_commande": "CMD001",
    "montant_total": 47.97,
    "date_facturation": ISODate("2024-06-08")
})

//Afficher la liste des plats de la catégorie "entrée" :

db.plats.find({ "categorie": "entrée" })

//Afficher les détails de la commande "CMD001" avec les plats commandés :

db.commandes.aggregate([
    { $match: { "numero_commande": "CMD001" } },
    { $unwind: "$plats" },
    { $lookup: { from: "plats", localField: "plats.nom", foreignField: "nom", as: "details_plats" } }
])

//Calculer le montant total des factures émises pour juin 2024 :
db.factures.aggregate([
    { $match: { "date_facturation": { $gte: ISODate("2024-06-01"), $lte: ISODate("2024-06-30") } } },
    { $group: { _id: null, montant_total: { $sum: "$montant_total" } } }
])

//Mettre à jour le statut de la commande "CMD001" à "préparée" :

db.commandes.updateOne(
    { "numero_commande": "CMD001" },
    { $set: { "statut": "préparée" } }
)


//Supprimer un client et toutes ses commandes associées :

db.clients.deleteOne({ "_id": ObjectId("...") })
db.commandes.deleteMany({ "client_id": ObjectId("...") })
