'use strict;'
function change(fileName) {
  var location;
  location = fileName + '.html'
  window.location.replace(location);
}
function getRandomInt(min, max){
  return Math.floor(Math.random()*(max-min)) + min;
}

(function makeImageSize(){
  function imgSizeSetter(img){
    img.style.width = img.style.height = imgSquareSize;
  }
  var imgs = document.getElementsByTagName("img");
  var imgSquareSize = String(window.innerHeight/10)+"px";
  for (var i = 0; i < imgs.length; i++) {
    imgSizeSetter(imgs[i]);
  };
})()


new Taggle('post1', {
    tags: ['d3']
});
new Taggle('post2', {
    tags: ['java','generic','oop']
});
$(".post1").airport(["Data", "Visualization", "With D3.js"],{fill_space: true, transition_speed:getRandomInt(1000,3000), loop:true});
$(".post2").airport(["Java", "Generic"],{fill_space: true, transition_speed:getRandomInt(1000,3000), loop:true});



console.log("app init done!");
