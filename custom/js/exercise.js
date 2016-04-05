console.log("hello");
// prism.js 로 대체.
// var codes = document.getElementsByTagName("code");
// _.each(codes, function(code){
//   code.innerHTML = code.innerText.replace(";",";<br>")
// })
// var pTagList = document.getElementById('p-tag-list');
// pTagList.

var scroll = function(element){
  var ele = document.getElementById(element);
  window.scrollTo(ele.offsetLeft, ele.offsetTop);
}

var freeze = function(element){
  var ele = document.getElementById(element);
  ele.style.position = 'fixed';
  ele.style.bottom = 0;
  ele.style.right = 0;
  ele.style.width = '200px';
  ele.style.height = (window.innerHeight/1.3) + "px";
  ele.style.color = "black";
  ele.style.backgroundColor = 'gray';
}
