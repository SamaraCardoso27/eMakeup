var alunoModulo = angular.module('aluno-modulo', ['aluno-servico']);

alunoModulo.directive('alunoForm', [function () {
    return {
        restrict: 'E',
        templateUrl: '/static/aluno/html/form.html',
        scope: {alunoSalvo: '&'},
        controller: function ($scope, AlunoAPI) {
            $scope.aluno = {nome: '', data_nascimento: '', telefone: ''};
            $scope.executandoSalvamento = false;
            $scope.erros = {};

            $scope.salvar = function () {
                $scope.executandoSalvamento = true;
                $scope.erros = {};
                var promessa = AlunoAPI.salvar($scope.aluno);
                promessa.success(function (aluno) {
                    $scope.executandoSalvamento = false;
                    if ($scope.alunoSalvo != null) {
                        $scope.alunoSalvo({'aluno': aluno})
                           $scope.aluno.nome = null;
                           $scope.aluno.data_nascimento = null;
                           $scope.aluno.telefone = null;
                           $scope.class = "ng-isolate-scope ng-hide";
                    }
                });
                promessa.error(function (erros) {
                    $scope.erros = erros;
                    $scope.executandoSalvamento = false;
                });
            }
        }
    };
}]);

alunoModulo.directive('alunoLinha', [function () {
    return {
        restrict: 'A',
        replace: true,
        templateUrl: '/static/aluno/html/linha.html',
        scope: {
            aluno: '=',
            alunoDeletado: '&'
        },
        controller: function ($scope, AlunoAPI) {
            $scope.apagandoFlag = false;
            $scope.editandoFlag = false;
            $scope.alunoEdicao={};
            $scope.deletar = function () {
                $scope.apagandoFlag = true;
                AlunoAPI.deletar($scope.aluno.id).success(function () {
                    $scope.apagandoFlag = false;
                    if ($scope.alunoDeletado != null) {
                        $scope.alunoDeletado();
                    }
                });
            }

            function copiarAluno(origem, destino){
                destino.id=origem.id;
                destino.telefone=origem.telefone;
                destino.nome=origem.nome;
                destino.data_nascimento=origem.data_nascimento;

            }

            $scope.entrarModoEdicao = function () {
                $scope.editandoFlag = true;
                copiarAluno($scope.aluno, $scope.alunoEdicao);
            };

            $scope.sairModoEdicao = function () {
                $scope.editandoFlag = false;
            };

            $scope.editar=function (){
                AlunoAPI.editar($scope.alunoEdicao).success(function(alunoServidor){
                    copiarAluno(alunoServidor,$scope.aluno);
                    $scope.editandoFlag = false;

                });
            }
        }
    };
}]);