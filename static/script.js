
sourceBox = document.querySelector(".source-city")
sourceOptions = document.querySelector(".source-box .options-list")

destinationBox = document.querySelector(".destination-city")
destinationOptions =  document.querySelector('.destination-box .options-list')

// Search Box Dropdown Event Listeners
function optionSelector(){

    source = document.querySelectorAll(".source-option")
        for (let i = 0; i < source.length; i++){
            source[i].addEventListener('click', function(){
                value = source[i].querySelector('span')
                sourceBox.value = value.innerHTML
                sourceOptions.classList.remove("active")
            })
        }


    destination = document.querySelectorAll(".destination-option")
    for (let i = 0; i < destination.length; i++){
        destination[i].addEventListener('click', function(){
            value = destination[i].querySelector('span')
            destinationBox.value = value.innerHTML
            destinationOptions.classList.remove("active")
        })
    }
}


// Autocomplete for Source input field
sourceBox.addEventListener('input', async function(){
    sourceOptions.classList.add('active')
    input = sourceBox.value
    if (input) {
        let response = await fetch("/search?p=source&q=" + input)
        let results = await response.text()
        sourceOptions.innerHTML = results
        optionSelector()
    }
    else {
        sourceOptions.classList.remove("active")
    }
})

// Autocomplete for Destination input field 
destinationBox.addEventListener('input', async function(){
    destinationOptions.classList.add("active")

    input = destinationBox.value
    if (input) {
        let response = await fetch("/search?p=destination&q=" + input)
        let results = await response.text()
        destinationOptions.innerHTML = results
        optionSelector()
    }
    else {
        destinationOptions.classList.remove('active')
    }
})