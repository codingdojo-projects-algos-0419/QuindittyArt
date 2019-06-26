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
  $('#loginUsername').keyup(function(){
    var data = $("#loginForm").serialize()
    $.ajax({
      method: "POST",
      url: "/users/loginUsername",
      data: data
    })
    .done(function(res){
      $('#loginUsernameMsg').html(res)
    })
  })
})