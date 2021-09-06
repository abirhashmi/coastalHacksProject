window.onload = () => {
    let button = document.querySelector("#btn");
  
    // Function for calculating BMI
    button.addEventListener("click", calculateBMI);
};
  
function calculateBMI() {
  
    /* Getting input from user into height variable. */
    let height = parseInt(document
            .querySelector("#height").value);
  
    /* Getting input from user into weight variable.*/
    let weight = parseInt(document
            .querySelector("#weight").value);
  
    let result = document.querySelector("#result");
  
    // Checking the user providing an actual
    // runnable value
    if (height === "" || isNaN(height)) 
        result.innerHTML = "Not a valid height";
  
    else if (weight === "" || isNaN(weight)) 
        result.innerHTML = "Not a valid height";
  
    else {
  
        // Fixing upto 2 decimal places
        let bmi = (weight * 703)/(height*height);
  
        // Dividing as per the bmi conditions
        if (bmi >= 0) result.innerHTML =
            `Your BMI : <span>${bmi}</span>`;
  
       
    }
}