const Product = require('../models/product.model.js');

module.exports = {
    createProduct : (req, res) => {
        Product.create(req.body)
            .then(product => response.json(product))
            .catch(err => response.json(err));
    }
};