/**
 * Created by Administrator on 2018/8/16.
 */
//alert('01');
$(function(){
  //alert('02');
  //表单提交事件:两次密码有么有错误;用户名是不是已经存在
  $('#formReg').submit(function() {
    //alert('03');
    //alert($('#upwd').val(),$('#uupwd').val());

      if($('#upwd').val() != $('#uupwd').val()){
        //alert('03-1');
        alert("the twise password is different");
        return false
      }
      if($("#phonemsg").html() == '用户名已经存在'){
        //alert('03-2');
        return false
      }
      return true
    });

  //Ajax 异步方式检查电话号码有没有重复
  $('input[name="uphone"]').blur(function(){
    //alert('04');
    if($('#uphone').val()){
      checkphone();
    }
  });
});

//Ajax 异步方式检查电话号码有没有重复
function checkphone(){
  //alert('05');

  var xhr=getXhr();
  xhr.open('post','/checkphone/',true);
  xhr.onreadystatechange=function(){
    if(xhr.readyState==4 && xhr.status==200){
      var regmsg = xhr.responseText;
      //alert('05-3'+regmsg);
      date = JSON.parse(regmsg);
      //alert('05-3'+date);
      $('#phonemsg').html(date.msg);
    }
  };
  xhr.setRequestHeader('Content-Type','application/x-www-form-urlencoded');
  var $phone = $('#uphone').val();
  //alert('05-1'+$phone);
  var $csrftoken = $("input[name='csrfmiddlewaretoken']").val();
  //alert('05-2'+$csrftoken);
  xhr.send('uphone='+$phone+"&csrfmiddlewaretoken="+$csrftoken);

}