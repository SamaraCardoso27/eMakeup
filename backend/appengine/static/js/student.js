$(document).ready(function () {
  var $ajaxSaveGif = $('#ajax-save-gif');
  $ajaxSaveGif.hide();
  var $nameInput = $('#name-input');
  var $birthdayInput = $('#birthday-input');
  var $phone_numberInput = $('#phone_number-input');
  var $courseInput = $('#course-input');
  var $studentsUl = $('#students-ul');


    function addStudent(student) {
    //var li = '<li id="li-' + student.id + '"';
    //li = li + '><button id="btn-deletar-' + student.id + '"';
    //li = li + ' class="btn btn-danger"><i class="glyphicon glyphicon-trash"></i></button>';
    //li = li + student.name + '</li>';
        //var li = '<td id="li-' + student.id + '">'+student.name+'</td>';
//li = li + '<td>'+student.birthday+'</td>';
//li = li + '<td>'+student.phone_number+'</td>';
//li = li + '<td><button id="btn-deletar-' + student.id + '"class="btn btn-danger"><i class="glyphicon glyphicon-trash"></i></button></td>'
var li = '<tr><th id="li-' + student.id + '">'+student.name+'</th><td>'+student.birthday+'</td><td>'+student.phone_number+'</td><td><button id="btn-deletar-' + student.id + '"class="btn btn-danger"><i class="glyphicon glyphicon-trash"></i></button></td></tr>'
    $studentsUl.append(li);
    $('#btn-deletar-' + student.id).click(function () {
      $.post('/students/rest/deletar', {student_id: student.id}, function () {
        $("#li-"+student.id).remove();
      });
    });
  }





  $.get('/students/rest/listar',function(students){
    $.each(students, function(index, stu){
      addStudent(stu);
    });
  });





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
            addStudent(student);
          $('input[type="text"]').val('');
            $('#exampleModal').hide();
            $("body" ).removeClass();
            $('.modal-backdrop').hide();
        }).error(function(erro){
          for (propriedade in erro.responseJSON){
            $('#'+propriedade+'-div').addClass('has-error');
            $('#'+propriedade+'-span').text(erro.responseJSON[propriedade]);
          }
        }).always(function(){
          $ajaxSaveGif.hide();
          $salvarBotao.removeAttr('disabled');
          $("body" ).removeClass( ".modal-open" );
        });
  });
});