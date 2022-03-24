import React, { useEffect, useState } from 'react'
import axios from 'axios';
import {useNavigate, useParams} from "react-router-dom";

const Update = (props) => {

    const { id } = useParams();
    const { productList, setProductList } = props;
    const [title, setTitle] = useState("");
    const [price, setPrice] = useState("");
    const [description, setDescription] = useState("");

    const navigate = useNavigate();

    useEffect(() => {
        axios.get(`http://localhost:8000/api/products/${id}`, )
            .then((res) => {
                console.log(res);
                console.log(res.data);
                setTitle(res.data.title);
                setPrice(res.data.price);
                setDescription(res.data.description);
            })
            .catch(err => console.log(err))
    }, [])

    const submitHandler = (e) => {

        e.preventDefault();
        
        axios.put(`http://localhost:8000/api/products/${id}`, {
                title,
                price,
                description
        })
            .then((res) => {
                console.log(res);
                console.log(res.data);
                // setProductList([...productList, res.data]);
                // setTitle("");
                // setPrice("");
                // setDescription("");
                navigate("/product");
            })
            .catch(err => console.log(err))
    }

    return (
        <div>
            <h1>Update a Product</h1>

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
                
                <input type='submit' value="Update" className="submit-input" />
            </form>
        </div>
    )
}
export default Update;