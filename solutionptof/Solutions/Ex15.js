// Creation des collections
db.createCollection("plats")

db.createCollection("commandes")

db.createCollection("clients")

db.createCollection("factures")

//Cr�er un plat :

db.plats.insertOne({
    "nom": "Plat A",
    "description": "Description du plat A",
    "prix": 15.99,
    "categorie": "entr�e"
})

//Cr�er une commande :

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

//Cr�er un client :
db.clients.insertOne({
    "nom": "John Doe",
    "email": "john.doe@example.com",
    "numero_telephone": "1234567890"
})

//Cr�er une facture :

db.factures.insertOne({
    "numero_facture": "INV001",
    "numero_commande": "CMD001",
    "montant_total": 47.97,
    "date_facturation": ISODate("2024-06-08")
})

//Afficher la liste des plats de la cat�gorie "entr�e" :

db.plats.find({ "categorie": "entr�e" })

//Afficher les d�tails de la commande "CMD001" avec les plats command�s :

db.commandes.aggregate([
    { $match: { "numero_commande": "CMD001" } },
    { $unwind: "$plats" },
    { $lookup: { from: "plats", localField: "plats.nom", foreignField: "nom", as: "details_plats" } }
])

//Calculer le montant total des factures �mises pour juin 2024 :
db.factures.aggregate([
    { $match: { "date_facturation": { $gte: ISODate("2024-06-01"), $lte: ISODate("2024-06-30") } } },
    { $group: { _id: null, montant_total: { $sum: "$montant_total" } } }
])

//Mettre � jour le statut de la commande "CMD001" � "pr�par�e" :

db.commandes.updateOne(
    { "numero_commande": "CMD001" },
    { $set: { "statut": "pr�par�e" } }
)


//Supprimer un client et toutes ses commandes associ�es :

db.clients.deleteOne({ "_id": ObjectId("...") })
db.commandes.deleteMany({ "client_id": ObjectId("...") })
