import React, { useEffect } from "react";
import { Link } from "react-router-dom";
import DeleteButton from "./DeleteButton";

const DisplayAll = (props) => {

    const { removeFromDom, productList } = props;

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
                        <DeleteButton productId={product._id} successCallback={()=>removeFromDom(product._id)}/>
                    </div>
                ))
            }
        </div>
    );
};

export default DisplayAll;