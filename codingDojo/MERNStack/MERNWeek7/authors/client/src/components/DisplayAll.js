
import { Link } from "react-router-dom";
import axios from 'axios';
import React, { useState, useEffect } from 'react'

const DisplayAll = (props) => {

    const [authorList, setAuthorList] = useState([]);

    useEffect(()=>{
        axios.get("http://localhost:8000/api/author")
        .then((res)=>{
            console.log(res.data);
            setAuthorList(res.data);
        })
        .catch((err)=>{
        console.log(err);
        })
    }, [])

    const removeFromDom = (id) => {
        axios.delete(`http://localhost:8000/api/author/${id}`)
        .then((res) => {
            console.log(res);
            console.log(res.data);
            setAuthorList(authorList.filter(author => author._id !== id));
        })
        .catch(err => console.log(err))
    }

    return (
        <div>
            <Link to={"/new"}>New Author</Link>
            <header><h1>All Authors:</h1></header>
            <table>
                <thead>
                    <tr>
                        <th>Author</th>
                        <th>Actions available</th>
                    </tr>
                </thead>
                <tbody>
                {
                    authorList.map((author, idx) => {
                    return(
                        <tr key={idx}>
                            <td>{author.name}</td>
                            <td>
                                <Link to={`/edit/${author._id}`}>
                                    Edit
                                </Link>
                                <button onClick={(e)=>{removeFromDom(author._id)}}>
                                    Delete
                                </button>
                            </td>
                        </tr>
                    )})
                }
                </tbody>
            </table>
        </div>
    );
};

export default DisplayAll;