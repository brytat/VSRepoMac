const Product = require("../models/product.model");

module.exports = {
    getAllProducts: (req, res) => {
        Product.find({})
            .then((allProducts) => {
                console.log(allProducts);
                res.json(allProducts);
            })
            .catch((err) => console.log(err));
    },

    createProduct: (req, res) => {
        Product.create(req.body)
            .then((newProduct) => {
                console.log(newProduct);
                res.json(newProduct);
            })
            .catch(err => res.json(err));
    },

    getOneProduct: (req, res) => {
        Product.findOne({ _id: req.params.id })
            .then((oneProduct) => {
                console.log(oneProduct);
                res.json(oneProduct);
            })
            .catch((err) => console.log(err));
    },

    updateProduct: (req, res) => {
        Product.findOneAndUpdate({ _id: req.params.id }, req.body, {new:true})
            .then((updatedPerson) => {
                console.log(updatedPerson);
                res.json(updatedPerson);
            })
            .catch(err => res.json(err))
    },

    deleteProduct: (req, res) => {
        Product.deleteOne({ _id: req.params.id })
            .then((deleteConfirmation) => {
                console.log(deleteConfirmation);
                res.json(deleteConfirmation);
            })
            .catch(err => res.json(err))
    }
};