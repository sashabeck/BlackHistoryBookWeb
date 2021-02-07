var fireBase = fireBase || firebase;
var hasInit = false;
var firebaseConfig = {
    apiKey: "AIzaSyA9yjSq_U8vYTjveVHoVC_CpZssJ__mjwo",
    authDomain: "strange-descent-296004.firebaseapp.com",
    projectId: "strange-descent-296004",
    storageBucket: "strange-descent-296004.appspot.com",
    messagingSenderId: "205688641263",
    appId: "1:205688641263:web:8e35eb6eeffcb6b3722d1a",
    measurementId: "G-7GELKP36P2"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
//firebase.analytics();
if (!hasInit) {
    firebase.initializeApp(config);
    hasInit = true;
}