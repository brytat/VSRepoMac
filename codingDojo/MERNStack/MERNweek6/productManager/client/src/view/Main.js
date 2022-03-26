import React, { useEffect, useState } from "react";
import axios from "axios";
import ProductForm from "../components/ProductForm";
import DisplayAll from "../components/DisplayAll";

const Main = () => {

    const [productList, setProductList] = useState([]);
    
    useEffect(() => {
        axios.get("http://localhost:8000/api/products")
        .then((res) => {
            console.log(res);
            console.log(res.data);
            setProductList(res.data);
        })
        .catch((err) => console.log(err));
    }, [])

    const removeFromDom = productId => {
        axios.delete('http://localhost:8000/api/products/' + productId)
        .then((res) => {
            console.log(res);
            console.log(res.data);
            setProductList(productList.filter(product => product._id !== productId));
        })
        .catch(err => console.log(err))
    }

    const createProduct = productParam => {
        axios.post("http://localhost:8000/api/products", productParam)
        .then(res => {
            console.log(res);
            console.log(res.data);
            setProductList([...productList, res.data]);
        })
        .catch((err) => console.log(err));
    };

    return (
        <div>
            <h1>Product Manager</h1>
            <ProductForm
                setProductList={setProductList}
                onSubmitProp={createProduct}
                initialTitle=""
                initialPrice=""
                initialDescription=""
            />
            <hr/>
            <DisplayAll
                productList={productList}
                setProductList={setProductList}
                removeFromDom={removeFromDom}
            />
        </div>
    )
}

export default Main;