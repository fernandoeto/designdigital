// Menu Hamburguer

let menu = document.querySelector(".menu");
let topNav = document.querySelector(".top-nav-links");

menu.addEventListener("click", function(){
    if(topNav.style.display === "block") {
        topNav.style.display = "none";
    } else {
        topNav.style.display = "block";
    }
});

window.addEventListener("resize", function(){
    if(window.innerWidth >= 770){
        topNav.style.display = "block";
    } else {
        topNav.style.display = "none";
    }
})

// Função validação de e-mail

function checkMail(inputText){
    var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/; 
    var userMail = document.getElementById("idMail").value;
    
if (inputText.value.match(mailformat)) {
    alert("O e-mail " + userMail + " foi cadastrado com sucesso!");
    document.getElementById("ShowMsg").innerHTML="Bem vindo ao Mundo Digital! " + userMail + " !";
    return true;  
}

else {alert("Email inválido");
    event.preventDefault();
    document.form.mail.focus();
    return false;  
    }
};