
var services = angular.module('services', [])

services.factory('services', function ($http, $window, $rootScope){

    var urlBase = "http://2ad63e7e.ngrok.io"
    
    var Services = {}

    Services.step1 = function(reqdata){

        console.log('reqdata', reqdata)
        return $http.post(urlBase + '/ajax/create/step1/', reqdata,{
            headers: {'Content-Type': undefined}
        })
    }

    return Services;

})