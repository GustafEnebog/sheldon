console.log("The java script file says hello!");

// https://www.youtube.com/watch?v=cuEtnrL9-H0&t=138s
// Fetch for "Read" and "Understood"
fetch('https://8000-gustafenebog-sheldon-snyii1xvpkq.ws.codeinstitute-ide.net/admin/textbook/unit/', {
    method: 'POST',
    headers: {
        'Content-Type': "application/json"
    },
    body: JSON.stringify({
        name: 'leonardHofstadter'
    })
}).then(res => {
    return res.json()
})
.then(data => console.log(data))
.catch(error => console.log('ERROR'))
// END OF: Fetch for "Read" and "Understood"


function displayDate() {
    document.getElementById("demo").innerHTML = Date();
  }