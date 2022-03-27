const Author = require("../models/author.model");

module.exports = {

    createAuthor: (req, res) => {
        const {name} = req.body;
        Author.create({
            name: name
        })
            .then((author) => {
                console.log(author);
                res.json(author)
            })
            .catch((err) => {
                console.log(err);
                res.status(400).json({err});
            });
    },

    getOneAuthor: (req, res) => {
        Author.findOne({ _id: req.params.id })
            .then((oneAuthor) => {
                console.log(oneAuthor);
                res.json(oneAuthor);
            })
            .catch((err) => {
                console.log(err);
                res.status(400).json({err});
            });
    },

    getAllAuthors: (req, res) => {
        Author.find({})
            .then((allAuthors) => {
                console.log(allAuthors);
                res.json(allAuthors);
            })
            .catch((err) => {
                console.log(err);
                res.status(400).json({err});
            });
    },

    updateAuthor: (req, res) => {
        Author.findOneAndUpdate({ _id: req.params.id },
            req.body, {
                new:true,
                runValidators: true,
            })
            .then((updatedAuthor) => {
                console.log(updatedAuthor);
                res.json({updatedAuthor});
            })
            .catch((err) => {
                console.log(err);
                res.status(400).json({err});
            })
    },

    deleteAuthor: (req, res) => {
        Author.deleteOne({ _id: req.params.id })
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
