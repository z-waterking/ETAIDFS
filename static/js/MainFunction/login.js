$('#LoginEnter').click(function(){
    $.cookie('email', 'abc@qq.com');
    LoginEmail = $('#LoginEmail').val();
    LoginPassword = $('#LoginPassword').val();
    LoginPost = {
        'email':LoginEmail,
        'password':LoginPassword
    };
    $.PostData('LoginEnter', LoginPost, function(data){
        alert(data['msg']);
        if(data['success'] === true){
            //记录自己的邮箱
            $.cookie('iden', data['iden']);
            $.cookie('email', data['email']);
            if(data['iden'] == 1){
                window.location.href="normal";
            }
            else{
                window.location.href="expert";
            }
        }
    })
})