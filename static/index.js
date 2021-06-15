console.log("done")

var submit = document.querySelector('#submit')

submit.addEventListener('click', function(){
    var imei = document.querySelector('#IMEI-input').value
    fetch('https://imei-validator.herokuapp.com/api/'+imei+"/")
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        var result = document.querySelector('.result');
        result.innerHTML = data.Status
  });
})

