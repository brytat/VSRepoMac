import { Link } from "react-router-dom";
import axios from 'axios';
import React, { useState, useEffect } from 'react'

const DisplayAll = (props) => {

    const [petList, setPetList] = useState([]);

    useEffect(()=>{
        axios.get("http://localhost:8000/api/pet")
        .then((res)=>{
            console.log(res.data);
            setPetList(res.data);
        })
        .catch((err)=>{
        console.log(err);
        })
    }, [])

    return (
        <div className="container">
            <Link to={"/pets/new"}>add a pet to the shelter</Link>
            <h3>These pets need a good home</h3>
            <div className="center">
                <table>
                    <thead>
                        <tr>
                            <th>Name</th>
                            <th>Type</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                    {
                        petList.map((pet, idx) => {
                        return(
                            <tr key={idx}>
                                <td>{pet.name}</td>
                                <td>{pet.type}</td>
                                <td>
                                    <Link className="nav-btn" to={`/pets/${pet._id}`}>
                                        Details
                                    </Link>
                                    <Link className="nav-btn" to={`/pets/edit/${pet._id}`}>
                                        Edit
                                    </Link>
                                </td>
                            </tr>
                        )})
                    }
                    </tbody>
                </table>
            </div>
        </div>
    );
};

export default DisplayAll;