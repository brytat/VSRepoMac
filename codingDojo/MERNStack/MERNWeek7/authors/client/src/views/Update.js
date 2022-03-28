import React, { useEffect, useState } from 'react'
import axios from 'axios';
import { useNavigate, useParams } from "react-router-dom";
import AuthorForm from '../components/AuthorForm';

const Update = (props) => {
    const navigate = useNavigate();
    const { id } = useParams();
    const [ author, setAuthor ] = useState({});
    const [ loaded, setLoaded ] = useState(false);
    const [ errors, setErrors ] = useState({});
    const [authorNotFoundError, setAuthorNotFoundError] = useState("");

    useEffect(() => {
        axios.get(`http://localhost:8000/api/author/${id}`)
        .then((res) => {
            console.log(res.data);
            setAuthor(res.data);
            setLoaded(true)
        })
        .catch((err) => {
            console.log(err.response);
            setAuthorNotFoundError(`Author not found using that ID`);
        });
    }, [])

    const updateAuthor = authorParam => {
        axios.put(`http://localhost:8000/api/author/${id}`, authorParam)
        .then((res) => {
            console.log(res);
            console.log(res.data);
            navigate("/");
        })
        .catch((err) => {
            console.log(err.response.data.err.errors);
            setErrors(err.response.data.err.errors);
        });
    }

    return (
        <div>
            <h1>Edit this Author</h1>
            {loaded && ( 
            <>
                <AuthorForm
                    onSubmitProp={updateAuthor}
                    initialName= {author.name}
                    errors={errors}
                />
            </>
            )}
        </div>
    )
}
export default Update;