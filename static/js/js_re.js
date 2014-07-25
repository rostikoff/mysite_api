var index=0;
var fil_add=0;
var index_for_but_del=0;
var index_for_opt=0;
var speed_but_add = 300
var speed_fil_add = 50


//JavaScript для открытия/закрытия формы "Добавления"
function but_add() { 
    if (index==0) {	
        $('#addform').fadeIn(speed_but_add); index=1;
    }
    else	 {
        $('#addform').fadeOut(speed_but_add); index=0;	
    }
};
//JavaScript для открытия/закрытия формы "Настройки"
function but_option() { 
    if (index_for_opt==0) {	
        $('#form_options').fadeIn(speed_but_add); index_for_opt=1;
    }
    else	 {
        $('#form_options').fadeOut(speed_but_add); index_for_opt=0;	
    }
};
$(document).ready(function(){
    $(document).click(function(event) {
        if ($(event.target).closest("#addform").length) return;
        if ($(event.target).closest("#img_add").length) return;
        if ($(event.target).closest("#but_add").length) return;
        if ($(event.target).closest("#tab_but_option").length) return;
        if ($(event.target).closest("#form_options").length) return;
        $('#addform').fadeOut(speed_but_add);index=0;
        $('#add_error').css({ 'display' :'none' });
        $('#add_success').css({ 'display' :'none' });
        $('#form_options').fadeOut(speed_but_add);index_for_opt=0;
        (event.stopPropagation ? event.stopPropagation() : (event.cancelBubble=true));
    });
});


//JavaScript для добавления фильтра
function new_fil() { 
    if (fil_add==0) {	
        $('#inp_fil_add').fadeIn(speed_fil_add);
        $('#btn_fil_add').css({ 'background': 'url(/static/img/glyphicons-halflings.png) -428px -93px' });
        fil_add=1;
    }
    else	 {
        $('#inp_fil_add').fadeOut(speed_fil_add);
        $('#btn_fil_add').css({ 'background': 'url(/static/img/glyphicons-halflings.png) -403px -93px' });	
        fil_add=0;	
    }
};    
                    
                    
$(document).ready(function() { 
//JavaScript для перегрузки страницы
     $('#but_del').click(function() {
         $('.windows8').css({ 'display' :'block' });
         $('.table').css({ 'opacity' :'0.2' });
         /*location.reload(); */
    });
})        

$(document).ready(function() { 
// Скрипт для скрытия кнопки удаления      
    $('.check').on('change',function() {
        var 
            active = 'hide',
            obj    = $('#but_del');
        if ( $('.check').is(":checked") ) {
            active = 'show';
            obj[ active ]();
        }
        else 
            $('#but_del').fadeOut(speed_fil_add);
    });
    
    $('#check_all').live('click', function(){ 
        if (!$(".check").prop("checked")) {
            $('#but_del').fadeOut(speed_fil_add);
        }
        else  {
           $('#but_del').fadeIn(speed_fil_add);
       }
    });        
})
 






$(document).ready(function() {
//Скрипт генерации паролей
    function str_rand() {
        var result       = '';
        var words        = '0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM';
        var max_position = words.length - 1;
            for( i = 0; i < 10; ++i ) {
                position = Math.floor ( Math.random() * max_position );
                result = result + words.substring(position, position + 1);
            }
        return result;
    }
    
    $('#show').click(function(){     
        if ($('.add_pass:[name = pass1]').get(0).type=='password') $('.add_pass:[name = pass1]').get(0).type='text'; else $('.add_pass:[name = pass1]').get(0).type='password';
        if ($('.add_pass:[name = pass2]').get(0).type=='password') $('.add_pass:[name = pass2]').get(0).type='text'; else $('.add_pass:[name = pass2]').get(0).type='password';
    });
    $('#generate').click(function() {
        $('.add_pass').attr('value', str_rand());
    });

    $('#check_all').live('click', function(){ 
        if (!$("#check_all").prop("checked")) {
            $(".check").removeAttr("checked");
            $("#check_all").removeAttr("checked");}
        else {
            $(".check").attr("checked","checked");}
    });
});