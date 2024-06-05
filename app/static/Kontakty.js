function openEmailMenu(email) {
    var subject = "Předmět emailu";
    var body = "Tělo emailu";

    var mailtoUrl = "mailto:" + email + "?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);

    var emailMenu = document.createElement("a");
    emailMenu.href = mailtoUrl;
    emailMenu.style.display = "none";
    document.body.appendChild(emailMenu);


    emailMenu.click();


    document.body.removeChild(emailMenu);
    }
