//Determined from Machine Learning
let testResult = false;

function displayResult(){
    if(testResult)
        document.getElementById("pResult").style.display = "block";
    else
        document.getElementById("nResult").style.display = "block";
}

let el = document.getElementById("file");
el.addEventListener('input', displayResult);




