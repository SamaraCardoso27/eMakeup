$(document).ready(function () {
    var $alunoForm = $('#aluno-form');
    $alunoForm.hide();
    $('#mostrar-form-btn').click(function () {
        $alunoForm.slideToggle();
    });


    var $nomeInput = $('#nomeInput');
    var $data_nascimentoInput = $('#data_nascimentoInput');
    var $telefoneInput = $('#telefoneInput');
    var $ajaxGif = $('#ajax-gif');

    var $nomeDiv = $('#nomeDiv');

    $ajaxGif.hide();
    var $salvarBtn = $('#salvar-btn');
    var $helpTituloSpan = $('#help-nome');
    var $corpoTabela = $('#corpo-tabela');

    var adicionarLinha=function adicionarLinha(aluno) {
        var linha = '<tr id="tr' + aluno.id + '"> <td>' + aluno.nome + '</td>' +
            '<td>' + aluno.data_nascimento + '</td>' +
            '<td>' + aluno.telefone + '</td>' +
            '<td><button id="bt' + aluno.id + '" class="btn btn-danger btn-sm"><i class="glyphicon glyphicon-trash"></i></button>' +
            '</td> </tr>';

        $corpoTabela.prepend(linha);

        var $linhaHtml = $('#tr' + aluno.id);

        $linhaHtml.hide();
        $linhaHtml.fadeIn();
        $('#bt' + aluno.id).click(function () {
            $linhaHtml.fadeOut();
            $.post('/alunos/rest/delete',{'aluno_id':aluno.id}).success(function(){
                $linhaHtml.remove();
            }).error(function(){
                alert('Remoção não funcionou');
                $linhaHtml.fadeIn();
            });
        });
    }

    $.get('/alunos/rest').success(function (listaDeFilmes) {
        for (var i = 0; i < listaDeFilmes.length; i += 1) {
            adicionarLinha(listaDeFilmes[i]);
        }

    });

    $salvarBtn.click(function () {
        var aluno = {nome: $nomeInput.val(),
            data_nascimento: $data_nascimentoInput.val(),
            telefone: $telefoneInput.val()};

        $ajaxGif.slideDown();
        $salvarBtn.hide();
        var promessa = $.post('/alunos/rest/save', aluno);
        promessa.success(function (aluno_do_servidor) {
            adicionarLinha(aluno_do_servidor);
        });


        promessa.error(function (erros) {
            if (erros.responseJSON != null && erros.responseJSON.nome != null) {
                $nomeDiv.addClass('has-error');
                $helpTituloSpan.text(erros.responseJSON.nome);
            }
        });

        promessa.always(function () {
            $ajaxGif.slideUp();
            $salvarBtn.slideDown();
        })
    });

});
