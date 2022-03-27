import React, { useState } from 'react';
import { Link } from "react-router-dom";

const AuthorForm = (props) => {
    const { initialName, onSubmitProp, errors } = props;
    const [ name, setName ] = useState(initialName);
    const submitHandler = (e) => {
        e.preventDefault();
        onSubmitProp({ name });
    }

    return (
        <div>
            <Link to={'/'}>Home</Link>
            <form onSubmit={submitHandler}>

                <div className="form-fields">
                    <label>Name:</label>
                    <input
                        onChange={(e) => setName(e.target.value)}
                        value={name}
                        type="text"
                        name='name'
                    />
                {errors.name ? <p>{errors.name.message}</p> : null}
                </div>

                <br />

                <input type='submit' value="Submit" className="submit-input" />
            </form>
        </div>
    );
};

export default AuthorForm;