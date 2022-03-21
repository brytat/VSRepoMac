const PersonController = require("../controllers/person.controller");

module.exports = (app) => {
    app.get('/api', PersonController.index);

    // app.get("/api/welcome", (request, response)=>{
    //     console.log("This is the welcome API route");
    //     response.json({message: "Welcome to our API... This is the response"})
    // })
    
    // app.post("/api/welcome", (request, response)=>{
    //     console.log("This is our post request");
    //     response.json({
    //         message: [
    //             "this is the json object response",
    //             "this is a second response message"
    //         ],
    //         ourRequestBody: request.body
    //     })
    //     console.log(request);
    // })
}