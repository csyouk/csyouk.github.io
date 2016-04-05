function change(fileName) {
  var location;
  location = fileName + '.html'
  window.location.replace(location);
}
console.log("app init done!");

new Taggle('post1', {
    tags: ['d3']
});
$(".post1").airport(["D3", "Data", "Visualization"],{fill_space: true, transition_speed:1000, loop:false});
