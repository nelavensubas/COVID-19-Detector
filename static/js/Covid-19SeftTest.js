//Determined from Machine Learning


function displayResult(){
    if(testResult == 1)
        document.getElementById("pResult").style.display = "block";
    else
        document.getElementById("nResult").style.display = "block";
}

let el = document.getElementById("file");
el.addEventListener('input', displayResult);




