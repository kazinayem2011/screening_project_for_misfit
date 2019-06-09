// This script only works when epub add and update button is clicked
$('input[type="submit"][id="click_me"]').on('click', function(){

   var language_session_id = document.getElementById('language_session_id').value;
   var epub_session_id = document.getElementById('epub_session_id').value;
   var car_session_id = document.getElementById('car_session_id').value;
   var confirm_upload_msg = document.getElementById('confirm_upload_msg').value;

    if(language_session_id == ''){
        $('.backend_show_error_msg').hide();
        $('.show_error_msg').show();
        $(".show_error_msg span").text("Please select a language first");
        return false;
    }
    else if(car_session_id == '' || epub_session_id == ''){
        $('.backend_show_error_msg').hide();
        $('ul.custom_error_msg').hide();
        $('.show_error_msg').show();
        $(".show_error_msg span").text("Please select both car and epub together");
        return false;
    }
    else {
        if( document.getElementById("id_file").files.length == 0 ) {
            $('.backend_show_error_msg').hide();
            $('.show_error_msg').hide();
            $('ul.custom_error_msg').show();
            $('ul.custom_error_msg li').text('This field is required');
            return false;
        }
        else {
            var uploaded_filename = $("#id_file").val().split('\\').pop();
            var lang_epub_name = document.getElementById('lang_epub_name').value;
            if(uploaded_filename == lang_epub_name){
                if (confirm(confirm_upload_msg)) {
                    // {#    Show loader and disable body#}
                    $("#loading_loader").show();
                    var div = document.createElement("div");
                    div.className += "disable_body";
                    document.body.appendChild(div);
                }
                else {
                    return false;
                }
            }
            else {
                $('.backend_show_error_msg').hide();
                $('ul.custom_error_msg').hide();
                $('ul.errorlist').hide();
                $('.show_error_msg').show();
                $(".show_error_msg span").text('Epub name mismatched found');
                return false;
            }
        }
    }

});

// This Scripts works on uploading combimeter image . . .
$('input[type="submit"][id="combimeter_img_upload"]').on('click', function(){
    var language_session_id = document.getElementById('language_session_id').value;
    var car_session_id = document.getElementById('car_session_id').value;
    var confirm_upload_msg = document.getElementById('confirm_upload_msg').value;

    if(language_session_id == ''){
        $('.backend_show_error_msg').hide();
        $('.show_error_msg').show();
        $(".show_error_msg span").text("Please select a language first");
        return false;
    }
    else if(car_session_id == ''){
        $('.backend_show_error_msg').hide();
        $('ul.custom_error_msg').hide();
        $('.show_error_msg').show();
        $(".show_error_msg span").text("Please select a car first");
        return false;
    }
    else{
        if( document.getElementById("id_file").files.length == 0 ) {
            $('.backend_show_error_msg').hide();
            $('.show_error_msg').hide();
            $('ul.custom_error_msg').show();
            $('ul.custom_error_msg li').text('This field is required');
            return false;
        }
        else {
            var uploaded_filename = $("#id_file").val().split('\\').pop();
            if (uploaded_filename == 'combimeter_button.zip') {
                if (confirm(confirm_upload_msg)) {
                    $("#loading_loader").show();
                    var div = document.createElement("div");
                    div.className += "disable_body";
                    document.body.appendChild(div);
                }
                else {
                    return false;
                }
            }
            else {
                $('.backend_show_error_msg').hide();
                $('ul.custom_error_msg').hide();
                $('ul.errorlist').hide();
                $('.show_error_msg').show();
                $(".show_error_msg span").text('Uploaded file should be a zip file named "combimeter_button.zip"');
                return false;
            }
        }
    }
});

// This script only works in session dropdown to load loader for Language only .
$('input[type="submit"][id="lang_button"]').on('click', function(){
   // Check redirect_url is null or exist. If found error, pass as true with null value . . .
   try {
        var redirect_url = document.getElementById('redirect_url').value;
   } catch (err) {
        if (err.name === 'TypeError')
        {
            redirect_url = 'something_as_url';
        }
   }
    // If not epub download list, Return valiadtion message as required every dropdown.
   if(redirect_url != 'epub:content_download_list'){
       if ($(".lang_dropdown").val() === "") {
           $('.backend_show_error_msg').hide();
           $('.show_error_msg').show();
           $(".show_error_msg span").text("Please select a language first");
           return false;
       }
       else {
            $("#loading_loader").show();
            var div = document.createElement("div");
            div.className += "disable_body";
            document.body.appendChild(div);
       }
   }
   // if epub download list, No validation added as required dropdown. load loader directly.
   else {
       if ($(".lang_dropdown").val() === "") {
           $('.backend_show_error_msg').hide();
           $('.show_error_msg').show();
           $(".show_error_msg span").text("Please select a language first");
           return false;
       }
       else {
            $("#loading_loader").show();
            var div = document.createElement("div");
            div.className += "disable_body";
            document.body.appendChild(div);
       }
   }
});


// This script only works in session dropdown to load loader for Car and Epub only.
$('input[type="submit"][id="car_epub_button"]').on('click', function(){
   // Check redirect_url is null or exist. If found error, pass as true with null value . . .
   try {
        var redirect_url = document.getElementById('redirect_url').value;
   } catch (err) {
        if (err.name === 'TypeError')
        {
            redirect_url = 'something_as_url';
        }
   }
    // If not download list, Return valiadtion message as required every dropdown.
   if(redirect_url != 'epub:content_download_list'){
       if ($("#car_dropdown").val() === "" || $("#epub_dropdown").val() === "") {
           $('.backend_show_error_msg').hide();
           $('.show_error_msg').show();
           $(".show_error_msg span").text("Please select both car and epub together");
           return false;
       }
       else {
            $("#loading_loader").show();
            var div = document.createElement("div");
            div.className += "disable_body";
            document.body.appendChild(div);
       }
   }
   // if download list, No validation added as required dropdown. load loader directly.
   else {
       if ($(".lang_dropdown").val() === "") {
           $('.backend_show_error_msg').hide();
           $('.show_error_msg').show();
           $(".show_error_msg span").text("Please select a language first");
           return false;
       }
       else {
            $("#loading_loader").show();
            var div = document.createElement("div");
            div.className += "disable_body";
            document.body.appendChild(div);
       }
   }
});


// This script only works in session dropdown to load loader for Car only .
$('input[type="submit"][id="car_button"]').on('click', function(){
    // Check redirect_url is null or exist. If found error, pass as true with null value . . .
   try {
        var redirect_url = document.getElementById('redirect_url').value;
   } catch (err) {
        if (err.name === 'TypeError')
        {
            redirect_url = 'something_as_url';
        }
   }
    // If not download list, Return valiadtion message as required every dropdown.
   if(redirect_url != 'images:image_download_list') {
       // If no language in session
       if ($(".lang_dropdown").val() === "") {
           $('.backend_show_error_msg').hide();
           $('.show_error_msg').show();
           $(".show_error_msg span").text("Please select a language first");
           return false;
       }
       // If no car in session
       if ($(".car_dropdown").val() === "") {
           $('.backend_show_error_msg').hide();
           $('.show_error_msg').show();
           $(".show_error_msg span").text("Please select a car first");
           return false;
       }
       else {
           $("#loading_loader").show();
           var div = document.createElement("div");
           div.className += "disable_body";
           document.body.appendChild(div);
       }
   }
   // if image download list, No validation added as required dropdown. load loader directly.
   else {
       if ($(".lang_dropdown").val() === "") {
           $('.backend_show_error_msg').hide();
           $('.show_error_msg').show();
           $(".show_error_msg span").text("Please select a language first");
           return false;
       }
       else {
            $("#loading_loader").show();
            var div = document.createElement("div");
            div.className += "disable_body";
            document.body.appendChild(div);
       }
   }
});


// This script works in executing some submit button to display alert and loader
$('.approve_all,.single_approve,.single_delete,.notify_to_all,.send_push,.send_to_all_failed,.send_again_push_msg,.send_again_push_msg_log').on('click', function(){
   if ($(this).hasClass("approve_all")) {
       var confirm_msg = "Are you sure to approve all?";
   }
   if ($(this).hasClass("single_approve")) {
       var confirm_msg = "Are you sure to approve?";
   }
   if ($(this).hasClass("send_again_push_msg")) {
       var confirm_msg = "Are you sure to send push message again?";
   }
   if ($(this).hasClass("single_delete")) {
       var confirm_msg = "Are you sure to delete update?";
   }
   if ($(this).hasClass("send_push")) {
        total_notification = $(this).attr('data-text');
        var confirm_msg = "Are you sure to send push notification for " + parseInt(total_notification) + " updated content?";
   }
   if ($(this).hasClass("notify_to_all")) {
       var confirm_msg = "Are you sure to send notification to all?";
   }
   if ($(this).hasClass("send_again_push_msg_log")) {
       var confirm_msg = "Are you sure to send again?";
   }
   if ($(this).hasClass("send_to_all_failed")) {
       var confirm_msg = "Are you sure to send message to all failed device?";
   }
   if (confirm(confirm_msg)) {
       $("#loading_loader").show();
       var div = document.createElement("div");
       div.className += "disable_body";
       document.body.appendChild(div);
   }
   else {
       return false;
   }
});
