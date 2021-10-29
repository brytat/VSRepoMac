function displayIfChildIsAbleToRideTheRollerCoaster(childHeight) {
    if (childHeight > 52) {
    //unit is in inches
        console.log("Get on that ride, kiddo!");
    } else {
        console.log("Sorry kiddo. Maybe next year");
    }
}
displayIfChildIsAbleToRideTheRollerCoaster(40);