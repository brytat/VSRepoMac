import React, { useState, useEffect } from "react";
import { useParams, Link } from "react-router-dom";
import axios from "axios";

const DisplayOneArmy = (props) => {
    const { id } = useParams();
    const [displayOneArmy, setDisplayOneArmy] = useState({});

    useEffect(() => {
        axios
        .get(`http://localhost:8000/api/army/${id}`)
        .then((res) => {
            console.log(res.data);
            setDisplayOneArmy(res.data);
        })
        .catch((err) => {
            console.log(err.response);
        });
    }, [id]);

    return (
        <div className="container">
            <Link to={'/'}>back to home</Link>
            <div className="inline column">
                <h3>Details about: {displayOneArmy.name}</h3>
                <button className="adopt-btn" onClick={(e)=>{removeFromDom(displayOneArmy._id)}}>
                    Apdopt {displayOneArmy.name}
                </button>
            </div>
            <div className="border">
                <div className="inline">
                    <h5>Pet type: </h5>
                    <p>{displayOneArmy.type}</p>
                </div>
                <div className="inline">
                    <h5>Description: </h5><p>{displayOneArmy.description}</p>
                </div>
                <div className="inline">
                    <h5>Skills: </h5>
                    <div>
                        <p>{displayOneArmy.skill_1} </p>
                        <p>{displayOneArmy.skill_2} </p>
                        <p>{displayOneArmy.skill_3}</p>
                    </div>

                </div>
            </div>

        </div>
    );
};

export default DisplayOneArmy;