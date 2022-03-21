const Product = require('../models/product.model.js');

module.exports = {
    getAllProducts: (req, res) => {
        Product.find({})
            .then((allProducts) => res.json(allProducts))
            .catch((err) => console.log(err));
    },

    getOneProduct: (req, res) => {
        Product.findOne({ _id: req.params.id })
            .then((oneProduct) => res.json(oneProduct))
            .catch((err) => console.log(err));
    },

    createProduct: (req, res) => {
        Product.create(req.body)
            .then(newProduct => response.json(newProduct))
            .catch(err => response.json(err));
    },
};