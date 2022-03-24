import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";

const DisplayOne = (props) => {

    const { id } = useParams();
    const [displayOne, setDisplayOne] = useState({});

    useEffect(() => {
        axios
        .get(`http://localhost:8000/api/products/${id}`)
        .then((res) => {
            console.log(res.data);
            setDisplayOne(res.data);
        })
        .catch((err) => {
            console.log(err);
        });
    }, [id]);

    return (
        <div className="displayOne-component">
            <h2>{displayOne.title}</h2>
            <p>Price: ${displayOne.price}</p>
            <p>Description: {displayOne.description}</p>
        </div>
    );
};

export default DisplayOne;