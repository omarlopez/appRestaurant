
var services = angular.module('services', [])

services.factory('services', function ($http, $window, $rootScope){

    var urlBase = "http://c45a091f.ngrok.io"
    
    var Services = {}

    Services.step1 = function(reqdata){

        return $http.post(urlBase + '/ajax/create/step1/', reqdata,{
           headers: {'Content-Type': undefined}
        })

    }

    return Services;

})