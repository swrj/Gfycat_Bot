// ==UserScript==
// @name        Gfycat Details Link Fixer
// @namespace   gfy
// @description Script that converts the url to the bloated page to the old direct link
// @include     *gfycat.com/gifs/detail/*
// @include     *gfycat.com/*/gifs/detail*
// @version     1.00
// ==/UserScript==

var url = window.location.href;

url = url.split("/");                
url = "https://gfycat.com/" + url[url.length-1];

document.body.innerHTML = "";

var frame = document.createElement('iframe');
frame.setAttribute('frameborder', '0');
frame.setAttribute('scrolling', 'no');
frame.setAttribute('src', url);
frame.setAttribute('height', '100%');
frame.setAttribute('width', '100%');
document.body.appendChild(frame);

history.replaceState('', document.title, url);
