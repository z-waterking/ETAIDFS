$('#LoginEnter').click(function(){
    LoginEmail = $('#LoginEmail').val()
    LoginPassword = $('#LoginEmail').val()

    LoginPost = {
        'email':LoginEmail,
        'password':LoginPassword
    }
    $.PostData('LoginEnter', LoginPost, function(data){
        if(data['success'] == true){
            alert('OK');
            window.location.href= "normal"
        }

    })
})