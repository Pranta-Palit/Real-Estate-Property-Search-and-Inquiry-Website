const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

// it has two parameter, fadeout function and time
setTimeout(function(){
    $('#message').fadeOut('slow');
}, 3000);
