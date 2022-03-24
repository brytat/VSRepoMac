import React, { useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";

const DisplayAll = (props) => {

    const { removeFromDom, productList, setProductList} = props;
    
    const deleteProduct = (productId) => {
        axios.delete('http://localhost:8000/api/products/' + productId)
            .then(res => {
                removeFromDom(productId)
            })
            .catch(err => console.log(err))
    }

    useEffect(() => {
        axios.get("http://localhost:8000/api/products")
            .then((res) => {
                console.log(res);
                console.log(res.data);
                setProductList(res.data);
                
            })
            .catch((err) => console.log(err));
    }, [])

    return (
        <div>
            <header>
                All Products:
            </header>
            {
                productList.map((product, index) => (
                    <div key={index}>
                        <Link to={`/product/${product._id}`}>
                            {product.title}
                        </Link>
                        <Link to={`/product/edit/${product._id}`}>
                            Edit
                        </Link>
                        <button onClick={(e)=>{deleteProduct(product._id)}}>
                            Delete
                        </button>
                    </div>
                ))
            }
        </div>
    );
};

export default DisplayAll;