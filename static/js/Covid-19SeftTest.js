//Determined from Machine Learning
let testResult = false;

function displayResult(){

    let progressBar = document.getElementById("progBar");
            document.getElementById("pBar").style.display = "block";

            let i = 2
            function progress(){
                if(i <100){
                    i++;
                    progressBar.style.width = i + "%";
                }
                setTimeout("progress()", 100);
            }
            progress();

    if(testResult){
        document.getElementById("pResult").style.display = "block";
    }
    else{
        document.getElementById("nResult").style.display = "block";
    }
}

let el = document.getElementById("file");
el.addEventListener('input', displayResult);



