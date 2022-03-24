import React, { useState } from "react";
import ProductForm from "../components/ProductForm";
import DisplayAll from "../components/DisplayAll";

const Main = (props) => {

    const [productList, setProductList] = useState([]);
    
    const removeFromDom = productId => {
        setProductList(productList.filter(product => product._id != productId));
    }
    
    return (
        <div>

            <ProductForm
                productList={productList}
                setProductList={setProductList}
            />
            <hr/>
            <DisplayAll
                productList={productList}
                setProductList={setProductList} removeFromDom={removeFromDom}
            />
        </div>
    )
}

export default Main;