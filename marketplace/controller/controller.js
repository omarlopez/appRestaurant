

var app =  angular.module('food.register', ['services'])

app.controller('formController', function($scope, $window, $location, services){

    $scope.step1 = function(){

        // ajax
        $scope.data = {
            'name': $scope.form.name,
            'user': $scope.form.user,
            'email': $scope.form.email,
            'password': $scope.form.pass
        }

        services.step1($scope.data).success(function (data, status, headers, config){
            
            console.log(data, status)
            if(data.code == 1){
                //code 1 = el usuario ya existe
                window.location = '#continue-register'
            }
            if(data.code == 0){
                // code 0 = el usuario registrado exitoso
                window.location = '#paso2'
            }

        }).error(function (data, status, headers, config){
            console.log(data, status)
        })

        //window.location = '#paso2' 
    }

    $scope.step2 = function(){
        window.location = '#paso3'
    }

    $scope.final = function(){
        window.location = '#usuario_registrado'
    }
    
})

app.controller('formControllerLogin', function($scope, $window, $location){

    $scope.login = function(){
        window.location = '#paso1'
    }
    
})