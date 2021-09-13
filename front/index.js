console.log("Check");

// switches to SignUP Page
let signUpPg=document.getElementById("signup-page");
let loginInPg=document.getElementById("login-page");
let signUpbtn=document.getElementById("SPbtn");
signUpbtn.addEventListener("click",function(){
    loginInPg.classList.add("hide");
    signUpPg.classList.remove("hide");
});


// switches to Login Page
let loginbtn=document.getElementById("login_btn");
loginbtn.addEventListener("click",function(){
    loginInPg.classList.remove("hide");
    signUpPg.classList.add("hide");
});

// Checking login Page
let loginPassword=document.getElementById("login_password");
let bar=document.getElementById("login_password_box");
let msg=document.getElementById("invalid-msg");
loginPassword.addEventListener("click",function(){
    bar.classList.remove("invalid");
    msg.style.display="none";
});
loginPassword.addEventListener("blur",()=>{
    let pss=loginPassword.value;
    if(pss.length<8){
        bar.classList.add("invalid");
        msg.style.display="inline-block";
        console.log("error");
    }
    console.log(loginPassword.value);
    console.log(loginPassword);

});

// Checking SignUP Page
