//Determined from Machine Learning
let testResult = false;

function displayResult(){
    if(testResult)
        document.getElementById("pResult").style.display = "block";
    else
        document.getElementById("nResult").style.display = "block";
}

let el = document.getElementById("input-file-now");
el.addEventListener('input', displayResult);
