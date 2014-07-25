var index=0;
var speed_but_add = 300

var fil_add=0;
var speed_fil_add = 50
function but_add() { 
                if (index==0) {	
                    $('#addform').fadeIn(speed_but_add);
                    index=1;
                }
                else	 {
                    $('#addform').fadeOut(speed_but_add);	
                    index=0;	
                }
        };
        
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

$(document).ready(function(){
   $(document).click(function(event) {
                
    if ($(event.target).closest("#addform").length) return;
    if ($(event.target).closest("#img_add").length) return;
    if ($(event.target).closest("#but_add").length) return;
    $('#addform').fadeOut(speed_but_add);index=0;
    $('#add_error').css({ 'display' :'none' });
    $('#add_success').css({ 'display' :'none' });
    (event.stopPropagation ? event.stopPropagation() : (event.cancelBubble=true));
                setTimeout(function() { 
                $('.add_pass').val('');
                $('.add_name').val('');
                $('#add_success').css({ 'display' :'none' });
                $('#add_error').css({ 'display' :'none' });
                }, 400)
  });
});



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