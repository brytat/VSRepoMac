import React, { useState } from 'react';

const ProductForm = (props) => {
    const { initialTitle, initialPrice, initialDescription, onSubmitProp } = props;
    const [title, setTitle] = useState(initialTitle);
    const [price, setPrice] = useState(initialPrice);
    const [description, setDescription] = useState(initialDescription);
    const submitHandler = (e) => {
        e.preventDefault();
        onSubmitProp({ title, price, description });
    }

    return (
        <div>
            <form onSubmit={submitHandler}>
            {authorNotFoundError ? (
                <h2>
                {authorNotFoundError} <Link to="/new">Click here to add author</Link>
                </h2>
            ) : null}
                <div className="form-fields">
                    <label>Title:</label>
                    <input
                        onChange={(e) => setTitle(e.target.value)}
                        value={title}
                        type="text"
                        name='title'
                    />
                </div>

                <br />

                <div className="form-fields">
                    <label>Price:</label>
                    <input
                        onChange={(e) => setPrice(e.target.value)}
                        value={price}
                        type="number"
                        name='price'
                    />
                </div>

                <br />

                <div className="form-fields">
                    <label>Description:</label>
                    <input
                        type="text"
                        name='description'
                        value={description}
                        onChange={(e) => setDescription(e.target.value)}
                    />
                </div>

                <br />
                
                <input type='submit' value="Submit" className="submit-input" />
            </form>
        </div>
    );
};

export default ProductForm;