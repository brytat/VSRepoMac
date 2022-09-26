async function getHeroNames() {
    // The await keyword lets js know that it needs to wait until it gets a response back to continue.
    var response = await fetch("https://api.fabdb.net/cards/?keywords=hero&keywords=young");
    // We then need to convert the data into JSON format.
    var heroNames = await response.json();
    return heroNames;
}
    
console.log(getHeroNames());