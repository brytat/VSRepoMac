import React, { useEffect, useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import PetForm from "../components/PetForm";

const Create = (props) => {
    const navigate = useNavigate();
    const [ errors, setErrors ] = useState({});
    const [petList, setPetList] = useState([]);
    
    useEffect(()=>{
        axios.get("http://localhost:8000/api/pet")
        .then((res)=>{
            console.log(res.data);
            setPetList(res.data);
        })
        .catch((err) => {
            console.log(err.response);
        })
    }, [])

    const createPet = petParam => {
        axios.post("http://localhost:8000/api/pet", petParam)
            .then(res => {
                console.log(res);
                console.log(res.data);
                setPetList([...petList, res.data]);
                navigate("/");
            })
            .catch((err) => {
                console.log(err.response.data.err.errors);
                setErrors(err.response.data.err.errors);
            })
    }

    return (
        <div>
            <PetForm
                pageTitle="Know a pet needing a home?"
                onSubmitProp={createPet}
                initialName=""
                initialType=""
                initialDescription=""
                initialSkill_1=""
                initialSkill_2=""
                initialSkill_3=""
                submitButton="Add Pet"
                errors={errors}
            />
        </div>
    )
}

export default Create;