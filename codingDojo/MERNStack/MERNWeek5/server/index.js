const faker = require("faker");

const express = require("express");

const app = express();
const port = 8000;

// User Object
//     _id
//     firstName
//     lastName
//     phoneNumber
//     email
//     password

const fakerUserObj = () => ({
    _id: faker.datatype.uuid(),
    firstName: faker.name.firstName(),
    lastName: faker.name.lastName(),
    phoneNumber: faker.phone.phoneNumber(),
    email: faker.internet.email(),
    passsword: faker.internet.password(),
});

// Company Object
//     _id
//     name
//     address
//         street
//         city
//         state
//         zipCode
//         country
const fakerCompanyObj = () => ({
    _id: faker.datatype.uuid(),
    name: faker.company.companyName(),
    address: {
        street: faker.address.streetAddress(),
        city: faker.address.cityName(),
        state: faker.address.state(),
        zipcode: faker.address.zipCode(),
        country: faker.address.country(),
    },
});

app.get("/api/users/new", (req, res) => {
    const newUser = fakerUserObj();
    res.json(newUser);
});

app.get("/api/companies/new", (req, res) => {
    const newCompany = fakerCompanyObj();
    res.json(newCompany);
});

app.get("/api/user/company", (req, res) => {
    const newUser = fakerUserObj();
    const newCompany = fakerCompanyObj();
    const responseObject = {
        user: newUser,
        company: newCompany,
    };
    res.json(responseObject);
});

app.listen(port, () => console.log(`express server running on port ${port}`));