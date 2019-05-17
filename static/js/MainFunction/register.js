$('#RegisterEnter').click(function(){
    UserName = $('#RegisterUsername').val()
    Password = $('#RegisterPassword').val()
    Password2 = $('#RegisterPassword2').val()
    Email = $('#RegisterEmail').val()

    if(Password != Password2){
        alert('两次输入密码不同，请重新输入');
        return;
    }

    RegisterPost = {
        'username':UserName,
        'password':Password,
        'email': Email
    }

    $.PostData('RegisterEnter', RegisterPost, function(data){
        if(data['success'] == true){
            alert('OK');
            window.location.href = "login"
        }
    })
})

