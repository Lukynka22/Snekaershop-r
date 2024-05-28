document.addEventListener('DOMContentLoaded', function () {
    var menuItems = document.querySelectorAll('#menu li a');

        menuItems.forEach(function (menuItem) {
        menuItem.addEventListener('mouseover', function () {
            menuItem.style.backgroundColor = 'black';
            menuItem.style.color = 'black';
            menuItem.style.transform = 'scale(1.1)';
        });

                menuItem.addEventListener('mouseout', function () {
            menuItem.style.backgroundColor = '';
            menuItem.style.color = '';
            menuItem.style.transform = '';
        });
    });
});
