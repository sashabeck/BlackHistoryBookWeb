firebase.auth().onAuthStateChanged(function(user) {
    if (user) {
        // User is signed in.
        document.getElementById("user_div").style.display = "initial";
        document.getElementById("login_div").style.display = "none";
    } else {
        // No user is signed in.
        document.getElementById("user_div").style.display = "initial";
        document.getElementById("login_div").style.display = "none";
    }
});

function login() {
    var userEmail = document.getElementById("email_field").value;
    var userPass = document.getElementById("password_field").value;
    // window.alert("ddd");
    firebase.auth().createUserWithEmailAndPassword(userEmail, userPass)
        .then((user) => {
            // Signed in
            // ...
            window.alert("dkdk");
        })
        .catch((error) => {
            var errorCode = error.code;
            var errorMessage = error.message;
            // ..
            window.alert(error.message);

        });
    // window.alert(error.message);

}