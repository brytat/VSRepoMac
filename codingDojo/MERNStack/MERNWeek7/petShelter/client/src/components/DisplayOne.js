import React, { useState, useEffect } from "react";
import { useParams, Link, useNavigate } from "react-router-dom";
import axios from "axios";

const DisplayOne = (props) => {
    const navigate = useNavigate();
    const { id } = useParams();
    const [displayOne, setDisplayOne] = useState({});
    const [petList, setPetList] = useState([]);

    useEffect(() => {
        axios
        .get(`http://localhost:8000/api/pet/${id}`)
        .then((res) => {
            console.log(res.data);
            setDisplayOne(res.data);
        })
        .catch((err) => {
            console.log(err.response);
        });
    }, [id]);

    const removeFromDom = (id) => {
        axios.delete(`http://localhost:8000/api/pet/${id}`)
        .then((res) => {
            console.log(res);
            console.log(res.data);
            setPetList(petList.filter(pet => pet._id !== id));
            navigate("/");
        })
        .catch(err => console.log(err))
    }

    return (
        <div className="container">
            <Link to={'/'}>back to home</Link>
            <div className="inline column">
                <h3>Details about: {displayOne.name}</h3>
                <button className="adopt-btn" onClick={(e)=>{removeFromDom(displayOne._id)}}>
                    Adopt {displayOne.name}
                </button>
            </div>
            <div className="border">
                <div className="inline">
                    <h5>Pet type: </h5>
                    <p>{displayOne.type}</p>
                </div>
                <div className="inline">
                    <h5>Description: </h5><p>{displayOne.description}</p>
                </div>
                <div className="inline">
                    <h5>Skills: </h5>
                    <div>
                        <p>{displayOne.skill_1} </p>
                        <p>{displayOne.skill_2} </p>
                        <p>{displayOne.skill_3}</p>
                    </div>

                </div>
            </div>

        </div>
    );
};

export default DisplayOne;