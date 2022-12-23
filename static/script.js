document.addEventListener("DOMContentLoaded", function(){
    source = document.querySelectorAll(".source-option")
    sourceBox = document.querySelector(".source-city")
    destination = document.querySelectorAll(".destination-option")
    destinationBox = document.querySelector(".destination-city")

    for (let i = 0; i < source.length; i++){
        console.log(source[i].innerHTML)
        source[i].addEventListener('click', function(){
            value = source[i].querySelector('span')
            sourceBox.value = value.innerHTML
        })
    }

    for (let i = 0; i < destination.length; i++){
        destination[i].addEventListener("click", function(){
            value = destination[i].querySelector('span')
            destinationBox.value = value.innerHTML
        })
    }

    

})

