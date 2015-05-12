$(document).ready(function () {
  var $ajaxSaveGif = $('#ajax-save-gif');
  $ajaxSaveGif.hide();
  var $nameInput = $('#name-input');
    var $birthdayInput = $('#birthday-input');
    var $phone_numberInput = $('#phone_number-input');
    var $courseInput = $('#course-input');

  function obterInputsDeProduto() {
    return {
      'name' :$nameInput.val(),
      'birthday': $birthdayInput.val(),
      'phone_number':$phone_numberInput.val(),
      'course':$courseInput.val()
    };
  }

  var $salvarBotao = $('#salvar-btn');
  $salvarBotao.click(function () {
    $('.has-error').removeClass('has-error');
    $('.help-block').empty();
    $ajaxSaveGif.fadeIn();
    $salvarBotao.attr('disabled','disabled')
    $.post('/students/rest/salvar',
        obterInputsDeProduto(),
        function (student) {
          $('input[type="text"]').val('');
        }).error(function(erro){
          for (propriedade in erro.responseJSON){
            $('#'+propriedade+'-div').addClass('has-error');
            $('#'+propriedade+'-span').text(erro.responseJSON[propriedade]);
          }
        }).always(function(){
          $ajaxSaveGif.hide();
          $salvarBotao.removeAttr('disabled')
        });
  });

});