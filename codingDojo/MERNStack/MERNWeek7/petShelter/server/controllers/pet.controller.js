const Pet = require("../models/pet.model");

module.exports = {

    createPet: (req, res) => {
        Pet.create(req.body)
            .then((newPet) => {
                console.log(newPet);
                res.json(newPet);
            })
            .catch((err) => {
                console.log(err);
                res.status(400).json({err});
            })
    },

    getOnePet: (req, res) => {
        Pet.findOne({ _id: req.params.id })
            .then((onePet) => {
                console.log(onePet);
                res.json(onePet);
            })
            .catch((err) => {
                console.log(err);
                res.status(400).json({err});
            })
    },

    getAllPets: (req, res) => {
        Pet.find({})
            .then((allPets) => {
                console.log(allPets);
                res.json(allPets);
            })
            .catch((err) => {
                console.log(err);
                res.status(400).json({err});
            });
    },

    updatePet: (req, res) => {
        Pet.findOneAndUpdate({ _id: req.params.id },
            req.body, {
                new:true,
                runValidators: true,
            })
            .then((updatedPet) => {
                console.log(updatedPet);
                res.json(updatedPet);
            })
            .catch((err) => {
                console.log(err);
                res.status(400).json({err});
            })
    },

    deletePet: (req, res) => {
        Pet.deleteOne({ _id: req.params.id })
            .then((deleteConfirmation) => {
                console.log(deleteConfirmation);
                res.json(deleteConfirmation);
            })
            .catch((err) => {
                console.log(err);
                res.status(400).json({err});
            })
    }
};
