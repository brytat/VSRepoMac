var img = document.getElementById('crop');

img.setAttribute('data-image', img.src);
img.onmouseover = function () {
    this.src = this.getAttribute('data-hover');
};
img.onmouseout = function () {
    this.src = this.getAttribute('data-image');
}

var img = document.getElementById('cropped-2');

img.setAttribute('data-image', img.src);
img.onmouseover = function () {
    this.src = this.getAttribute('data-hover');
};
img.onmouseout = function () {
    this.src = this.getAttribute('data-image');
}


var img = document.getElementById('cropped-3');

img.setAttribute('data-image', img.src);
img.onmouseover = function () {
    this.src = this.getAttribute('data-hover');
};
img.onmouseout = function () {
    this.src = this.getAttribute('data-image');
}