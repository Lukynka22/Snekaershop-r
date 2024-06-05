function openEmailMenu(email) {
    var subject = "Předmět emailu";
    var body = "Tělo emailu";

    var mailtoUrl = "mailto:" + email + "?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);
