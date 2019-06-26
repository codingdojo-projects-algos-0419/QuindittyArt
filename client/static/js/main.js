$(document).ready(function(){
  $('#username').keyup(function(){
    var data = $("#regForm").serialize()
    $.ajax({
      method: "POST",
      url: "/users/username",
      data: data
    })
    .done(function(res){
      $('#usernameMsg').html(res)
    })
  })
})