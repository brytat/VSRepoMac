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
            </div>
            <div className="border">
                <div className="inline">
                    <h5>Faction: </h5>
                    <p>{displayOneArmy.faction}</p>
                </div>
                {/* This is a work in progress, needs to implement league functionality */}
                <div className="inline">
                    <h5>League Level: </h5><p>Coming Soon{displayOneArmy.league_level}</p>
                </div>
                <div className="inline">
                    <h5>Created: </h5>
                    <div>
                        <p>{displayOneArmy.created_at} </p>
                    </div>

                </div>
            </div>

        </div>
    );
};

export default DisplayOneArmy;