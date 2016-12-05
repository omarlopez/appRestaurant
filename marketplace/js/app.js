

var app = angular.module('app', ['ngRoute', 'food.register','ngMessages'])

app.config(['$routeProvider', function($routeProvider){

    $routeProvider
    .when('/paso1', {
        templateUrl: '../views/register/paso1.html',
        controller: 'formController'
    })

    .when('/paso2', {
        templateUrl: '../views/register/paso2.html',
        controller: 'formController'
    })

    .when('/paso3', {
        templateUrl: '../views/register/paso3.html',
        controller: 'formController'
    })

    .when('/usuario_registrado', {
        templateUrl: '../views/register/usuario_registrado.html'
    })

    .when('/user_profile', {
        templateUrl: '../views/profile/user_profile.html'
    })

    .when('/login', {
        templateUrl: '../views/login/login.html',
        controller: 'formControllerLogin'
    })

    .otherwise({
        redirectTo: '/'
    })

}])