/**
 * Created by Administrator on 2018/8/16.
 */
//alert('01');
$(function(){
  //alert('02');
  //���ύ�¼�:����������ô�д���;�û����ǲ����Ѿ�����
  $('#formReg').submit(function() {
    //alert('03');
    //alert($('#upwd').val(),$('#uupwd').val());

      if($('#upwd').val() != $('#uupwd').val()){
        //alert('03-1');
        alert("the twise password is different");
        return false
      }
      if($("#phonemsg").html() == '�û����Ѿ�����'){
        //alert('03-2');
        return false
      }
      return true
    });

  //Ajax �첽��ʽ���绰������û���ظ�
  $('input[name="uphone"]').blur(function(){
    //alert('04');
    if($('#uphone').val()){
      checkphone();
    }
  });
});

//Ajax �첽��ʽ���绰������û���ظ�
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