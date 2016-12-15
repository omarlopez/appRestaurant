
var services = angular.module('services', [])

services.factory('services', function ($http, $window, $rootScope){

    var urlBase = "http://6c1d9ad4.ngrok.io"
    //var urlBase = "http://0.0.0.0:8003"

	var Services = {}

	Services.step1 = function(reqdata){

    	console.log('reqdata', reqdata)
        return $http.post(urlBase + '/ajax/create/step1/', reqdata,{
        	headers: {'Content-Type': undefined}
        })
    }

    return Services;

})