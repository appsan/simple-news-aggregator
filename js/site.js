var mainApp = angular.module('mainApp', ['ui.bootstrap', 'ngResource', 'ngRoute']);

mainApp.controller('TabsCtrl', ['$scope', 'API', function ($scope, API) {
	$scope.reddit = function(){
		$scope.tab_content = API.reddit.query();
	};
	$scope.hackernews = function(){
		$scope.tab_content  = API.hackernews.query();
	};
	$scope.bloomberg = function(){
		$scope.tab_content = API.bloomberg.query();
	};
}]);

mainApp.factory('API', ['$resource', function($resource){
    return {
		reddit: $resource('api/reddit'),
		hackernews: $resource('api/hackernews'),
		bloomberg: $resource('api/bloomberg'),
    };
}]);