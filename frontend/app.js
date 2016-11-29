
code_color = function(code){
    if (code == 'OK'){
        return "green";
     }else{
         return "red";
     }
};

var app = angular.module('bcn_tourist', []);

app.controller('mainCtrl', function($scope, $http) {

    var refresh_data = function() {
         $http.get("/card/all/")
                    .then(function(response) {
                        $scope.all_data = response.data;
                });
    };

    refresh_data();

    $scope.consoleHide = function(){
        console.log($scope.console_show);
        $scope.console_show = false;
    };

    $scope.addCard = function(){

        $http.post("/card/")
            .then(function(response) {
                $scope.console = response.data.info;
                $scope.console_show = true;
                $scope.console_color = code_color(response.data.code);
                refresh_data();
        });


    };

    $http.get("/card/api/info")
        .then(function(response) {
            $scope.api_data = response.data.info;
    });


    $scope.removeCard = function(id){
         $http.delete("/card/"+id+"/")
            .then(function(response) {
                $scope.console = response.data.info;
                $scope.console_show = true;
                $scope.console_color = code_color(response.data.code);
                refresh_data();
        });
    };


    $scope.showPoints = function(id){
        console.log(id);
        var show = $scope.$eval("show_point_"+id);
        console.log(show);
        show = !show;
    };


    $scope.addPoint = function(){

        var data = { "card_id": $scope.card_id,
                     "lat": $scope.lat,
                     "lon": $scope.lon};

        var parameter = JSON.stringify(data);

         $http.post("/card/position", parameter)
            .then(function(response) {
                $scope.console = response.data.info;
                $scope.console_show = true;
                $scope.console_color = code_color(response.data.code);
        });
    };

});

