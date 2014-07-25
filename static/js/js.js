function ajax_form(e) { 
var data_form   = $(e).serialize();
        $.ajax({
                type: 'POST',
                async: true,
                datatype: 'json',
                url: '/reg_user_token/',
                data: data_form,
            success: function(data){ 
                code_err = data.charAt(0);
                mess = data.substring(1);
                if (code_err=='0') {
                $('#add_error').css({ 'display' :'none' });
                id='#add_success';
                
                setTimeout(function() { 
                $('.add_pass').val('');
                $('.add_name').val('');
                }, 1500)
                
                setTimeout(function() { 
                $('#addform').fadeOut('1000');
                $('#add_success').css({ 'display' :'none' });
                }, 2000)
                
                pagin_ind('1');
                index=0;
                } 
                else
                { id='#add_error';}
                
                $(id).fadeIn('200');
                $(id).text(mess);
                },
            error:  function(data){
                console.log(data);
            },
            complete: function(data) { 

                 }
  });
}

function pagin_ind(strn) { 
t_str = $('#in_pole').val();
max_pag = $('#max_in_pole').val();
if (t_str==1 && strn=='l') {return false;}
if (t_str==max_pag && strn=='r' ) {return false;} 
$.ajax({
                type: 'POST',
                async: true,
                datatype: 'json',
                url: '/xml_res_pagin/',
                data: { 
                        page: t_str,
                        sost: strn
                      },
                success: function(data){     
                        $('#mail').html(data);
                    },
                error:  function(data){

                },
                complete: function(data) { 

                 }
  });
}

function ajax_del() { 
var i=0;
$(".check:checked").each(function(elem) {i++;});
if (i>0) {if (confirm("Удалить выделенных пользователей?")) {} else {return false;}} else {return false;}
var str = '';
t_str = $('#in_pole').val(); 
$(".check:checked").each(function(elem) { 
	if ($(this).prop("checked")) {
        str+=this.id+',';
	} else { 
	return false;	
	}
});
$.ajax({
                type: 'POST',
                async: true,
                datatype: 'json',
                url: '/delete_user/',
                data: { 
                        data: str
                      },
            success: function(data){     
                pagin_ind(t_str);
                },
            error:  function(data){

            },
            complete: function(data) { 
                $('.windows8').fadeOut('300');
                //alert('данные: ' + data); 
                //console.log(data.responseText);
                 }
  });
}

function aj_filtr(e) {
        event.preventDefault();
        console.log(e.id);
        i = 0;
        $('.nav-list li').each(function(elem) {i++;
        if (i==1) {} else {$(this).attr('class', '');}
        });
        $(e).parent('li').attr('class', 'active');
}









