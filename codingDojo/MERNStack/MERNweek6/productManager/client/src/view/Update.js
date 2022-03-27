import React, { useEffect, useState } from 'react'
import axios from 'axios';
import {useNavigate, useParams} from "react-router-dom";
import ProductForm from "../components/ProductForm";
import DeleteButton from '../components/DeleteButton';

const Update = (props) => {
    const navigate = useNavigate();
    const { id } = useParams();
    const [ product, setProduct ] = useState({});
    const [loaded, setLoaded] = useState(false);

    useEffect(() => {
        axios.get(`http://localhost:8000/api/products/${id}`)
        .then((res) => {
            console.log(res.data);
            setProduct(res.data);
            setLoaded(true)
        })
    }, [])

    const updateProduct = productParam => {
        axios.put(`http://localhost:8000/api/products/${id}`, productParam)
        .then((res) => {
            console.log(res);
            console.log(res.data);
            navigate("/product");
        })
        .catch(err => console.log(err))
    }

    return (
        <div>
            <h1>Update a Product</h1>
            {loaded && ( 
            <>
                <ProductForm
                    onSubmitProp={updateProduct}
                    initialTitle= {product.title}
                    initialPrice={product.price}
                    initialDescription={product.description}
                />
                <DeleteButton productId={product._id} successCallback={() => navigate("/product")} />
            </>
            )}
        </div>
    )
}
export default Update;