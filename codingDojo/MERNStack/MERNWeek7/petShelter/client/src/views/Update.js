import React, { useEffect, useState } from "react";
import axios from "axios";
import { useNavigate, useParams, Link } from "react-router-dom";
import PetForm from "../components/PetForm";

const Update = (props) => {
    const navigate = useNavigate();
    const { id } = useParams();
    const [ pet, setPet ] = useState([]);
    const [ loaded, setLoaded ] = useState(false);
    const [ errors, setErrors ] = useState({});
    
    useEffect(()=>{
        axios.get(`http://localhost:8000/api/pet/${id}`)
        .then((res)=>{
            console.log(res.data);
            setPet(res.data);
            setLoaded(true)
        })
        .catch((err) => {
            console.log(err.response);
        })
    }, [])

    const updatePet = petParam => {
        axios.put(`http://localhost:8000/api/pet/${id}`, petParam)
            .then(res => {
                console.log(res);
                console.log(res.data);
                navigate("/");
            })
            .catch((err) => {
                console.log(err.response.data.err.errors);
                setErrors(err.response.data.err.errors);
            })
    }

    return (
        <div>
            <h3>Edit {pet.name}</h3>
            {loaded && ( 
            <>
                <PetForm
                    onSubmitProp={updatePet}
                    initialName= {pet.name}
                    initialType= {pet.type}
                    initialDescription= {pet.description}
                    initialSkill_1={pet.skill_1}
                    initialSkill_2={pet.skill_2}
                    initialSkill_3={pet.skill_3}
                    submitButton="Update"
                    errors={errors}
                />
            </>
            )}
        </div>
    )
}

export default Update;