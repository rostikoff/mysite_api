function ajax_form(e) { 
var data_form   = $(e).serialize(); 
name =  $('.add_name').val();
domain_name =  $('#tek_domain_name').val();

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
                $('#addform').fadeOut('300');
                setTimeout(function() {
                $('#add_success').css({ 'display' :'none' });                                 
                $('.add_pass').val('');
                $('.add_name').val('');}, 400)
                }, 1500);
                //pagin_ind('r');
                $('#mail .table').prepend("<tbody><tr><td class='no_mark'><input type='checkbox' name='cheks' class='check' id='"+name+"'></td><td>"+name+"<span id='domain_name'>"+domain_name+"</span></td><td>0</td></tr></tbody>");                
                i=0;
                $('#mail .table tbody:last-child').remove(); 
                $('#jump_3').text(parseInt ($('#jump_3').text()) +1);
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

n_pag = t_str+1;
p_pag = t_str-1;

if (p_pag<1 && strn=='l') {return false;}
if (n_pag>max_pag && strn=='r' ) {return false;}
if (strn[0]=='n') {t_str=1;id_filtr=strn.substring(1);} else {id_filtr = $('.active a').attr('id');}

 //console.log(id_filtr);

$.ajax({
                type: 'POST',
                async: true,
                datatype: 'json',
                url: '/xml_res_pagin/',
                data: { 
                        page: t_str,
                        sost: strn,
                        filtr: id_filtr
                      },
            success: function(data){     
                    $('#mail').html(data);
                    str = $('#in_pole').val();
                    max = $('#max_in_elem').val();
                    vsego = $('#max_in_vsego').val();
                    max_str = $('#max_in_pole').val();
                    
                    if ($('#jump_4').text()=='') {$('#jump_4').text(' – ');}
                    if (str==max_str) {$('#jump_1').text(vsego);}
                    else {$('#jump_1').text((str)*max);}
                    $('#jump_0').text(((str-1)*max)+1);
                    if (vsego==(((str-1)*max)+1)) {$('#jump_0').text('');$('#jump_4').text('');}
                    $('#jump_3').text(vsego);
                    if (vsego=='0') {$('#jump_1').text('0');$('#jump_0').text('');$('#jump_4').text('');}
                                      
                },
            error:  function(data){
console.log(data.responseText);
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
                //alert('данные: ' + data); 
                //console.log(data.responseText);
                 }
  });
}

function aj_filtr(e) {
        event.preventDefault();
        //console.log(e.id);
        i = 0;
        $('.nav-list li').each(function(elem) {i++;
        if (i==1) {} else {$(this).attr('class', '');$(this).attr('style', '');}
        });
        
        $(e).css('background-color', '#EEEEEE');
        setTimeout(function() {$(e).attr('style', '');pagin_ind('n'+e.id);

        i2 = 0;
        $('.nav-list li').each(function(elem) {i2++;
        if (i2==1) {} else {$(this).attr('class', '');}
        
        $(e).parent('li').attr('class', 'active');
        });

        }, 1000);               
}











