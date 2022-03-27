import React, { useEffect, useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import AuthorForm from "../components/AuthorForm";

const Create = (props) => {
    const navigate = useNavigate();
    const [ errors, setErrors ] = useState({});
    const [authorList, setAuthorList] = useState([]);
    
    useEffect(()=>{
        axios.get("http://localhost:8000/api/author")
        .then((res)=>{
            console.log(res.data);
            setAuthorList(res.data);
        })
        .catch((err) => {
            console.log(err.response);
        })
    }, [])

    const createAuthor = authorParam => {
        axios.post("http://localhost:8000/api/author", authorParam)
            .then(res => {
                console.log(res);
                console.log(res.data);
                setAuthorList([...authorList, res.data]);
                navigate("/");
            })
            .catch((err) => {
                console.log(err.response.data.err.errors);
                setErrors(err.response.data.err.errors);
            })
    }

    return (
        <div>
            <h1>We have quotes by:</h1>
            <AuthorForm
                onSubmitProp={createAuthor}
                initialName=""
                errors={errors}
            />
        </div>
    )
}

export default Create;