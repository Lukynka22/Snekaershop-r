document.addEventListener("DOMContentLoaded", function() {
    const fileInput = document.getElementById("file-input");
    const profilePic = document.getElementById("profile-pic");

    fileInput.addEventListener("change", function() {
        const file = fileInput.files[0];
        const reader = new FileReader();

        reader.onload = function() {
            profilePic.src = reader.result;
        };

        if (file) {
            reader.readAsDataURL(file);
        }
    });
});
