console.log("done")

var submit = document.querySelector('#submit')

submit.addEventListener('click', function(){
    var imei = document.querySelector('#IMEI-input').value
    fetch('http://127.0.0.1:8000/api/'+imei+"/")
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        var result = document.querySelector('.result');
        result.innerHTML = data.Status
  });
})

