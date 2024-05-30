// File Information
// Version: 0.50.01 (Pre-Beta)
// Creator: Michael Yurachek
// Last updated: 05 / 30 / 2024

currentGraph = 1;
function nextGraph(direction) {
    if (direction == 1) {
        if (currentGraph == 1) {
            document.getElementById("highGraph").style.display = "none";
            document.getElementById("edcSurveyGraph").style.display = "block";
            currentGraph = 3;
            return currentGraph;
        } else if (currentGraph == 2) {
            document.getElementById("collegeGraph").style.display = "none";
            document.getElementById("highGraph").style.display = "block";
            currentGraph = 1;
            return currentGraph;
        } else if (currentGraph == 3) {
            document.getElementById("edcSurveyGraph").style.display = "none";
            document.getElementById("collegeGraph").style.display = "block";
            currentGraph = 2;
            return currentGraph;
        } else {
            console.log("Page error | Page failed to change graphs")
        }
    } else if (direction == 2) {
        if (currentGraph == 1) {
            document.getElementById("highGraph").style.display = "none";
            document.getElementById("collegeGraph").style.display = "block";
            currentGraph = 2;
            return currentGraph;
        } else if (currentGraph == 2) {
            document.getElementById("collegeGraph").style.display = "none";
            document.getElementById("edcSurveyGraph").style.display = "block";
            currentGraph = 3;
            return currentGraph;
        } else if (currentGraph == 3) {
            document.getElementById("edcSurveyGraph").style.display = "none";
            document.getElementById("highGraph").style.display = "block";
            currentGraph = 1;
            return currentGraph;
        } else {
            console.log("Page error | Page failed to change graphs")
        }
    } else {
        console.log("Page error | Could not change graphs direction")
    }
}