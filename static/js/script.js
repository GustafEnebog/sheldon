console.log("The java script file says hello!");


function displayDate() {
    document.getElementById("demo").innerHTML = Date();
  }

  console.log("The java script file says hello!");


no
function beenHereFetcher() {
    // https://www.youtube.com/watch?v=cuEtnrL9-H0&t=138s
    // Fetch for "Been Here"
    fetch('https://8000-gustafenebog-sheldon-snyii1xvpkq.ws.codeinstitute-ide.net/admin/textbook/unit/')
        .then(res => {
            if (res.ok) {
                console.log('SUCCESS')
            } else {
                console.log("Not Successful")
            }
        })
        .then(data => console.log(data))
        .catch(error => console.log("ERROR"))
}
// END OF: Fetch for "Been Here"

beenHereFetcher();


function readFetcher() {
    // https://www.youtube.com/watch?v=cuEtnrL9-H0&t=138s
    // Fetch for "Read" and "Understood"
    fetch('https://8000-gustafenebog-sheldon-snyii1xvpkq.ws.codeinstitute-ide.net/admin/textbook/unit/', {
            method: 'POST',
            headers: {
                'Content-Type': "application/json"
            },
            body: JSON.stringify({
                name: 'xxxxxxxxxxxxxxxxx'
            })
        }).then(res => {
            return res.json()
        })
        .then(data => console.log(data))
        .catch(error => console.log('ERROR'))
    // END OF: Fetch for "Read" and "Understood"
}
readFetcher();


function displayDate() {
    document.getElementById("demo").innerHTML = Date();
}

// Conditonal colorcoding of units according to user progress from: https://stackoverflow.com/questions/36587177/how-can-i-conditionally-change-css-styles-with-js
function colorCoding() {
    if (been_here === 1)
        document.getElementById("user-progress-styling").style.backgroundColor = "#E5E5E5";
    else if (read === 1)
        document.getElementById("user-progress-styling").style.backgroundColor = "#80D3FF";
    else if (understood === 1)
        document.getElementById("user-progress-styling").style.backgroundColor = "#40BCFF";
    else
    
    if (bookmark === 1)
        document.getElementById("user-progress-styling").style.border = "red";
}
// END OF: Conditonal colorcoding of units according to user progress from: https://stackoverflow.com/questions/36587177/how-can-i-conditionally-change-css-styles-with-js