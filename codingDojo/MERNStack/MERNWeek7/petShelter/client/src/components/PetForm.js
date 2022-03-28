import React, { useState } from 'react';
import { Link } from "react-router-dom";

const PetForm = (props) => {
    const { pageTitle, initialName, initialType, initialDescription, initialSkill_1, initialSkill_2, initialSkill_3, onSubmitProp, submitButton, errors } = props;
    const [ name, setName ] = useState(initialName);
    const [ type, setType ] = useState(initialType);
    const [ description, setDescription ] = useState(initialDescription);
    const [ formButton, setFormButton ] = useState(submitButton)
    const [ skill_1, setSkill_1 ] = useState(initialSkill_1);
    const [ skill_2, setSkill_2 ] = useState(initialSkill_2);
    const [ skill_3, setSkill_3 ] = useState(initialSkill_3);
    const submitHandler = (e) => {
        e.preventDefault();
        onSubmitProp({ name, type, description, skill_1, skill_2, skill_3 });
    }

    return (
        <div className="container">
            <Link to={'/'}>back to home</Link>
            
            <br />

            <h3>{pageTitle}</h3>

            <br />

            <form onSubmit={submitHandler}>
                <div className='column'>
                    <div className="form-fields">
                        <label>Pet Name:</label>
                        <br/>
                        <input
                            onChange={(e) => setName(e.target.value)}
                            value={name}
                            type="text"
                            name='name'
                        />
                    {errors.name ? <p>{errors.name.message}</p> : null}
                    </div>

                    <br />

                    <div className="form-fields">
                        <label>Pet Type:</label>
                        <br/>
                        <input
                            onChange={(e) => setType(e.target.value)}
                            value={type}
                            type="text"
                            name='type'
                        />
                    {errors.type ? <p>{errors.type.message}</p> : null}
                    </div>

                    <br />

                    <div className="form-fields">
                        <label>Pet Description:</label>
                        <br/>
                        <input
                            onChange={(e) => setDescription(e.target.value)}
                            value={description}
                            type="text"
                            name='description'
                        />
                    {errors.description ? <p>{errors.description.message}</p> : null}
                    </div>
                    <div>
                        <input type='submit' value={submitButton} className="submit-input" />
                    </div>
                </div>
                <div className='column'>
                    <p>Skills (optional)</p>
                    <div className="form-fields">
                        <label>Skill 1:</label>
                        <br/>
                        <input
                            onChange={(e) => setSkill_1(e.target.value)}
                            value={skill_1}
                            type="text"
                            name='skill_1'
                        />
                    </div>

                    <br />

                    <div className="form-fields">
                        <label>Skill 2:</label>
                        <br/>
                        <input
                            onChange={(e) => setSkill_2(e.target.value)}
                            value={skill_2}
                            type="text"
                            name='skill_2'
                        />
                    </div>

                    <br />

                    <div className="form-fields">
                        <label>Skill 3:</label>
                        <br/>
                        <input
                            onChange={(e) => setSkill_3(e.target.value)}
                            value={skill_3}
                            type="text"
                            name='skill_3'
                        />
                    </div>
                </div>


            </form>
        </div>
    );
};

export default PetForm;