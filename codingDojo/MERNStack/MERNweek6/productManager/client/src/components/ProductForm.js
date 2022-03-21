import React, { useState } from 'react'
import axios from 'axios';

const ProductForm= () => {

    const [title, setTitle] = useState("");
    const [price, setPrice] = useState("");
    const [description, setDescription] = useState("");

    const submitHandler = (e) => {
        e.preventDefault();

        axios.post("http://localhost:8000/api/products",{
            title,
            price,
            description
        })
        .then((res)=>{
            console.log(res);
            console.log(res.data);
            setTitle("");
            setPrice("");
            setDescription("");
        })
        .catch((err)=>{
            console.log(err);
        })
    }

    return (
        <div class="col">
            <h1>
                Product Manager
            </h1>
            <form onSubmit={submitHandler}>
                <div class="row">
                    <label class='col' for='title'>Title:</label>
                    <input
                        onChange={(e) => setTitle(e.Target.value)}
                        class='col'
                        type="text"
                        id="title"
                        name='title'/>
                </div>

                <br />

                <div class="row">
                    <label class='col' for='price'>Price:</label>
                    <input
                        onChange={(e) => setPrice(e.Target.value)}
                        class='col'
                        type="text"
                        id="price"
                        name='price' />
                </div>

                <br />

                <div class="row">
                    <label class='col' for='description'>Description:</label>
                    <input
                        onChange={(e) => setDescription(e.Target.value)}
                        class='col'
                        type="text"
                        id="description"
                        name='description' />
                </div>

                <br />

                <input type='submit' value="Create" class="btn btn-warning" />
            </form>
        </div>
    )
}
export default ProductForm;