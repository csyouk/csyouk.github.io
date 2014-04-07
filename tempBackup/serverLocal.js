var http = require('http');
var fs = require('fs');
var port = 3000;


http.createServer(function (req, res) {
  fs.readFile('index.html', function(error, data) {
            res.writeHead(200, {'Content-Type': 'text/html'});
            res.end(data);
   });

}).listen(port,function(){
  console.log('start server port : ' + port);
});
