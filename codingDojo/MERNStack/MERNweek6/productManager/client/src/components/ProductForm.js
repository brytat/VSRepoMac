import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ProductForm = (props) => {

    const { productList, setProductList } = props;

    const [title, setTitle] = useState("");
    const [price, setPrice] = useState("");
    const [description, setDescription] = useState("");

    const submitHandler = (e) => {
        e.preventDefault();

        axios
            .post("http://localhost:8000/api/products", {
                title,
                price,
                description,
            })
            .then((res) => {
                console.log(res);
                console.log(res.data);
                setProductList([...productList, res.data]);
                setTitle("");
                setPrice("");
                setDescription("");
            })
            .catch((err) => {
                console.log(err);
            });
    };

    return (
        <div>
            <h1>Product Manager </h1>

            <form onSubmit={submitHandler}>
                <div className="form-fields">
                    <label>Title:</label>
                    <input
                        onChange={(e) => setTitle(e.target.value)}
                        value={title}
                        type="text"
                        name='title'
                    />
                </div>

                <br />

                <div className="form-fields">
                    <label>Price:</label>
                    <input
                        onChange={(e) => setPrice(e.target.value)}
                        value={price}
                        type="number"
                        name='price'
                    />
                </div>

                <br />

                <div className="form-fields">
                    <label>Description:</label>
                    <input
                        onChange={(e) => setDescription(e.target.value)}
                        value={description}
                        type="text"
                        name='description'
                    />
                </div>

                <br />
                
                <input type='submit' value="Create" className="submit-input" />
            </form>
        </div>
    );
};

export default ProductForm;